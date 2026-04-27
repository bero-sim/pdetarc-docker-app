<!-- https://github.com/bero-sim/pdetarc-docker-app/blob/main/README.md -->
# PDETARC (v1.0.0)

Portable Deterministic Archive Tool for Long-term Digital Integrity

PDETARC（ピーデットアーク）は、デジタル資産の恒久的な継承を実現するために設計された、決定論的アーカイブツールです。

時代の変遷や技術基盤の変化に左右されず、アーカイブされたその瞬間の「環境」と「データ」を数学的な同一性をもって次世代へと繋ぎます。

---

## 🌟 特徴
- **完全な再現性**: Dockerイメージを固定（SHA256指定）することで、いつでも全く同じバイナリを生成します。
- **決定論的パッキング**: ファイルのタイムスタンプやメタデータの差異を排除し、中身が同じなら常に同じハッシュ値（SHA256）を持つアーカイブを生成します。
- **自己完結型**: アーカイブ内に[解凍ツール](https://github.com/bero-sim/pdetarc-tools/releases)（Win/Mac/Linux）と、再構築用の[Dockerイメージ](https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc_image_v1.0.0.tar)（`pdetarc_image_v1.0.0.tar`）およびソースコード（[圧縮用](https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc-docker-app-source.tar.gz)、[解凍用](https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/pdetarc-extract-windows-latest.zip)）を自動同梱します。
- **データの誠実性**: SHA256ハッシュ値により、1ビットの改ざんや破損も許さない厳格な検証を行います。

---

## ❄️ 決定論的アーカイブを支える「3つの固定」

本ツールが、環境や時間を超えて「常に同じハッシュ値」を再現できるのは、以下の3つの要素を技術的に固定しているためです。

1. **実行環境の固定（Environment Pinning）**
    - **仕組み**: `Dockerfile` において、ベースイメージをタグではなく、不変の識別子である **SHA256 Digest** で指定しています。
    - **効果**: [公式リポジトリ](https://github.com/bero-sim/pdetarc-tools)から特定のタグが消えていても、ビルド時に当時と全く同一のバイナリ環境が再現されます。
2. **ファイルメタデータの初期化（Metadata Neutralization）**
    - **仕組み**: パッキングの際、各ファイルの「更新日時」や「権限」をすべて特定の基準値（Unixエポック 0 等）に書き換えます。
    - **効果**: 「今日」固めても「X年後」に固めても、時刻の差異によるハッシュ値の変化が発生しません。
3. **バイナリ・パッキング・ロジックの固定（Binary Logic Pinning）**
    - **仕組み**: ファイルの格納順を辞書順でソートし、圧縮パラメータを固定しています。
    - **効果**: 並列処理等による順序の入れ替わりを排除し、ビット単位で一貫したバイナリを生成します。

![概念図:PDETARC:3つの固定](https://raw.githubusercontent.com/bero-sim/pdetarc-docker-app/refs/heads/main/pdetarc_concepts.png)

---

### 💡 PDETARC利用者が得られる「安心」の根拠

| 変数 | 一般的なアーカイブ | PDETARC |
| :--- | :--- | :--- |
| **作成日時** | 実行時の時刻（毎回変わる） | **2000-01-01 00:00:00 UTC（固定）** |
| **OS環境** | その時の最新OS（変動する） | **SHA256指定のDocker（固定）** |
| **ファイル順序** | ファイルシステム依存 | **辞書順ソート（固定）** |
| **ハッシュ値** | 毎回異なる可能性がある | **常に同一（決定論的）** |

---

## 🛠 セットアップ
1. **前提条件**
   - [Docker](https://www.docker.com/ja-jp/) が動作する環境（Windows / macOS / Linux）
2. **準備**
   - [ソースコード](https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc-docker-app-source.tar.gz)を展開し、 `pdetarc.py` , `Dockerfile` , `pdetarc.bat` を作業フォルダ（例: `C:\workspace`）に配置します。
3. **実行環境の構築**
   - 作業フォルダで以下のコマンドを実行し、専用イメージをビルドします。<br>
`docker build -t pdetarc .`
     - 💡 **同一性の保証（技術注記）**
本ビルドは `python:3.12.3` を SHA256 で厳密に指定するため、いつ誰が実行しても内部環境は同一になります。<br>
※生成されるイメージを `docker save` で出力した際のファイルハッシュ値は、実行時刻等のメタデータにより変動しますが、`Dockerfile` のDigestが一致していれば実行環境としての真正性は担保されます。

---

### 💡 ビルドがうまくいかない場合（オフライン・将来の復元）

ネットワーク環境がない場合や、[Docker Hub](https://www.docker.com/ja-jp/products/docker-hub/) の仕様変更等で `docker build` が失敗する場合は、同梱されている[イメージファイル](https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc_image_v1.0.0.tar)を直接読み込んでください。

1. **イメージの読み込み**:<br>アーカイブ内に同梱されている（または `pdetarc-docker-app` から[入手](https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc_image_v1.0.0.tar)した） `pdetarc_image_v1.0.0.tar` ファイルを使用します。以下のコマンドを実行してイメージを読み込みます。
   - **Powershell**: `docker load --input pdetarc_image_v1.0.0.tar`
   - **Bash / コマンドプロンプト**: `docker load < pdetarc_image_v1.0.0.tar`
3. **確認**:<br>以下のコマンドで `pdetarc` イメージがリストに現れれば復元完了です。<br>`docker images`<br>※ `docker load` で復元した場合も、`docker build` した時と全く同一のバイナリ環境が再現されます。

---

## 🚀 使い方

1. **圧縮（アーカイブ `.pdetarc.gz` の作成）**
   1. **圧縮方法**
      - **ドロップレット使用**: 圧縮対象のフォルダを `pdetarc.bat` にドラッグ＆ドロップしてください。
      - **コマンド使用**: `docker run --rm -v .:/work pdetarc [圧縮対象のフォルダ名]`）
   2. **圧縮後確認**: `pdetarc.log` に **「完了:」** と表示されれば圧縮成功です。
3. **解凍（データの復元）**
   1. **解凍方法**
      - **ドロップレット**: `.pdetarc.gz` を `pdetarc-extract` ツールにドラッグ＆ドロップしてください。
   2. **展開後確認** `pdetarc-extract.log` に **「検証結果: OK（完全一致）」** と表示されれば復元成功です。

---

### 🛡️ 実行時の注意（セキュリティと権限）

本ツールは未署名のバイナリとして提供されているため、初回実行時に各OSのセキュリティ機能によってブロックされる場合があります。

- **Windows をご利用の場合**
  - 実行時に「WindowsによってPCが保護されました」と表示された場合は、[詳細情報] をクリックし、表示された [実行] ボタンを押してください。
- **macOS / Linux をご利用の場合**
  1. **実行権限の付与**: ターミナルで以下のコマンドを実行し、実行権限を与えてください。
     - **macOS**: `chmod +x pdetarc-extract-mac`<br>
     - **Linux**: `chmod +x pdetarc-extract-linux`
  2. macOS Gatekeeper: 初回起動時に「開発元を検証できないため開けません」と表示された場合は、右クリック（または Control+クリック）から [開く] を選択し、ダイアログで再度 [開く] をクリックしてください。

---

## 📁 フォルダ・アーカイブ構造

1. **アーカイブ作成対象のフォルダ構成（最小構成）**
    - 実データはルート直下の `archive` フォルダ中に配置してください。<br>※圧縮対象はルート直下の `archive` フォルダのみです。その他は圧縮前に `backup` フォルダに退避されて圧縮されません。
    - `bundle.toml`は公式リポジトリから[入手](https://github.com/bero-sim/pdetarc-tools/releases/download/v1.0.0/bundle.toml)可能です。

```
project_folder/
└── archive/
     ├── portable-deterministic-archive-v1/
     │    ├── bundle.toml      # ツール取得元リスト
     │    └── README.pdf       # ツール利用者向けマニュアル
     └── [実データ]             # フォルダ・ファイル
```

2. **アーカイブ（.pdetarc.gz）の内部構造**

```
archive.pdetarc.gz/
├── manifest.json                      # 各ファイルのSHA256リスト
├── bundle-hash.json                   # 同梱ツールの検証データ
├── pdetarc-extract-linux              # 解凍ツールlinux用
├── pdetarc-extract-mac                # 解凍ツールmac用
├── pdetarc-extract-windows.exe        # 解凍ツールwindows用
├── pdetarc_image_v1.0.0.tar           # 圧縮ツールDockerイメージ
├── pdetarc-docker-app-source.tar.gz   # ソースファイル圧縮関連
├── pdetarc-tools-source.tar.gz        # ソースファイル解凍関連
├── README.pdf                         # ツール利用者向けマニュアル
└── files/                             # 実データ（パッキングされた保護状態）
```

---

## 🛡 トラブルシューティング（ヒューマンエラーへの対応）

本アーカイブは決定論的に構築されているため、操作ミスによるデータ喪失や混乱に対しても、以下の方法で「元の正しい状態」を復元・再証明できます。

1. **展開後に元のアーカイブ（`.pdetarc.gz`）を紛失した場合**
    - **状況**: アーカイブを展開して中身を取り出したが、元の `.pdetarc.gz` ファイル自体を誤って削除してしまった。
    - **処置**: 展開された中身（`archive/` フォルダや `manifest.json` 等）がすべて揃っていれば、内部同梱の [Dockerイメージ](https://github.com/bero-sim/pdetarc-docker-app/releases/download/v1.0.0/pdetarc_image_v1.0.0.tar)（`pdetarc_image_v1.0.0.tar`）を用いて、再びアーカイブ化を実行してください。その際、ルート直下に `manifest.json` を置いてあるとファイルの過不足検査とハッシュ値検査が実施されます。<br>※必要なファイルやフォルダの階層情報は `manifest.json` の `path` に記録されています。
    - **結果**: 1ビットの差異もなく、**元と全く同一のハッシュ値を持つ `.pdetarc.gz` が再生成**されます。これにより、手元のデータがオリジナルと同じ正真のものであることをいつでも再証明可能です。
2. **「中身を取り出した」と誤認して、元のアーカイブを削除してしまった場合**
    - **状況**: OS標準の右クリックメニュー等で展開した際、`.pdetarc` という中間フォルダだけが生成されることがあります。この時、「解凍が完了した」と勘違いして、元の `.pdetarc.gz` ファイルを削除してしまい、詰んでしまった場合。
    - **処置**: 焦る必要はありません。その中間フォルダ（`.pdetarc`）を、同梱されている `pdetarc-extract` ツールへそのままドラッグ＆ドロップしてください。
    - **結果**: ツールが中間状態を認識し、最終的なデータ展開とハッシュ検証を完遂させます。
  
---

## 📄 ライセンス・著作権
本プロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE.md) ファイルをご覧ください。

---

## 🔗 関連
- **[pdetarc-tools](https://github.com/bero-sim/pdetarc-tools)**  (Binary & Extraction Logic)
- **[Operation-verification](Operation-verification.md)**（Actual behavior）
- **ファイルハッシュ値（SHA256）の確認方法**
  - **Windows（PowerShell）**: `(Get-FileHash "filename" -Algorithm SHA256).Hash.ToLower()`
  - **macOS ／ Linux（ターミナル）**: `shasum -a 256 "filename" | awk '{print $1}'`
