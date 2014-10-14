FROM ubuntu:14.04

# update packages
RUN apt-get update
RUN apt-get upgrade -y

# set locales (for postgres)
RUN apt-get install -y language-pack-en
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN locale-gen en_US.UTF-8

# we want python (and pip)
RUN apt-get install -y build-essential python-dev python-pip

# we want postgres
RUN apt-get install -y postgresql postgresql-contrib libpq-dev

# install sentry and postgres binding
ADD requirements.txt /
RUN pip install -r /requirements.txt

# move sentry config to default location
ADD sentry.conf.py /.sentry/sentry.conf.py

# create the initial schema
RUN sentry upgrade

# run bootstrap script to add our default team, projects and superusers
# see http://sentry.readthedocs.org/en/latest/faq/index.html#how-do-i
ADD boostrap.py /boostrap.py
RUN python boostrap.py

# as the default superuser was not created on the first `upgrade` run,
# sentry requires us to
RUN sentry repair --owner=ozan

EXPOSE 3000
