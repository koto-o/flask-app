#!/bin/sh

export FLASK_APP=apps:app
flask run --host=0.0.0.0 --debug

