#!/bin/sh

export FLASK_APP=apps:app
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
