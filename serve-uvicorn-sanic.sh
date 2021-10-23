#!/usr/bin/env bash

uvicorn --port 8001 -host 0.0.0.0 --workers $PWPWORKERS app_sanic:app
