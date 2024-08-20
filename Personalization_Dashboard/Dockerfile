FROM python:3.10
RUN apt-get update \
&& apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        vim
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt && \
    rm -rf /tmp/pip* /root/.cache/pip

ADD ./ /app