Sentry server
===

This project represents the configuration required to deploy a Sentry
server for our projects.


Local installation
---
To run locally (eg for testing) install docker then

    docker build -t vida/sentry .
    docker run -p 3000:3000 --entrypoint="sentry" vida/sentry start

and visit http://[DOCKER_HOST]:3000 in your browser


Deployment
---

After cloning the project, add the remotes:

    git remote add staging git@beta.aptible.com:vida-sentry-staging-2.git
    git remote add production git@beta.aptible.com:vida-sentry-production.git

Then `git push production master` etc.
