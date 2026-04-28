<!-- https://github.com/bero-sim/pdetarc-docker-app/blob/main/Operation-verification.md -->
# 🟫PDETARC V1.0.0 構築～検証ログ

# 🟫目次

1. 🟫PDETARCリポジトリ構築
   1. 🟥pdetarc-docker-appリポジトリ
      1. 👉Create a new repository
      1. 👉pdetarc-docker-appのworkflowでエラーが出ないように権限を与える
      1. 👉creating a new file；作成し保存（コミット）する
      1. 👉Upload files
      1. 👉タグの削除
      1. 👉タグv1.0.0をプッシュしてアセット生成
      1. 👉Workflowログ確認
      1. 👉Node.js 24のワーニング対策
      1. 👉Node.js 24のワーニング対策したWorkflowログ確認
      1. 👉Releases Assets確認#
   1. 🟥pdetarc-toolsリポジトリ
      1. 👉Create a new repository
      1. 👉pdetarc-toolsのworkflowでエラーが出ないように権限を与える
      1. 👉creating a new file；作成し保存（コミット）する
      1. 👉Upload files
      1. 👉タグの削除
      1. 👉タグv1.0.0をプッシュしてアセット生成
      1. 👉Workflowログ確認
      1. 👉Node.js 24のワーニング対策
      1. 👉Node.js 24のワーニング対策したWorkflowログ確認
      1. 👉Releases Assets確認
1. 🟫検証用の圧縮対象フォルダ作成
   1. 🟥検証用フォルダ作成・公開
      1. 👉test_data.tar.gz の作成・アップロード
      1. 👉Releases Assets確認
   1. 🟥検証用フォルダのダウンロード・展開
      1. 👉test_data.tar.gzをリポジトリよりダウンロード・解凍してtest_dataフォルダを作成
1. 🟫動作検証
   1. 🟥生成ツールのdockerビルド
      1. 👉pdetarc-docker-appのソースファイルをリポジトリよりダウンロードして解凍
      1. 👉Docker起動
      1. 👉Docker版pythonのハッシュ値確認
      1. 👉Dockerビルド実行
   1. 🟥Dockerビルドベースの動作検証
      1. 👉動作検証前の状況確認
      1. 👉test_dataフォルダをpdetarc.batにD&D
      1. 👉圧縮ツールの時間表示は標準時のUTCで表示のため9時間遅い
      1. 👉圧縮結果確認
      1. 👉test_data.pdetarc.gzをpdetarc.batにD&D
      1. 👉圧縮専用だからエラー（正常動作）
      1. 👉test_data.pdetarc.gzからpdetarc-extract-windows.exeを取り出す。
      1. 👉test_data.pdetarc.gzをpdetarc-extract-windows.exeにD&D
      1. 👉test_dataを揺さぶってみる（ZIP圧縮・解凍）
      1. 👉揺さぶったtest_dataフォルダをpdetarc-extract-windows.exeにD&D
      1. 👉解凍できないためエラー（正常動作）
      1. 👉test_dataフォルダをpdetarc.batにD&D
      1. 👉bashで状況確認
      1. 👉test_dataフォルダを揺さぶっても同じハッシュ値再現した。
      1. 👉test_data.pdetarc.gzを右クリックですべて展開する。
      1. 👉test_data.pdetarcをpdetarc.batにD&Dする。
      1. 👉bash確認
      1. 👉.pdetarcは圧縮対象ではないためエラー（正常動作）
      1. 👉test_data.pdetarcをpdetarc-extract-windows.exeにD&Dする。
      1. 👉test_data.pdetarcの中間状態から解凍したtest_dataをpdetarc.batにD&Dする。
      1. 👉bashで状況確認
      1. 👉test_data.pdetarcの中間状態から解凍後に圧縮しても同じハッシュ値再現した。
   1. 🟥Dockerイメージを使った動作検証
      1. 👉Dockerイメージを全て削除
      1. 👉test_dataをpdetarc.batにD&Dする。
      1. 👉Dockerイメージ削除したから動かない。（正常動作）
      1. 👉Dockerイメージ（pdetarc_image_v1.0.0.tar）の読み込み
      1. 👉test_dataをpdetarc.batにD&Dする。
      1. 👉bash確認
      1. 👉Dockerイメージを読み込んで圧縮しても同じハッシュ値が生成された。
      1. 👉コマンドを使って圧縮
      1. 👉コマンドを使って圧縮しても同じハッシュ値が生成された。
      1. 👉test_dataフォルダのルート直下にあったものはbackupフォルダに退避されている。
      1. 👉動作検証完了。

---

# 1. 🟫PDETARCリポジトリ構築

## ⅰ. 🟥pdetarc-docker-appリポジトリ

### a. 👉Create a new repository
1. Repository name: `pdetarc-docker-app`
2. Description: `決定論的アーカイブ形式PDETARCの圧縮専用Dockerコンテナアプリ▶入力: <folder/> を pdetarc.bat にドラッグ＆ドロップ▶出力: <folder>.pdetarc.gz へ圧縮`
3. 「Create repository」をクリック

### b. 👉pdetarc-docker-appのworkflowでエラーが出ないように権限を与える
- Settings/Actions/General/Workflow permissions/に移動
  1. 「Read and write permissions」を選択
  2. 「Allow GitHub Actions to create and approve pull requests」にチェック
  3. 「Save」をクリック

### c. 👉creating a new file；作成し保存（コミット）する
1. https://github.com/bero-sim/pdetarc-docker-app/blob/main/pdetarc.py
2. https://github.com/bero-sim/pdetarc-docker-app/blob/main/Dockerfile
3. https://github.com/bero-sim/pdetarc-docker-app/blob/main/pdetarc.bat
4. https://github.com/bero-sim/pdetarc-docker-app/blob/main/.github/workflows/release-assets.yml
5. https://github.com/bero-sim/pdetarc-docker-app/blob/main/README.md
6. https://github.com/bero-sim/pdetarc-docker-app/blob/main/LICENSE.md

### d. 👉Upload files
1. https://github.com/bero-sim/pdetarc-docker-app/blob/main/pdetarc_concepts.png

### e. 👉タグの削除
1. https://github.com/bero-sim/pdetarc-docker-app/releases の Releases を全部削除
2. https://github.com/bero-sim/pdetarc-docker-app/releases の Tags を全部削除

### f. 👉タグv1.0.0をプッシュしてアセット生成

```
PS C:\Users\info> cd C:\Users\info\Documents\Git-ws
PS C:\Users\info\Documents\Git-ws> Remove-Item -Path "pdetarc-docker-app" -Recurse -Force
PS C:\Users\info\Documents\Git-ws> git clone https://github.com/bero-sim/pdetarc-docker-app.git
Cloning into 'pdetarc-docker-app'...
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Compressing objects: 100% (20/20), done.
remote: Total 23 (delta 5), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (23/23), 1.75 MiB | 2.11 MiB/s, done.
Resolving deltas: 100% (5/5), done.
PS C:\Users\info\Documents\Git-ws> cd .\pdetarc-docker-app\
PS C:\Users\info\Documents\Git-ws\pdetarc-docker-app> git add .
PS C:\Users\info\Documents\Git-ws\pdetarc-docker-app> git commit -m "fix workflow"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
PS C:\Users\info\Documents\Git-ws\pdetarc-docker-app> git push origin main
Everything up-to-date
PS C:\Users\info\Documents\Git-ws\pdetarc-docker-app> git tag v1.0.0
PS C:\Users\info\Documents\Git-ws\pdetarc-docker-app> git push origin v1.0.0
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/bero-sim/pdetarc-docker-app.git
 * [new tag]         v1.0.0 -> v1.0.0
PS C:\Users\info\Documents\Git-ws\pdetarc-docker-app>
```

### g. 👉Workflowログ確認
https://github.com/bero-sim/pdetarc-docker-app/actions/runs/25025829602

