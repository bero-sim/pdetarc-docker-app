# https://github.com/bero-sim/pdetarc-docker-app/blob/main/pdetarc.py
import os
import sys
import json
import tarfile
import gzip
import hashlib
import urllib.request
import zipfile
import shutil
from pathlib import Path
from datetime import datetime, UTC

# Python 3.11+
import tomllib

FIXED_TS = 946684800  # 2000-01-01 UTC


# ------------------------
# ログ
# ------------------------
def log(msg, logfile=None):
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S} UTC] {msg}"
    print(line)

    if logfile:
        with open(logfile, "a", encoding="utf-8-sig") as f:
            f.write(line + "\n")


# ------------------------
# SHA256
# ------------------------
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


# ------------------------
# 衝突回避コピー
# ------------------------
def copy_with_collision(src, ROOT):
    target = ROOT / src.name

    if target.exists():
        stem = src.stem
        suffix = src.suffix
        i = 1
        while True:
            new = ROOT / f"{stem}_{i}{suffix}"
            if not new.exists():
                target = new
                break
            i += 1

    with open(src, "rb") as s, open(target, "wb") as d:
        d.write(s.read())

    os.utime(target, (FIXED_TS, FIXED_TS))
    return target.name


# ------------------------
# ZIP展開（衝突対応）
# ------------------------
def extract_zip_with_collision(zip_path, ROOT):
    extracted = []

    with zipfile.ZipFile(zip_path) as z:
        for name in sorted(z.namelist()):
            if name.endswith("/"):
                continue

            base = Path(name).name
            target = ROOT / base

            if target.exists():
                stem = target.stem
                suffix = target.suffix
                i = 1
                while True:
                    new = ROOT / f"{stem}_{i}{suffix}"
                    if not new.exists():
                        target = new
                        break
                    i += 1

            with z.open(name) as src, open(target, "wb") as dst:
                dst.write(src.read())

            os.utime(target, (FIXED_TS, FIXED_TS))
            extracted.append(target.name)

    return extracted


# ------------------------
# 内容の事前検査（フォルダ直下にmanifest.jsonがある場合）
# ------------------------
def verify_existing_manifest(input_path, logfile):
    manifest_path = os.path.join(input_path, "manifest.json")
    if not os.path.exists(manifest_path):
        return True 

    log(f"既存の manifest.json を検出しました。整合性を検査します...", logfile)
    
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest_data = json.load(f)
        
        # マニフェストに記載されたファイルの集合を作成
        manifest_files = manifest_data.get("files", [])
        manifest_path_set = {item['path'] for item in manifest_files}
        
        # 1. 記録されているファイルが正しく存在し、ハッシュが一致するか
        for item in manifest_files:
            file_path = os.path.join(input_path, item['path'])
            if not os.path.exists(file_path):
                log(f"ERROR: 記録されたファイルが見つかりません -> {item['path']}", logfile)
                return False
            
            if sha256_file(file_path) != item['sha256']:
                log(f"ERROR: ハッシュ不一致 -> {item['path']}", logfile)
                return False

        # 2. 実際のarchiveフォルダを走査し、マニフェストにないファイルがないかチェック
        # ※ archive フォルダのみを対象にする
        archive_root = os.path.join(input_path, "archive")
        if os.path.exists(archive_root):
            for root, dirs, files in os.walk(archive_root):
                for file in files:
                    full_path = os.path.join(root, file)
                    # input_path からの相対パスを取得 (manifestのpath形式に合わせる)
                    rel_path = os.path.relpath(full_path, input_path).replace(os.sep, '/')
                    
                    if rel_path not in manifest_path_set:
                        log(f"ERROR: マニフェストに未記載のファイルが混入しています -> {rel_path}", logfile)
                        return False
        
        log("事前検査完了: すべてのファイルの整合性が確認されました（混入なし）。", logfile)
        return True
    except Exception as e:
        log(f"ERROR: マニフェスト読み込みエラー: {e}", logfile)
        return False


# ------------------------
# backup退避
# ------------------------
def move_to_backup(ROOT):
    archive_dir = ROOT / "archive"
    backup_dir = ROOT / "backup"

    backup_dir.mkdir(exist_ok=True)

    for item in ROOT.iterdir():
        if item.name in ("archive", "backup"):
            continue

        shutil.move(str(item), backup_dir / item.name)


