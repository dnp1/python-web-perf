#!/usr/bin/env bash

uwsgi --uwsgi-socket 0.0.0.0:8001 -w app_bottle:app --processes $PWPWORKERS