```
Annotations
1 warning
build-and-release
Node.js 20 actions are deprecated. The following actions are running on Node.js 20 and may not work as expected: actions/checkout@v4, softprops/action-gh-release@v2. Actions will be forced to run with Node.js 24 by default starting June 2nd, 2026. Node.js 20 will be removed from the runner on September 16th, 2026. Please check if updated versions of these actions are available that support Node.js 24. To opt into Node.js 24 now, set the FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true environment variable on the runner or in your workflow file. Once Node.js 24 becomes the default, you can temporarily opt out by setting ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

### h. 👉Node.js 24のワーニング対策
- 今のうちに一度動かしておいて、動かない要素があるなら潰しておく。
- ymlのjobs:の直前下記の2行を追加して、上記のタグの削除からやり直してみる。

```
env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: 'true'
```

### i. 👉Node.js 24のワーニング対策したWorkflowログ確認

```
Annotations
1 warning
build-and-release
Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, softprops/action-gh-release@v2. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

- エラーはなかったので、ymlは元に戻しておく。

### j. 👉Releases Assets確認
https://github.com/bero-sim/pdetarc-docker-app/releases

```
v1.0.0 Latest
Full Changelog: https://github.com/bero-sim/pdetarc-docker-app/commits/v1.0.0

Assets 4
📦pdetarc-docker-app-source.tar.gz
sha256:de913fb0b8b8eeba6082740e4af75312319e980f16c17e23e3b45035d8357a1f
1.74 MB
📦pdetarc_image_v1.0.0.tar
sha256:29ca6652c707f7d7c38dc35a74cad04c8829b5b24ddf56dec5b684c7e01857ba
993 MB
📄Source code(zip)
📄Source code(tar.gz)
```

---

## ⅱ. 🟥pdetarc-toolsリポジトリ

### a. 👉Create a new repository
1. Repository name: `pdetarc-tools`
2. Description: `決定論的アーカイブ形式PDETARCの解凍専用バイナリ単一アプリ▶入力: <folder>.pdetarc.gz を pdetarc-extract.exe にドラッグ＆ドロップ▶出力: <folder/> へ解凍`
3. 「Create repository」をクリック

### b. 👉pdetarc-toolsのworkflowでエラーが出ないように権限を与える
- Settings/Actions/General/Workflow permissions/に移動
  1. 「Read and write permissions」を選択
  2. 「Allow GitHub Actions to create and approve pull requests」にチェック
  3. 「Save」をクリック

### c. 👉creating a new file；作成し保存（コミット）する
1. https://github.com/bero-sim/pdetarc-tools/blob/main/pdetarc-extract.py
2. https://github.com/bero-sim/pdetarc-tools/blob/main/.github/workflows/build-release.yml
3. https://github.com/bero-sim/pdetarc-tools/blob/main/README.md
4. https://github.com/bero-sim/pdetarc-tools/blob/main/LICENSE.md

### d. 👉Upload files
1. https://github.com/bero-sim/pdetarc-tools/blob/main/PDETARC_EXTRACT.ico
2. https://github.com/bero-sim/pdetarc-tools/blob/main/PDETARC_EXTRACT.icns

### e. 👉タグの削除
1. https://github.com/bero-sim/pdetarc-tools/releases の Releases を全部削除
2. https://github.com/bero-sim/pdetarc-tools/releases の Tags を全部削除

### f. 👉タグv1.0.0をプッシュしてアセット生成

```
PS C:\Users\info\Documents\Git-ws\pdetarc-docker-app> cd C:\Users\info\Documents\Git-ws
PS C:\Users\info\Documents\Git-ws> Remove-Item -Path "pdetarc-tools" -Recurse -Force
PS C:\Users\info\Documents\Git-ws> git clone https://github.com/bero-sim/pdetarc-tools.git
Cloning into 'pdetarc-tools'...
remote: Enumerating objects: 20, done.
remote: Counting objects: 100% (20/20), done.
remote: Compressing objects: 100% (17/17), done.
remote: Total 20 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (20/20), 167.81 KiB | 2.40 MiB/s, done.
Resolving deltas: 100% (4/4), done.
PS C:\Users\info\Documents\Git-ws> cd .\pdetarc-tools\
PS C:\Users\info\Documents\Git-ws\pdetarc-tools> git add .
PS C:\Users\info\Documents\Git-ws\pdetarc-tools> git commit -m "fix workflow"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
PS C:\Users\info\Documents\Git-ws\pdetarc-tools> git push origin main
Everything up-to-date
PS C:\Users\info\Documents\Git-ws\pdetarc-tools> git tag v1.0.0
PS C:\Users\info\Documents\Git-ws\pdetarc-tools> git push origin v1.0.0
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/bero-sim/pdetarc-tools.git
 * [new tag]         v1.0.0 -> v1.0.0
PS C:\Users\info\Documents\Git-ws\pdetarc-tools>
```

### g. 👉Workflowログ確認
https://github.com/bero-sim/pdetarc-tools/actions/runs/25026702968

```
Annotations
4 warnings
build (ubuntu-latest)
Node.js 20 actions are deprecated. The following actions are running on Node.js 20 and may not work as expected: actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4. Actions will be forced to run with Node.js 24 by default starting June 2nd, 2026. Node.js 20 will be removed from the runner on September 16th, 2026. Please check if updated versions of these actions are available that support Node.js 24. To opt into Node.js 24 now, set the FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true environment variable on the runner or in your workflow file. Once Node.js 24 becomes the default, you can temporarily opt out by setting ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
build (macos-latest)
Node.js 20 actions are deprecated. The following actions are running on Node.js 20 and may not work as expected: actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4. Actions will be forced to run with Node.js 24 by default starting June 2nd, 2026. Node.js 20 will be removed from the runner on September 16th, 2026. Please check if updated versions of these actions are available that support Node.js 24. To opt into Node.js 24 now, set the FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true environment variable on the runner or in your workflow file. Once Node.js 24 becomes the default, you can temporarily opt out by setting ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
build (windows-latest)
Node.js 20 actions are deprecated. The following actions are running on Node.js 20 and may not work as expected: actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4. Actions will be forced to run with Node.js 24 by default starting June 2nd, 2026. Node.js 20 will be removed from the runner on September 16th, 2026. Please check if updated versions of these actions are available that support Node.js 24. To opt into Node.js 24 now, set the FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true environment variable on the runner or in your workflow file. Once Node.js 24 becomes the default, you can temporarily opt out by setting ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
release
Node.js 20 actions are deprecated. The following actions are running on Node.js 20 and may not work as expected: actions/checkout@v4, actions/download-artifact@v4, softprops/action-gh-release@v2. Actions will be forced to run with Node.js 24 by default starting June 2nd, 2026. Node.js 20 will be removed from the runner on September 16th, 2026. Please check if updated versions of these actions are available that support Node.js 24. To opt into Node.js 24 now, set the FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true environment variable on the runner or in your workflow file. Once Node.js 24 becomes the default, you can temporarily opt out by setting ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

### h. 👉Node.js 24のワーニング対策
- 今のうちに一度動かしておいて、動かない要素があるなら潰しておく。
- ymlのjobs:の直前下記の2行を追加して、上記のタグの削除からやり直してみる。

```
env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: 'true'
```

### i. 👉Node.js 24のワーニング対策したWorkflowログ確認

```
Annotations
4 warnings
build (ubuntu-latest)
Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
build (macos-latest)
Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
build (windows-latest)
Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
release
Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/download-artifact@v4, softprops/action-gh-release@v2. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

- エラーはなかったので、ymlは元に戻しておく。

---

### j. 👉Releases Assets確認
https://github.com/bero-sim/pdetarc-tools/releases

```
v1.0.0 Pre-release
Full Changelog: https://github.com/bero-sim/pdetarc-tools/commits/v1.0.0

Assets 8
📦bundle.toml
sha256:7043911cf076a3434cbd5e8ca51fa49c3df564bb2429d83944655839a570e1c6
1.78 KB
📦pdetarc-docker-app-source.tar.gz
sha256:de913fb0b8b8eeba6082740e4af75312319e980f16c17e23e3b45035d8357a1f
1.74 MB
📦pdetarc-extract-macos-latest.zip
sha256:9e6731e1495a10d9e25a436749343d779d5b9a235edee4fe81046fe5e0901e6b
6.87 MB
📦pdetarc-extract-ubuntu-latest.zip
sha256:57535966cab9f65021aef0d339bbea6e7362515d56aa9fd4e85862520324b167
18.8 MB
📦pdetarc-extract-windows-latest.zip
sha256:e5ea59335de5f774feb6ff7ea17fdc01bd1736acf40efe0948ede4bffbdbf181
7.7 MB
📦pdetarc-tools-source.tar.gz
sha256:d7b31ceee07b7a44fadb03fe3de0800b3602e5734bd6a37b52578453ad8bf8d8
163 KB
📄Source code
(zip)
📄Source code
(tar.gz)
```

