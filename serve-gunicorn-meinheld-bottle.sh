#!/usr/bin/env bash

gunicorn --bind 0.0.0.0:8001 -w $PWPWORKERS app_bottle:app --worker-class "egg:meinheld#gunicorn_worker"
