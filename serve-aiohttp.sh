#!/usr/bin/env bash

gunicorn app_aio:app -w $PWPWORKERS --bind 0.0.0.0:8001 --worker-class aiohttp.GunicornWebWorker