---

# 2. 🟫検証用の圧縮対象フォルダ作成

## ⅰ. 🟥検証用フォルダ作成・公開

### a. 👉test_data.tar.gz の作成・アップロード
1. bundle.tomlを [入手](https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/bundle.toml) して `test_data\archive\portable-deterministic-archive-v1` フォルダの中に入れる。
2. test_dataフォルダの中身は下記の通り。
```
PS C:\Users\info> cd C:\workspace\
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/04/28     12:03                test_data


PS C:\workspace> Get-ChildItem -Path "test_data" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data\archive
C:\workspace\test_data\archive\png
C:\workspace\test_data\archive\portable-deterministic-archive-v1
C:\workspace\test_data\archive\test.html
C:\workspace\test_data\archive\png\pdetarc_concepts.png
C:\workspace\test_data\archive\portable-deterministic-archive-v1\README.pdf


PS C:\workspace> wget -O .\test_data\archive\portable-deterministic-archive-v1\bundle.toml https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/bundle.toml
PS C:\workspace> Get-ChildItem -Path "test_data" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data\archive
C:\workspace\test_data\archive\png
C:\workspace\test_data\archive\portable-deterministic-archive-v1
C:\workspace\test_data\archive\test.html
C:\workspace\test_data\archive\png\pdetarc_concepts.png
C:\workspace\test_data\archive\portable-deterministic-archive-v1\bundle.toml
C:\workspace\test_data\archive\portable-deterministic-archive-v1\README.pdf


PS C:\workspace> (Get-FileHash "C:\workspace\test_data\archive\portable-deterministic-archive-v1\bundle.toml" -Algorithm SHA256).Hash.ToLower()
7043911cf076a3434cbd5e8ca51fa49c3df564bb2429d83944655839a570e1c6
PS C:\workspace>
```
3. test_dataをtest_data.tar.gzに圧縮
```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/04/28     12:03                test_data


PS C:\workspace> tar -czvf test_data.tar.gz test_data
a test_data
a test_data/archive
a test_data/archive/png
a test_data/archive/portable-deterministic-archive-v1
a test_data/archive/test.html
a test_data/archive/portable-deterministic-archive-v1/bundle.toml
a test_data/archive/portable-deterministic-archive-v1/README.pdf
a test_data/archive/png/pdetarc_concepts.png
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/04/28     12:03                test_data
-a----        2026/04/28     13:05        4336691 test_data.tar.gz


PS C:\workspace> (Get-FileHash "test_data.tar.gz" -Algorithm SHA256).Hash.ToLower()
83ec57fcecc26b237c20f962aa760eb04b2bfb4a48df582e92c04ceea46466eb
PS C:\workspace> tar -tzvf .\test_data.tar.gz
drwxrwxrwx  0 0      0           0 4 28 12:03 test_data/
drwxrwxrwx  0 0      0           0 4 28 12:32 test_data/archive/
drwxrwxrwx  0 0      0           0 4 27 17:12 test_data/archive/png/
drwxrwxrwx  0 0      0           0 4 28 13:00 test_data/archive/portable-deterministic-archive-v1/
-rw-rw-rw-  0 0      0       40529 4 28 12:32 test_data/archive/test.html
-rw-rw-rw-  0 0      0        1823 4 28 13:00 test_data/archive/portable-deterministic-archive-v1/bundle.toml
-rw-rw-rw-  0 0      0     2738412 4 28 12:20 test_data/archive/portable-deterministic-archive-v1/README.pdf
-rw-rw-rw-  0 0      0     1893180 1 01  2000 test_data/archive/png/pdetarc_concepts.png
PS C:\workspace>
```

4. test_data.tar.gzをpdetarc-toolsリポジトリのv1.0.0 Assetsの添付書類として追加。
  1. 「Edit v1.0.0」をクリック。
  2. 「Attach binaries by dropping them here or selecting them.」をクリック
　3. `C:\workspace\test_data\test_data.tar.gz` を選択して「開く」をクリック
  4. 「test_data.tar.gz (4.14 MB)」が追加されたら「Update release」をクリック

### b. 👉Releases Assets確認

```
v1.0.0 Pre-release
@github-actions github-actions released this 3 hours ago
 v1.0.0
 ebca8f2 
Full Changelog: https://github.com/bero-sim/pdetarc-tools/commits/v1.0.0

Assets 9
📦bundle.toml
sha256:7043911cf076a3434cbd5e8ca51fa49c3df564bb2429d83944655839a570e1c6
1.78 KB
📦pdetarc-docker-app-source.tar.gz
sha256:de913fb0b8b8eeba6082740e4af75312319e980f16c17e23e3b45035d8357a1f
1.74 MB
📦pdetarc-extract-macos-latest.zip
sha256:9e6731e1495a10d9e25a436749343d779d5b9a235edee4fe81046fe5e0901e6b
6.87 MB
📦pdetarc-extract-ubuntu-latest.zip
sha256:57535966cab9f65021aef0d339bbea6e7362515d56aa9fd4e85862520324b167
18.8 MB
📦pdetarc-extract-windows-latest.zip
sha256:e5ea59335de5f774feb6ff7ea17fdc01bd1736acf40efe0948ede4bffbdbf181
7.7 MB
📦pdetarc-tools-source.tar.gz
sha256:d7b31ceee07b7a44fadb03fe3de0800b3602e5734bd6a37b52578453ad8bf8d8
163 KB
📦test_data.tar.gz
sha256:83ec57fcecc26b237c20f962aa760eb04b2bfb4a48df582e92c04ceea46466eb
4.14 MB
📄Source code(zip)
📄Source code(tar.gz)
```

---

## ⅱ. 🟥検証用フォルダのダウンロード・展開

### a. 👉test_data.tar.gzをリポジトリよりダウンロード・解凍してtest_dataフォルダを作成

```
S C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/04/28     12:03                test_data
-a----        2026/04/28     13:05        4336691 test_data.tar.gz


PS C:\workspace> rm .\test_data.tar.gz
PS C:\workspace> Remove-Item -Path "test_data" -Recurse -Force
PS C:\workspace> ls
PS C:\workspace> wget -O test_data.tar.gz https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/test_data.tar.gz
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        2026/04/28     13:21        4336691 test_data.tar.gz


PS C:\workspace> (Get-FileHash "test_data.tar.gz" -Algorithm SHA256).Hash.ToLower()
83ec57fcecc26b237c20f962aa760eb04b2bfb4a48df582e92c04ceea46466eb
PS C:\workspace> tar -xzvf .\test_data.tar.gz
x test_data/
x test_data/archive/
x test_data/archive/png/
x test_data/archive/portable-deterministic-archive-v1/
x test_data/archive/test.html
x test_data/archive/portable-deterministic-archive-v1/bundle.toml
x test_data/archive/portable-deterministic-archive-v1/README.pdf
x test_data/archive/png/pdetarc_concepts.png
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/04/28     12:03                test_data
-a----        2026/04/28     13:21        4336691 test_data.tar.gz


PS C:\workspace> Get-ChildItem -Path "test_data" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data\archive
C:\workspace\test_data\archive\png
C:\workspace\test_data\archive\portable-deterministic-archive-v1
C:\workspace\test_data\archive\test.html
C:\workspace\test_data\archive\png\pdetarc_concepts.png
C:\workspace\test_data\archive\portable-deterministic-archive-v1\bundle.toml
C:\workspace\test_data\archive\portable-deterministic-archive-v1\README.pdf


PS C:\workspace> rm .\test_data.tar.gz
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/04/28     12:03                test_data


PS C:\workspace>
```

---

# 3. 🟫動作検証

## ⅰ. 🟥生成ツールのdockerビルド

### a. 👉pdetarc-docker-appのソースファイルをリポジトリよりダウンロードして解凍