# ------------------------
# メイン
# ------------------------
def main():
    if len(sys.argv) < 2:
        print("Usage: pdetarc.py <input_dir>")
        sys.exit(1)

    ROOT = Path(sys.argv[1]).resolve()
    base_dir = ROOT.parent
    OUT = base_dir / (ROOT.name + ".pdetarc.gz")
    
    logfile = os.path.join(base_dir, "pdetarc.log")

    log("==== PDETARC START ====", logfile)
    log("モード: 圧縮", logfile)
    log(f"入力: {ROOT}", logfile)

    archive_dir = ROOT / "archive"
    if not archive_dir.exists():
        log("ERROR: archive folder not found", logfile)
        sys.exit(1)

    if not verify_existing_manifest(ROOT, logfile):
        log("ERROR: 事前検査失敗。処理を中断します。", logfile)
        sys.exit(1)

    # ------------------------
    # backup退避
    # ------------------------
    move_to_backup(ROOT)

    # ------------------------
    # bundle処理
    # ------------------------
    bundle_dir = archive_dir / "portable-deterministic-archive-v1"
    bundle_toml = bundle_dir / "bundle.toml"

    bundles = []
    if bundle_toml.exists():
        with open(bundle_toml, "rb") as f:
            bundles = tomllib.load(f).get("bundle", [])

    bundle_hash = []

    for b in bundles:
        url = b["url"]
        fname = b["file"]
        sha_expected = b["sha256"]

        src = bundle_dir / fname

        if not src.exists():
            log(f"[DL] {url}", logfile)
            urllib.request.urlretrieve(url, src)

        sha_actual = sha256_file(src)
        if sha_actual != sha_expected:
            raise Exception(f"SHA mismatch: {fname}")

        extracted = []

        if fname.endswith(".zip"):
            extracted = extract_zip_with_collision(src, ROOT)
        else:
            name = copy_with_collision(src, ROOT)
            extracted.append(name)

        bundle_hash.append({
            "name": fname,
            "file": fname,
            "url": url,
            "sha256": sha_actual,
            "source": b.get("source", ""),
            "extracted": extracted
        })

    # READMEコピー（bundle.tomlとは別扱い）
    readme = bundle_dir / "README.pdf"
    if readme.exists():
        copy_with_collision(readme, ROOT)

    # ------------------------
    # bundle-hash.json
    # ------------------------
    bundle_hash_path = ROOT / "bundle-hash.json"
    with open(bundle_hash_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(bundle_hash, f, indent=2, sort_keys=True)
    os.utime(bundle_hash_path, (FIXED_TS, FIXED_TS))

    # ------------------------
    # ファイル収集（archiveのみ）
    # ------------------------
    files = []

    for p in sorted(archive_dir.rglob("*")):
        if p.is_file():
            rel = p.relative_to(ROOT).as_posix()
            files.append((rel, p))

    # ------------------------
    # manifest
    # ------------------------
    manifest = {
        "format": "portable-deterministic-archive-v1",
        "tool_version": "PDETARC_1.0.0",
        "build": datetime.fromtimestamp(FIXED_TS, UTC).strftime("%Y-%m-%d-%H-%M-%S"),
        "files": []
    }

    for i, (rel, path) in enumerate(files, 1):
        manifest["files"].append({
            "id": f"{i:08d}",
            "path": rel,
            "size": path.stat().st_size,
            "sha256": sha256_file(path)
        })

    manifest_path = ROOT / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, indent=2, sort_keys=True)
    os.utime(manifest_path, (FIXED_TS, FIXED_TS))

    # ------------------------
    # filesディレクトリ
    # ------------------------
    files_dir = ROOT / "files"
    if files_dir.exists():
        shutil.rmtree(files_dir)
    files_dir.mkdir()

    for i, (rel, path) in enumerate(files, 1):
        dst = files_dir / f"{i:08d}"
        with open(path, "rb") as s, open(dst, "wb") as d:
            d.write(s.read())
        os.utime(dst, (FIXED_TS, FIXED_TS))

    # ------------------------
    # tar作成
    # ------------------------
    tmp_tar = ROOT.parent / (ROOT.name + ".tmp.tar")

    with tarfile.open(tmp_tar, "w") as tar:

        def add_file(path, arcname):
            info = tar.gettarinfo(path, arcname)
            info.mtime = FIXED_TS
            info.uid = 0
            info.gid = 0
            info.uname = ""
            info.gname = ""
            with open(path, "rb") as f:
                tar.addfile(info, f)

        # files/
        for f in sorted(files_dir.glob("*")):
            add_file(f, f"files/{f.name}")

        # ルートファイル
        for f in sorted(ROOT.glob("*")):
            if f.name in ("files", "backup"):
                continue
            if f.is_file():
                add_file(f, f.name)

    # ------------------------
    # gzip
    # ------------------------
    with open(tmp_tar, "rb") as f_in:
        with gzip.GzipFile(OUT, "wb", mtime=FIXED_TS) as f_out:
            while chunk := f_in.read(8192):
                f_out.write(chunk)

    os.remove(tmp_tar)
    shutil.rmtree(files_dir, ignore_errors=True)

    log(f"完了: {OUT}", logfile)
    log("==== PDETARC END ====", logfile)


if __name__ == "__main__":
    main()
