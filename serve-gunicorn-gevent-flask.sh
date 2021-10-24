#!/usr/bin/env bash


export GEVENT=1
gunicorn --bind 0.0.0.0:8001 -w $PWPWORKERS app_flask:app --worker-class gunicorn.workers.ggevent.GeventWorker --worker-connections 100
