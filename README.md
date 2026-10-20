# Flask on AWS Lambda

A template poject for hexagonal (ports and adapters) architecture python
project with Flask server and AWS Lambda adapter.

[TODO: Something about hexagonal architecture]

Idea is to have architectural parts (core, individual adapters) as a separate
namespace packages, so to enable dependency isolation.

## Clone from Github

~~~bash
git clone 
cd flask-on-lambda

~~~

### Flask server for local dev

#### Install

~~~bash
poetry -P fol-adapter-flask install

~~~

#### Test

~~~bash
poetry -P fol-adapter-flask run pytest fol-adapter-flask

~~~

### Build & deploy to lambda

#### Install poetry env

~~~bash
poetry -P fol-deploy install

~~~

#### Build docker image

~~~bash
cd fol-deploy/flask-on-lambda
poetry run sam build

~~~

#### Deploy to aws

~~~bash
cd fol-deploy/flask-on-lambda
poetry run sam deploy -g

~~~

After first guided deployment -g can be omitted.
