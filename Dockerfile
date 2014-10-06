FROM ubuntu:14.04

# bring software up to date
RUN apt-get update
RUN apt-get upgrade -y

# locales (for postgres)
RUN apt-get install -y language-pack-en
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN locale-gen en_US.UTF-8

# we want python (and pip)
RUN apt-get install -y build-essential python-dev python-pip

# we want postgres
RUN apt-get install -y postgresql postgresql-contrib libpq-dev


RUN echo $ENVIRONMENT

# install sentry and postgres binding
ADD requirements.txt /
RUN pip install -r /requirements.txt

# move sentry config to default location
ADD sentry.conf.py /.sentry/sentry.conf.py
RUN sentry upgrade

ADD boostrap.py /boostrap.py
# RUN python boostrap.py


RUN sentry repair --owner=ozan

EXPOSE 3000
