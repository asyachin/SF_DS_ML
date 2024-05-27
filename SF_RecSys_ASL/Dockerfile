FROM ubuntu:latest

MAINTAINER Alexander Syachin 'asyachin@gmail.com'

RUN mkdir -p /usr/src/app

RUN set -xe \
    && apt-get update -y\
    && apt-get -y install python3-pip

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install -r requirements.txt

ENV PORT 3000
EXPOSE $PORT

ENTRYPOINT ["python3", "app.py"]