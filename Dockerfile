# Docker Hubにあるpythonイメージをベースにする
FROM python:3.8.5

# 環境変数を設定する
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libzip-dev zlib1g-dev libpng-dev libssl1.1 libjpeg-dev gnupg unzip wget build-essential xorg libxrender-dev wget gdebi libgraphviz-dev graphviz pkg-config

# コンテナ内にcodeディレクトリを作り、そこをワークディレクトリとする
RUN mkdir /code
WORKDIR /code

# ホストPCにあるrequirements.txtをコンテナ内のcodeディレクトリにコピーする
# コピーしたrequirements.txtを使ってパッケージをインストールする
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# ホストPCの各種ファイルをcodeディレクトリにコピーする
COPY . /code

# 起動用のスクリプトをコピーする
COPY ./docker/docker-entrypoint.sh /
RUN chmod 777 /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