```
PS C:\workspace> wget -O pdetarc-docker-app-source.tar.gz https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-docker-app-source.tar.gz
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/04/28     12:03                test_data
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz


PS C:\workspace> (Get-FileHash "pdetarc-docker-app-source.tar.gz" -Algorithm SHA256).Hash.ToLower()
de913fb0b8b8eeba6082740e4af75312319e980f16c17e23e3b45035d8357a1f
PS C:\workspace> tar -xzvf .\pdetarc-docker-app-source.tar.gz
x ./
x ./.github/
x ./.github/workflows/
x ./.github/workflows/release-assets.yml
x ./Dockerfile
x ./LICENSE.md
x ./README.md
x ./pdetarc.bat
x ./pdetarc.py
x ./pdetarc_concepts.png
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     12:03                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace>
```

### b. 👉Docker起動

### c. 👉Docker版pythonのハッシュ値確認

```
PS C:\workspace> docker pull python:3.12.3
3.12.3: Pulling from library/python
Digest: sha256:3966b81808d864099f802080d897cef36c01550472ab3955fdd716d1c665acd6
Status: Downloaded newer image for python:3.12.3
docker.io/library/python:3.12.3
PS C:\workspace>
```

### d. 👉Dockerビルド実行

```
PS C:\workspace> docker build -t pdetarc .
[+] Building 2.1s (9/9) FINISHED                                                                   docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                               0.0s
 => => transferring dockerfile: 1.24kB                                                                             0.0s
 => [internal] load metadata for docker.io/library/python@sha256:3966b81808d864099f802080d897cef36c01550472ab3955  1.4s
 => [auth] library/python:pull token for registry-1.docker.io                                                      0.0s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [1/3] FROM docker.io/library/python@sha256:3966b81808d864099f802080d897cef36c01550472ab3955fdd716d1c665acd6    0.0s
 => => resolve docker.io/library/python@sha256:3966b81808d864099f802080d897cef36c01550472ab3955fdd716d1c665acd6    0.0s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 10.45kB                                                                               0.0s
 => CACHED [2/3] WORKDIR /work                                                                                     0.0s
 => [3/3] COPY pdetarc.py /app/                                                                                    0.0s
 => exporting to image                                                                                             0.3s
 => => exporting layers                                                                                            0.1s
 => => exporting manifest sha256:f23d60b989672b0da1abd6998ceb8f867e4bcc7ead7b73f3ee9c91336ccf3482                  0.0s
 => => exporting config sha256:7741ef93809bc3c44f4ca0d2aa1304e1d8df57359264b12ad7cde527a4cdd3b4                    0.0s
 => => exporting attestation manifest sha256:f9de608847e137b41ffe1a7306ecda19cf3a72086af5f84885f941cdbe15d959      0.0s
 => => exporting manifest list sha256:17ac47418ced7a1667fa699c4b9ddb8caae99de68a72bb8a19d53542bf93b4c5             0.0s
 => => naming to docker.io/library/pdetarc:latest                                                                  0.0s
 => => unpacking to docker.io/library/pdetarc:latest                                                               0.1s
PS C:\workspace>
```

---

## ⅱ. 🟥Dockerビルドベースの動作検証

### a. 👉動作検証前の状況確認

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     12:03                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace> Get-ChildItem -Path "test_data" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data\archive
C:\workspace\test_data\archive\png
C:\workspace\test_data\archive\portable-deterministic-archive-v1
C:\workspace\test_data\archive\test.html
C:\workspace\test_data\archive\png\pdetarc_concepts.png
C:\workspace\test_data\archive\portable-deterministic-archive-v1\bundle.toml
C:\workspace\test_data\archive\portable-deterministic-archive-v1\README.pdf


PS C:\workspace> cat .\test_data\archive\portable-deterministic-archive-v1\bundle.toml

[[bundle]]
name = "pdetarc-extract-macos-latest.zip"
file = "pdetarc-extract-macos-latest.zip"
url = "https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-macos-latest.zip"
sha256 = "9e6731e1495a10d9e25a436749343d779d5b9a235edee4fe81046fe5e0901e6b"
source = "github-releases"

[[bundle]]
name = "pdetarc-extract-ubuntu-latest.zip"
file = "pdetarc-extract-ubuntu-latest.zip"
url = "https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-ubuntu-latest.zip"
sha256 = "57535966cab9f65021aef0d339bbea6e7362515d56aa9fd4e85862520324b167"
source = "github-releases"

[[bundle]]
name = "pdetarc-extract-windows-latest.zip"
file = "pdetarc-extract-windows-latest.zip"
url = "https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-windows-latest.zip"
sha256 = "e5ea59335de5f774feb6ff7ea17fdc01bd1736acf40efe0948ede4bffbdbf181"
source = "github-releases"

[[bundle]]
name = "pdetarc_image_v1.0.0.tar"
file = "pdetarc_image_v1.0.0.tar"
url = "https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc_image_v1.0.0.tar"
sha256 = "29ca6652c707f7d7c38dc35a74cad04c8829b5b24ddf56dec5b684c7e01857ba"
source = "github-releases"

[[bundle]]
name = "pdetarc-docker-app-source.tar.gz"
file = "pdetarc-docker-app-source.tar.gz"
url = "https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc-docker-app-source.tar.gz"
sha256 = "de913fb0b8b8eeba6082740e4af75312319e980f16c17e23e3b45035d8357a1f"
source = "github-releases"

[[bundle]]
name = "pdetarc-tools-source.tar.gz"
file = "pdetarc-tools-source.tar.gz"
url = "https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-tools-source.tar.gz"
sha256 = "d7b31ceee07b7a44fadb03fe3de0800b3602e5734bd6a37b52578453ad8bf8d8"
source = "github-releases"

PS C:\workspace>
```

### b. 👉test_dataフォルダをpdetarc.batにD&D

- **「開いているファイル - セキュリティ警告」→「実行」をクリック**

```
==== PDETARC DOCKER DROPLET START ====
Input: C:\workspace\test_data
Dir  : C:\workspace
Name : test_data
Running Docker...
[2026-04-28 05:15:34 UTC] ==== PDETARC START ====
[2026-04-28 05:15:34 UTC] モード: 圧縮
[2026-04-28 05:15:34 UTC] 入力: /work/test_data
[2026-04-28 05:15:34 UTC] [DL] https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-macos-latest.zip
[2026-04-28 05:15:35 UTC] [DL] https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-ubuntu-latest.zip
[2026-04-28 05:15:38 UTC] [DL] https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-windows-latest.zip
[2026-04-28 05:15:40 UTC] [DL] https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc_image_v1.0.0.tar
[2026-04-28 05:18:44 UTC] [DL] https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc-docker-app-source.tar.gz
[2026-04-28 05:18:45 UTC] [DL] https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-tools-source.tar.gz
[2026-04-28 05:24:38 UTC] 完了: /work/test_data.pdetarc.gz
[2026-04-28 05:24:38 UTC] ==== PDETARC END ====

