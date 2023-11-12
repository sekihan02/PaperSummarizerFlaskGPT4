FROM python:3.10-slim-buster

# 作業ディレクトリの設定
WORKDIR /usr/src/app

# 必要なライブラリのインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# ポートの公開
EXPOSE 5000

# アプリケーションの起動コマンド
CMD ["flask", "run", "--host=0.0.0.0"]
