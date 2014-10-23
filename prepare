#!/bin/bash

# create the initial schema if needed
sentry upgrade

# run bootstrap script to add our default team, projects and superusers
# see http://sentry.readthedocs.org/en/latest/faq/index.html#how-do-i
python boostrap.py

# as the default superuser was not created on the first `upgrade` run,
# sentry requires us to
sentry repair --owner=ozan
