#!/usr/bin/env bash

uwsgi --http-socket 0.0.0.0:8001 -w app_flask:app --processes $PWPWORKERS