==== RETURN CODE: 0 ====
==== PDETARC DOCKER DROPLET END ====
続行するには何かキーを押してください . . .
```

### c. 👉圧縮ツールの時間表示は標準時のUTCで表示のため9時間遅い

### d. 👉圧縮結果確認

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     14:19                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2026/04/28     14:24           1042 pdetarc.log
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     14:24      822579872 test_data.pdetarc.gz


PS C:\workspace> cat .\pdetarc.log
[2026-04-28 05:15:34 UTC] ==== PDETARC START ====
[2026-04-28 05:15:34 UTC] モード: 圧縮
[2026-04-28 05:15:34 UTC] 入力: /work/test_data
[2026-04-28 05:15:34 UTC] [DL] https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-macos-latest.zip
[2026-04-28 05:15:35 UTC] [DL] https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-ubuntu-latest.zip
[2026-04-28 05:15:38 UTC] [DL] https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-windows-latest.zip
[2026-04-28 05:15:40 UTC] [DL] https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc_image_v1.0.0.tar
[2026-04-28 05:18:44 UTC] [DL] https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc-docker-app-source.tar.gz
[2026-04-28 05:18:45 UTC] [DL] https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-tools-source.tar.gz
[2026-04-28 05:24:38 UTC] 完了: /work/test_data.pdetarc.gz
[2026-04-28 05:24:38 UTC] ==== PDETARC END ====
PS C:\workspace> Get-ChildItem -Path "test_data" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data\archive
C:\workspace\test_data\backup
C:\workspace\test_data\bundle-hash.json
C:\workspace\test_data\manifest.json
C:\workspace\test_data\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\pdetarc-extract-linux
C:\workspace\test_data\pdetarc-extract-mac
C:\workspace\test_data\pdetarc-extract-windows.exe
C:\workspace\test_data\pdetarc-tools-source.tar.gz
C:\workspace\test_data\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\README.pdf
C:\workspace\test_data\archive\png
C:\workspace\test_data\archive\portable-deterministic-archive-v1
C:\workspace\test_data\archive\test.html
C:\workspace\test_data\archive\png\pdetarc_concepts.png
C:\workspace\test_data\archive\portable-deterministic-archive-v1\bundle.toml
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-macos-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-ubuntu-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-windows-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-tools-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\archive\portable-deterministic-archive-v1\README.pdf


PS C:\workspace> cat .\test_data\bundle-hash.json
[
  {
    "extracted": [
      "pdetarc-extract-mac"
    ],
    "file": "pdetarc-extract-macos-latest.zip",
    "name": "pdetarc-extract-macos-latest.zip",
    "sha256": "9e6731e1495a10d9e25a436749343d779d5b9a235edee4fe81046fe5e0901e6b",
    "source": "github-releases",
    "url": "https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-macos-latest.zip"
  },
  {
    "extracted": [
      "pdetarc-extract-linux"
    ],
    "file": "pdetarc-extract-ubuntu-latest.zip",
    "name": "pdetarc-extract-ubuntu-latest.zip",
    "sha256": "57535966cab9f65021aef0d339bbea6e7362515d56aa9fd4e85862520324b167",
    "source": "github-releases",
    "url": "https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-ubuntu-latest.zip"
  },
  {
    "extracted": [
      "pdetarc-extract-windows.exe"
    ],
    "file": "pdetarc-extract-windows-latest.zip",
    "name": "pdetarc-extract-windows-latest.zip",
    "sha256": "e5ea59335de5f774feb6ff7ea17fdc01bd1736acf40efe0948ede4bffbdbf181",
    "source": "github-releases",
    "url": "https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-windows-latest.zip"
  },
  {
    "extracted": [
      "pdetarc_image_v1.0.0.tar"
    ],
    "file": "pdetarc_image_v1.0.0.tar",
    "name": "pdetarc_image_v1.0.0.tar",
    "sha256": "29ca6652c707f7d7c38dc35a74cad04c8829b5b24ddf56dec5b684c7e01857ba",
    "source": "github-releases",
    "url": "https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc_image_v1.0.0.tar"
  },
  {
    "extracted": [
      "pdetarc-docker-app-source.tar.gz"
    ],
    "file": "pdetarc-docker-app-source.tar.gz",
    "name": "pdetarc-docker-app-source.tar.gz",
    "sha256": "de913fb0b8b8eeba6082740e4af75312319e980f16c17e23e3b45035d8357a1f",
    "source": "github-releases",
    "url": "https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc-docker-app-source.tar.gz"
  },
  {
    "extracted": [
      "pdetarc-tools-source.tar.gz"
    ],
    "file": "pdetarc-tools-source.tar.gz",
    "name": "pdetarc-tools-source.tar.gz",
    "sha256": "d7b31ceee07b7a44fadb03fe3de0800b3602e5734bd6a37b52578453ad8bf8d8",
    "source": "github-releases",
    "url": "https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-tools-source.tar.gz"
  }
]
PS C:\workspace> cat .\test_data\manifest.json
{
  "build": "2000-01-01-00-00-00",
  "files": [
    {
      "id": "00000001",
      "path": "archive/png/pdetarc_concepts.png",
      "sha256": "5a2ec0cf8819534a95e2db2a80fb20f0e74c820ba190f50054919d78bef1962e",
      "size": 1893180
    },
    {
      "id": "00000002",
      "path": "archive/portable-deterministic-archive-v1/README.pdf",
      "sha256": "95c3abb634587eea34882cf8d9b5b1732277d9f61329c45019703d59b6266d56",
      "size": 2738412
    },
    {
      "id": "00000003",
      "path": "archive/portable-deterministic-archive-v1/bundle.toml",
      "sha256": "7043911cf076a3434cbd5e8ca51fa49c3df564bb2429d83944655839a570e1c6",
      "size": 1823
    },
    {
      "id": "00000004",
      "path": "archive/portable-deterministic-archive-v1/pdetarc-docker-app-source.tar.gz",
      "sha256": "de913fb0b8b8eeba6082740e4af75312319e980f16c17e23e3b45035d8357a1f",
      "size": 1827674
    },
    {
      "id": "00000005",
      "path": "archive/portable-deterministic-archive-v1/pdetarc-extract-macos-latest.zip",
      "sha256": "9e6731e1495a10d9e25a436749343d779d5b9a235edee4fe81046fe5e0901e6b",
      "size": 7201332
    },
    {
      "id": "00000006",
      "path": "archive/portable-deterministic-archive-v1/pdetarc-extract-ubuntu-latest.zip",
      "sha256": "57535966cab9f65021aef0d339bbea6e7362515d56aa9fd4e85862520324b167",
      "size": 19671993
    },
    {
      "id": "00000007",
      "path": "archive/portable-deterministic-archive-v1/pdetarc-extract-windows-latest.zip",
      "sha256": "e5ea59335de5f774feb6ff7ea17fdc01bd1736acf40efe0948ede4bffbdbf181",
      "size": 8072575
    },
    {
      "id": "00000008",
      "path": "archive/portable-deterministic-archive-v1/pdetarc-tools-source.tar.gz",
      "sha256": "d7b31ceee07b7a44fadb03fe3de0800b3602e5734bd6a37b52578453ad8bf8d8",
      "size": 167143
    },
    {
      "id": "00000009",
      "path": "archive/portable-deterministic-archive-v1/pdetarc_image_v1.0.0.tar",
      "sha256": "29ca6652c707f7d7c38dc35a74cad04c8829b5b24ddf56dec5b684c7e01857ba",
      "size": 1041643520
    },
    {
      "id": "00000010",
      "path": "archive/test.html",
      "sha256": "e3ffec2f554fe8cd0e298e22a4482b000175b75e8a15927064354aa1861ab1f3",
      "size": 40529
    }
  ],
  "format": "portable-deterministic-archive-v1",
  "tool_version": "PDETARC_1.0.0"
}
PS C:\workspace> tar -tzvf .\test_data.pdetarc.gz
-rw-r--r--  0 0      0     1893180 1 01  2000 files/00000001
-rw-r--r--  0 0      0     2738412 1 01  2000 files/00000002
-rw-r--r--  0 0      0        1823 1 01  2000 files/00000003
-rw-r--r--  0 0      0     1827674 1 01  2000 files/00000004
-rw-r--r--  0 0      0     7201332 1 01  2000 files/00000005
-rw-r--r--  0 0      0    19671993 1 01  2000 files/00000006
-rw-r--r--  0 0      0     8072575 1 01  2000 files/00000007
-rw-r--r--  0 0      0      167143 1 01  2000 files/00000008
-rw-r--r--  0 0      0  1041643520 1 01  2000 files/00000009
-rw-r--r--  0 0      0       40529 1 01  2000 files/00000010
-rw-r--r--  0 0      0     2738412 1 01  2000 README.pdf
-rw-r--r--  0 0      0        2340 1 01  2000 bundle-hash.json
-rw-r--r--  0 0      0        2333 1 01  2000 manifest.json
-rw-r--r--  0 0      0     1827674 1 01  2000 pdetarc-docker-app-source.tar.gz
-rw-r--r--  0 0      0    19855536 1 01  2000 pdetarc-extract-linux
-rw-r--r--  0 0      0     7349360 1 01  2000 pdetarc-extract-mac
-rw-r--r--  0 0      0     8267545 1 01  2000 pdetarc-extract-windows.exe
-rw-r--r--  0 0      0      167143 1 01  2000 pdetarc-tools-source.tar.gz
-rw-r--r--  0 0      0  1041643520 1 01  2000 pdetarc_image_v1.0.0.tar
PS C:\workspace> (Get-FileHash "test_data.pdetarc.gz" -Algorithm SHA256).Hash.ToLower()
5e127d9ceeef0ee0d9269be5fa4e721bc809f11f595b22b957989d36d9a79bba
PS C:\workspace> Remove-Item -Path "test_data" -Recurse -Force
PS C:\workspace> rm .\pdetarc.log
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     14:24      822579872 test_data.pdetarc.gz


PS C:\workspace>
```

