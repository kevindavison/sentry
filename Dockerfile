FROM ubuntu

ENV DB_HOST localhost
ENV MAILGUN_ACCESS_KEY 12345
ENV MAILGUN_SERVER_NAME localhost
ENV SENTRY_URL_PREFIX http://sentry.local.com

# update packages
RUN apt-get update  # cachebust
RUN apt-get upgrade -y

# set locales (for postgres)
RUN apt-get install -y language-pack-en
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN locale-gen en_US.UTF-8

# we want python (and pip)
RUN apt-get install -y \
	build-essential \
	python-dev \
	python-pip \
	postgresql \
	postgresql-contrib \
	libpq-dev

# add the source code
RUN mkdir -p /app
WORKDIR /app
ADD . /app/

# move sentry config to default location
ADD sentry.conf.py /root/.sentry/sentry.conf.py

# install sentry and postgres binding
RUN pip install -r /app/requirements.txt


EXPOSE 9000


#FROMCACHE vida-sentry
