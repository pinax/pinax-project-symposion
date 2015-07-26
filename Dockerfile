FROM debian:jessie
MAINTAINER pinax_project
ENV PATH=/usr/local/bin:${PATH}

## Your configuration

ENV PROJECT_NAME=conf_site

## security upgrade and install dependencies
RUN apt-get update && apt-get upgrade -y --no-install-recommends && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential make g++ gcc libc6-dev git vim \
    curl libcurl3 libcurl3-nss \
    libssl-dev libyaml-dev libffi-dev \
    ca-certificates software-properties-common yui-compressor \
    libpq5 sqlite3 libmysqlclient18 \
    libpcre3 libxml2 libxslt1.1 \
    libreadline5 libyaml-0-2\
    libmysqlclient-dev libsqlite3-dev libpq-dev \
    libcurl4-openssl-dev libpcre3-dev libxml2-dev libxslt-dev \
    libreadline-gplv2-dev \
    python2.7 python2.7-minimal python2.7-dev python-nose python-coverage \
    python-pysqlite2 libfreetype6-dev python-virtualenv \
    libjpeg-dev zlib1g-dev liblcms2-dev libwebp-dev && \
    apt-get clean
## install pip and node/npm
RUN curl -sL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python - && \
    curl -sL https://deb.nodesource.com/setup | bash - && apt-get install -y nodejs
## workaround and update npm
RUN ln -s /usr/include/freetype2 /usr/local/include/freetype && \
    npm install -g npm@latest && \
    npm install -g less
## install website source
RUN mkdir -p /opt/pyapp/
WORKDIR /opt/pyapp
RUN virtualenv .VENV
RUN source .VENV/bin/activate && \
    pip install Django==1.7.1 && \
    django-admin.py startproject --extension=py,json --template=https://github.com/pinax/pinax-project-symposion/zipball/master ${PROJECT_NAME}
WORKDIR /opt/pyapp/${PROJECT_NAME}
RUN source .VENV/bin/activate && \
    pip install -r requirements.txt && \
    python manage.py migrate && \
    python manage.py loaddata fixtures/* 

CMD ["/usr/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