### e. 👉test_data.pdetarc.gzをpdetarc.batにD&D
- **「開いているファイル - セキュリティ警告」→「実行」をクリック**

```
==== PDETARC DOCKER DROPLET START ====
Input: C:\workspace\test_data.pdetarc.gz
Dir  : C:\workspace
Name : test_data.pdetarc.gz
Running Docker...
[2026-04-28 05:38:55 UTC] ==== PDETARC START ====
[2026-04-28 05:38:55 UTC] モード: 圧縮
[2026-04-28 05:38:55 UTC] 入力: /work/test_data.pdetarc.gz
[2026-04-28 05:38:55 UTC] ERROR: archive folder not found

==== RETURN CODE: 1 ====
==== PDETARC DOCKER DROPLET END ====
続行するには何かキーを押してください . . .
```

### f. 👉圧縮専用だからエラー（正常動作）

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2026/04/28     14:38            216 pdetarc.log
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     14:24      822579872 test_data.pdetarc.gz


PS C:\workspace> cat .\pdetarc.log
[2026-04-28 05:38:55 UTC] ==== PDETARC START ====
[2026-04-28 05:38:55 UTC] モード: 圧縮
[2026-04-28 05:38:55 UTC] 入力: /work/test_data.pdetarc.gz
[2026-04-28 05:38:55 UTC] ERROR: archive folder not found
PS C:\workspace> rm .\pdetarc.log
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     14:24      822579872 test_data.pdetarc.gz


PS C:\workspace>
```

### g. 👉test_data.pdetarc.gzからpdetarc-extract-windows.exeを取り出す。

```
PS C:\workspace> tar -zxvf test_data.pdetarc.gz pdetarc-extract-windows.exe
x pdetarc-extract-windows.exe
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     14:24      822579872 test_data.pdetarc.gz


PS C:\workspace>
```

### h. 👉test_data.pdetarc.gzをpdetarc-extract-windows.exeにD&D

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     14:49                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2026/04/28     14:49            383 pdetarc-extract.log
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     14:24      822579872 test_data.pdetarc.gz


PS C:\workspace> cat .\pdetarc-extract.log
[2026-04-28 14:49:06] ==== PDETARC EXTRACT START ====
[2026-04-28 14:49:06] モード: 解凍
[2026-04-28 14:49:06] 入力: C:\workspace\test_data.pdetarc.gz
[2026-04-28 14:49:06] 出力: C:\workspace\test_data
[2026-04-28 14:49:25] 検証結果: OK（完全一致）
[2026-04-28 14:49:25] 完了: C:\workspace\test_data
[2026-04-28 14:49:25] ==== PDETARC EXTRACT END ====
PS C:\workspace> Get-ChildItem -Path "test_data" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data\archive
C:\workspace\test_data\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\pdetarc-extract-linux
C:\workspace\test_data\pdetarc-extract-mac
C:\workspace\test_data\pdetarc-extract-windows.exe
C:\workspace\test_data\pdetarc-tools-source.tar.gz
C:\workspace\test_data\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\README.pdf
C:\workspace\test_data\archive\png
C:\workspace\test_data\archive\portable-deterministic-archive-v1
C:\workspace\test_data\archive\test.html
C:\workspace\test_data\archive\png\pdetarc_concepts.png
C:\workspace\test_data\archive\portable-deterministic-archive-v1\bundle.toml
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-macos-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-ubuntu-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-windows-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-tools-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\archive\portable-deterministic-archive-v1\README.pdf


PS C:\workspace> rm .\test_data.pdetarc.gz
PS C:\workspace> rm .\pdetarc-extract.log
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     14:49                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace>
```

### i. 👉test_dataを揺さぶってみる（ZIP圧縮・解凍）

```
PS C:\workspace> powershell Compress-Archive -Path "C:\workspace\test_data\*" -DestinationPath "C:\workspace\test.zip"
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     14:49                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     15:07      827119699 test.zip


PS C:\workspace> Remove-Item -Path "test_data" -Recurse -Force
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     15:07      827119699 test.zip


PS C:\workspace> powershell Expand-Archive -Path "C:\workspace\test.zip" -DestinationPath "C:\workspace\test_data\"
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:08                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     15:07      827119699 test.zip


PS C:\workspace> Get-ChildItem -Path "test_data" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data\archive
C:\workspace\test_data\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\pdetarc-extract-linux
C:\workspace\test_data\pdetarc-extract-mac
C:\workspace\test_data\pdetarc-extract-windows.exe
C:\workspace\test_data\pdetarc-tools-source.tar.gz
C:\workspace\test_data\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\README.pdf
C:\workspace\test_data\archive\png
C:\workspace\test_data\archive\portable-deterministic-archive-v1
C:\workspace\test_data\archive\test.html
C:\workspace\test_data\archive\png\pdetarc_concepts.png
C:\workspace\test_data\archive\portable-deterministic-archive-v1\bundle.toml
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-macos-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-ubuntu-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-windows-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-tools-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\archive\portable-deterministic-archive-v1\README.pdf


PS C:\workspace> rm .\test.zip
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:08                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace>
```

### j. 👉揺さぶったtest_dataフォルダをpdetarc-extract-windows.exeにD&D

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:08                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2026/04/28     15:10            134 pdetarc-extract.log
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace> cat .\pdetarc-extract.log
[2026-04-28 15:10:42] ERROR: 解凍非対象のフォルダです (有効な中間フォルダではありません) -> test_data
PS C:\workspace> rm .\pdetarc-extract.log
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:08                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace>
```

### k. 👉解凍できないためエラー（正常動作）

### l. 👉test_dataフォルダをpdetarc.batにD&D

```
==== PDETARC DOCKER DROPLET START ====
Input: C:\workspace\test_data
Dir  : C:\workspace
Name : test_data
Running Docker...
[2026-04-28 06:23:05 UTC] ==== PDETARC START ====
[2026-04-28 06:23:05 UTC] モード: 圧縮
[2026-04-28 06:23:05 UTC] 入力: /work/test_data
[2026-04-28 06:29:24 UTC] 完了: /work/test_data.pdetarc.gz
[2026-04-28 06:29:24 UTC] ==== PDETARC END ====

==== RETURN CODE: 0 ====
==== PDETARC DOCKER DROPLET END ====
続行するには何かキーを押してください . . .
```

### m. 👉bashで状況確認

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:23                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2026/04/28     15:29            256 pdetarc.log
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     15:29      822579872 test_data.pdetarc.gz


PS C:\workspace> cat .\pdetarc.log
[2026-04-28 06:23:05 UTC] ==== PDETARC START ====
[2026-04-28 06:23:05 UTC] モード: 圧縮
[2026-04-28 06:23:05 UTC] 入力: /work/test_data
[2026-04-28 06:29:24 UTC] 完了: /work/test_data.pdetarc.gz
[2026-04-28 06:29:24 UTC] ==== PDETARC END ====
PS C:\workspace> (Get-FileHash "test_data.pdetarc.gz" -Algorithm SHA256).Hash.ToLower()
5e127d9ceeef0ee0d9269be5fa4e721bc809f11f595b22b957989d36d9a79bba
PS C:\workspace> Remove-Item -Path "test_data" -Recurse -Force
PS C:\workspace> rm .\pdetarc.log
PS C:\workspace>
```

### n. 👉test_dataフォルダを揺さぶっても同じハッシュ値再現した。

### o. 👉test_data.pdetarc.gzを右クリックですべて展開する。

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:37                test_data.pdetarc
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     15:29      822579872 test_data.pdetarc.gz


PS C:\workspace> Get-ChildItem -Path "test_data.pdetarc" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data.pdetarc\files
C:\workspace\test_data.pdetarc\bundle-hash.json
C:\workspace\test_data.pdetarc\manifest.json
C:\workspace\test_data.pdetarc\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data.pdetarc\pdetarc-extract-linux
C:\workspace\test_data.pdetarc\pdetarc-extract-mac
C:\workspace\test_data.pdetarc\pdetarc-extract-windows.exe
C:\workspace\test_data.pdetarc\pdetarc-tools-source.tar.gz
C:\workspace\test_data.pdetarc\pdetarc_image_v1.0.0.tar
C:\workspace\test_data.pdetarc\README.pdf
C:\workspace\test_data.pdetarc\files\00000001
C:\workspace\test_data.pdetarc\files\00000002
C:\workspace\test_data.pdetarc\files\00000003
C:\workspace\test_data.pdetarc\files\00000004
C:\workspace\test_data.pdetarc\files\00000005
C:\workspace\test_data.pdetarc\files\00000006
C:\workspace\test_data.pdetarc\files\00000007
C:\workspace\test_data.pdetarc\files\00000008
C:\workspace\test_data.pdetarc\files\00000009
C:\workspace\test_data.pdetarc\files\00000010


