#!/usr/bin/env bash

gunicorn -w $PWPWORKERS --bind 0.0.0.0:8001 app_flask:app
