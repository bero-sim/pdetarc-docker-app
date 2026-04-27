# https://github.com/bero-sim/pdetarc-docker-app/blob/main/Dockerfile
# Python 3.12.3 (Debian Bookworm) の特定のイメージを指紋で指定
# これにより、イメージが更新されても古い「この版」を使い続けられる
# PS C:\workspace\pdetarc-docker-app-main> docker pull python:3.12.3
# 3.12.3: Pulling from library/python
# 2a4ca5af09fa: Pull complete
# bf2c3e352f3d: Pull complete
# 891494355808: Pull complete
# a99509a32390: Pull complete
# d46a03def8d9: Pull complete
# 4429b810e09e: Pull complete
# 6582c62583ef: Pull complete
# c6cf28de8a06: Pull complete
# Digest: sha256:3966b81808d864099f802080d897cef36c01550472ab3955fdd716d1c665acd6
FROM python@sha256:3966b81808d864099f802080d897cef36c01550472ab3955fdd716d1c665acd6

WORKDIR /work

# スクリプトをコピー
COPY pdetarc.py /app/

# RUN apt-get update && apt-get install -y tar gzip && rm -rf /var/lib/apt/lists/*
# OS側のtar/gzipをインストールせず、Python標準機能のみに頼ることで
# OSパッケージの更新による影響をゼロにする。
# もしどうしてもOS側が必要なら、バージョンを固定して記述する。

ENTRYPOINT ["python", "/app/pdetarc.py"]