PS C:\workspace> rm .\test_data.pdetarc.gz
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:37                test_data.pdetarc
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace>
```

### p. 👉test_data.pdetarcをpdetarc.batにD&Dする。

```
==== PDETARC DOCKER DROPLET START ====
Input: C:\workspace\test_data.pdetarc
Dir  : C:\workspace
Name : test_data.pdetarc
Running Docker...
[2026-04-28 06:43:23 UTC] ==== PDETARC START ====
[2026-04-28 06:43:23 UTC] モード: 圧縮
[2026-04-28 06:43:23 UTC] 入力: /work/test_data.pdetarc
[2026-04-28 06:43:23 UTC] ERROR: archive folder not found

==== RETURN CODE: 1 ====
==== PDETARC DOCKER DROPLET END ====
続行するには何かキーを押してください . . .
```

### q. 👉bash確認

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:37                test_data.pdetarc
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2026/04/28     15:43            213 pdetarc.log
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace> cat .\pdetarc.log
[2026-04-28 06:43:23 UTC] ==== PDETARC START ====
[2026-04-28 06:43:23 UTC] モード: 圧縮
[2026-04-28 06:43:23 UTC] 入力: /work/test_data.pdetarc
[2026-04-28 06:43:23 UTC] ERROR: archive folder not found
PS C:\workspace> rm .\pdetarc.log
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:37                test_data.pdetarc
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace>
```

### r. 👉.pdetarcは圧縮対象ではないためエラー（正常動作）

### s. 👉test_data.pdetarcをpdetarc-extract-windows.exeにD&Dする。

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:47                test_data
d-----        2026/04/28     15:37                test_data.pdetarc
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2026/04/28     15:47            380 pdetarc-extract.log
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace> cat .\pdetarc-extract.log
[2026-04-28 15:47:43] ==== PDETARC EXTRACT START ====
[2026-04-28 15:47:43] モード: 解凍
[2026-04-28 15:47:43] 入力: C:\workspace\test_data.pdetarc
[2026-04-28 15:47:43] 出力: C:\workspace\test_data
[2026-04-28 15:47:46] 検証結果: OK（完全一致）
[2026-04-28 15:47:46] 完了: C:\workspace\test_data
[2026-04-28 15:47:46] ==== PDETARC EXTRACT END ====
PS C:\workspace> Get-ChildItem -Path "test_data" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data\archive
C:\workspace\test_data\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\pdetarc-extract-linux
C:\workspace\test_data\pdetarc-extract-mac
C:\workspace\test_data\pdetarc-extract-windows.exe
C:\workspace\test_data\pdetarc-tools-source.tar.gz
C:\workspace\test_data\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\README.pdf
C:\workspace\test_data\archive\png
C:\workspace\test_data\archive\portable-deterministic-archive-v1
C:\workspace\test_data\archive\test.html
C:\workspace\test_data\archive\png\pdetarc_concepts.png
C:\workspace\test_data\archive\portable-deterministic-archive-v1\bundle.toml
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-macos-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-ubuntu-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-windows-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-tools-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\archive\portable-deterministic-archive-v1\README.pdf


PS C:\workspace> Remove-Item -Path "test_data.pdetarc" -Recurse -Force
PS C:\workspace> rm .\pdetarc-extract.log
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     15:47                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace>
```

### t. 👉test_data.pdetarcの中間状態から解凍したtest_dataをpdetarc.batにD&Dする。

```
==== PDETARC DOCKER DROPLET START ====
Input: C:\workspace\test_data
Dir  : C:\workspace
Name : test_data
Running Docker...
[2026-04-28 07:08:09 UTC] ==== PDETARC START ====
[2026-04-28 07:08:09 UTC] モード: 圧縮
[2026-04-28 07:08:09 UTC] 入力: /work/test_data
[2026-04-28 07:14:28 UTC] 完了: /work/test_data.pdetarc.gz
[2026-04-28 07:14:28 UTC] ==== PDETARC END ====

==== RETURN CODE: 0 ====
==== PDETARC DOCKER DROPLET END ====
続行するには何かキーを押してください . . .
```

### u. 👉bashで状況確認

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     16:08                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2026/04/28     16:14            256 pdetarc.log
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     16:14      822579872 test_data.pdetarc.gz


PS C:\workspace> cat .\pdetarc.log
[2026-04-28 07:08:09 UTC] ==== PDETARC START ====
[2026-04-28 07:08:09 UTC] モード: 圧縮
[2026-04-28 07:08:09 UTC] 入力: /work/test_data
[2026-04-28 07:14:28 UTC] 完了: /work/test_data.pdetarc.gz
[2026-04-28 07:14:28 UTC] ==== PDETARC END ====
PS C:\workspace> (Get-FileHash "test_data.pdetarc.gz" -Algorithm SHA256).Hash.ToLower()
5e127d9ceeef0ee0d9269be5fa4e721bc809f11f595b22b957989d36d9a79bba
PS C:\workspace>
```

### v. 👉test_data.pdetarcの中間状態から解凍後に圧縮しても同じハッシュ値再現した。

---

## ⅲ. 🟥Dockerイメージを使った動作検証

### a. 👉Dockerイメージを全て削除

```
PS C:\workspace> docker images
                                                                                                    i Info →   U  In Use
IMAGE            ID             DISK USAGE   CONTENT SIZE   EXTRA
pdetarc:latest   17ac47418ced       1.47GB          381MB
python:3.12.3    3966b81808d8       1.47GB          381MB
PS C:\workspace> docker ps -q
PS C:\workspace> docker rmi $(docker images -q)
Untagged: pdetarc:latest
Deleted: sha256:17ac47418ced7a1667fa699c4b9ddb8caae99de68a72bb8a19d53542bf93b4c5
Untagged: python:3.12.3
Deleted: sha256:3966b81808d864099f802080d897cef36c01550472ab3955fdd716d1c665acd6
PS C:\workspace> docker images
                                                                                                    i Info →   U  In Use
IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTRA
PS C:\workspace> rm test_data.pdetarc.gz
PS C:\workspace> rm .\pdetarc.log
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     16:08                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace>
```

### b. 👉test_dataをpdetarc.batにD&Dする。

```
==== PDETARC DOCKER DROPLET START ====
Input: C:\workspace\test_data
Dir  : C:\workspace
Name : test_data
Running Docker...
Unable to find image 'pdetarc:latest' locally
docker: Error response from daemon: pull access denied for pdetarc, repository does not exist or may require 'docker login'

Run 'docker run --help' for more information

==== RETURN CODE: 125 ====
==== PDETARC DOCKER DROPLET END ====
続行するには何かキーを押してください . . .
```

### c. 👉Dockerイメージ削除したから動かない。（正常動作）

### d. 👉Dockerイメージ（pdetarc_image_v1.0.0.tar）の読み込み

```
PS C:\workspace> ls .\test_data\


    ディレクトリ: C:\workspace\test_data


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2026/04/28     15:47                archive
d-----        2026/04/28     16:08                backup
-a----        2000/01/01      9:00           2340 bundle-hash.json
-a----        2000/01/01      9:00           2333 manifest.json
-a----        2000/01/01      9:00        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00       19855536 pdetarc-extract-linux
-a----        2000/01/01      9:00        7349360 pdetarc-extract-mac
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00         167143 pdetarc-tools-source.tar.gz
-a----        2000/01/01      9:00     1041643520 pdetarc_image_v1.0.0.tar
-a----        2000/01/01      9:00        2738412 README.pdf


PS C:\workspace> docker load --input .\test_data\pdetarc_image_v1.0.0.tar
Loaded image: pdetarc:latest
PS C:\workspace> docker images
                                                                                                    i Info →   U  In Use
IMAGE            ID             DISK USAGE   CONTENT SIZE   EXTRA
pdetarc:latest   f50c88e97750       2.14GB         1.04GB
PS C:\workspace>
```
### e. 👉test_dataをpdetarc.batにD&Dする。

```
==== PDETARC DOCKER DROPLET START ====
Input: C:\workspace\test_data
Dir  : C:\workspace
Name : test_data
Running Docker...
[2026-04-28 07:28:20 UTC] ==== PDETARC START ====
[2026-04-28 07:28:20 UTC] モード: 圧縮
[2026-04-28 07:28:20 UTC] 入力: /work/test_data
[2026-04-28 07:28:20 UTC] 既存の manifest.json を検出しました。整合性を検査します...
[2026-04-28 07:28:39 UTC] 事前検査完了: すべてのファイルの整合性が確認されました（混入なし）。
[2026-04-28 07:35:00 UTC] 完了: /work/test_data.pdetarc.gz
[2026-04-28 07:35:00 UTC] ==== PDETARC END ====

==== RETURN CODE: 0 ====
==== PDETARC DOCKER DROPLET END ====
続行するには何かキーを押してください . . .
```

### f. 👉bash確認

```
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     16:29                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2026/04/28     16:35            489 pdetarc.log
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     16:34      822579872 test_data.pdetarc.gz


PS C:\workspace> cat .\pdetarc.log
[2026-04-28 07:28:20 UTC] ==== PDETARC START ====
[2026-04-28 07:28:20 UTC] モード: 圧縮
[2026-04-28 07:28:20 UTC] 入力: /work/test_data
[2026-04-28 07:28:20 UTC] 既存の manifest.json を検出しました。整合性を検査します...
[2026-04-28 07:28:39 UTC] 事前検査完了: すべてのファイルの整合性が確認されました（混入なし）。
[2026-04-28 07:35:00 UTC] 完了: /work/test_data.pdetarc.gz
[2026-04-28 07:35:00 UTC] ==== PDETARC END ====
PS C:\workspace> (Get-FileHash "test_data.pdetarc.gz" -Algorithm SHA256).Hash.ToLower()
5e127d9ceeef0ee0d9269be5fa4e721bc809f11f595b22b957989d36d9a79bba
PS C:\workspace> rm .\pdetarc.log
PS C:\workspace> rm .\test_data.pdetarc.gz
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     16:35                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md


PS C:\workspace>
```

### g. 👉Dockerイメージを読み込んで圧縮しても同じハッシュ値が生成された。

### h. 👉コマンドを使って圧縮

```
PS C:\workspace> Get-ChildItem -Path "test_data" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data\archive
C:\workspace\test_data\backup
C:\workspace\test_data\bundle-hash.json
C:\workspace\test_data\manifest.json
C:\workspace\test_data\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\pdetarc-extract-linux
C:\workspace\test_data\pdetarc-extract-mac
C:\workspace\test_data\pdetarc-extract-windows.exe
C:\workspace\test_data\pdetarc-tools-source.tar.gz
C:\workspace\test_data\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\README.pdf
C:\workspace\test_data\archive\png
C:\workspace\test_data\archive\portable-deterministic-archive-v1
C:\workspace\test_data\archive\test.html
C:\workspace\test_data\archive\png\pdetarc_concepts.png
C:\workspace\test_data\archive\portable-deterministic-archive-v1\bundle.toml
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-macos-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-ubuntu-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-windows-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-tools-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\archive\portable-deterministic-archive-v1\README.pdf
C:\workspace\test_data\backup\bundle-hash.json
C:\workspace\test_data\backup\manifest.json
C:\workspace\test_data\backup\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\backup\pdetarc-extract-linux
C:\workspace\test_data\backup\pdetarc-extract-mac
C:\workspace\test_data\backup\pdetarc-extract-windows.exe
C:\workspace\test_data\backup\pdetarc-tools-source.tar.gz
C:\workspace\test_data\backup\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\backup\README.pdf


PS C:\workspace> docker run --rm -v .:/work pdetarc test_data
[2026-04-28 07:38:52 UTC] ==== PDETARC START ====
[2026-04-28 07:38:52 UTC] モード: 圧縮
[2026-04-28 07:38:52 UTC] 入力: /work/test_data
[2026-04-28 07:38:52 UTC] 既存の manifest.json を検出しました。整合性を検査します...
[2026-04-28 07:39:11 UTC] 事前検査完了: すべてのファイルの整合性が確認されました（混入なし）。
[2026-04-28 07:45:32 UTC] 完了: /work/test_data.pdetarc.gz
[2026-04-28 07:45:32 UTC] ==== PDETARC END ====
PS C:\workspace> ls


    ディレクトリ: C:\workspace


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2000/01/01      9:00                .github
d-----        2026/04/28     16:39                test_data
-a----        2000/01/01      9:00           1201 Dockerfile
-a----        2000/01/01      9:00           2640 LICENSE.md
-a----        2026/04/28     13:24        1827674 pdetarc-docker-app-source.tar.gz
-a----        2000/01/01      9:00        8267545 pdetarc-extract-windows.exe
-a----        2000/01/01      9:00            625 pdetarc.bat
-a----        2026/04/28     16:45            489 pdetarc.log
-a----        2000/01/01      9:00          10415 pdetarc.py
-a----        2000/01/01      9:00        1893180 pdetarc_concepts.png
-a----        2000/01/01      9:00          12493 README.md
-a----        2026/04/28     16:45      822579872 test_data.pdetarc.gz


PS C:\workspace> cat .\pdetarc.log
[2026-04-28 07:38:52 UTC] ==== PDETARC START ====
[2026-04-28 07:38:52 UTC] モード: 圧縮
[2026-04-28 07:38:52 UTC] 入力: /work/test_data
[2026-04-28 07:38:52 UTC] 既存の manifest.json を検出しました。整合性を検査します...
[2026-04-28 07:39:11 UTC] 事前検査完了: すべてのファイルの整合性が確認されました（混入なし）。
[2026-04-28 07:45:32 UTC] 完了: /work/test_data.pdetarc.gz
[2026-04-28 07:45:32 UTC] ==== PDETARC END ====
PS C:\workspace> (Get-FileHash "test_data.pdetarc.gz" -Algorithm SHA256).Hash.ToLower()
5e127d9ceeef0ee0d9269be5fa4e721bc809f11f595b22b957989d36d9a79bba
PS C:\workspace> Get-ChildItem -Path "test_data" -Recurse | Select-Object FullName

FullName
--------
C:\workspace\test_data\archive
C:\workspace\test_data\backup
C:\workspace\test_data\bundle-hash.json
C:\workspace\test_data\manifest.json
C:\workspace\test_data\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\pdetarc-extract-linux
C:\workspace\test_data\pdetarc-extract-mac
C:\workspace\test_data\pdetarc-extract-windows.exe
C:\workspace\test_data\pdetarc-tools-source.tar.gz
C:\workspace\test_data\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\README.pdf
C:\workspace\test_data\archive\png
C:\workspace\test_data\archive\portable-deterministic-archive-v1
C:\workspace\test_data\archive\test.html
C:\workspace\test_data\archive\png\pdetarc_concepts.png
C:\workspace\test_data\archive\portable-deterministic-archive-v1\bundle.toml
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-macos-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-ubuntu-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-extract-windows-latest.zip
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc-tools-source.tar.gz
C:\workspace\test_data\archive\portable-deterministic-archive-v1\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\archive\portable-deterministic-archive-v1\README.pdf
C:\workspace\test_data\backup\bundle-hash.json
C:\workspace\test_data\backup\manifest.json
C:\workspace\test_data\backup\pdetarc-docker-app-source.tar.gz
C:\workspace\test_data\backup\pdetarc-extract-linux
C:\workspace\test_data\backup\pdetarc-extract-mac
C:\workspace\test_data\backup\pdetarc-extract-windows.exe
C:\workspace\test_data\backup\pdetarc-tools-source.tar.gz
C:\workspace\test_data\backup\pdetarc_image_v1.0.0.tar
C:\workspace\test_data\backup\README.pdf


PS C:\workspace>
```

### i. 👉コマンドを使って圧縮しても同じハッシュ値が生成された。

### j. 👉test_dataフォルダのルート直下にあったものはbackupフォルダに退避されている。

### k. 👉動作検証完了。
