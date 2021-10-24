#!/usr/bin/bash
set -e
REQUEST_COUNT=1000000

SERVERS=(serve-aiohttp.sh
serve-daphne-starlette.sh
serve-gunicorn-flask.sh
serve-gunicorn-gevent-flask.sh
serve-gunicorn-meinheld-bottle.sh
serve-gunicorn-meinheld-falcon.sh
serve-gunicorn-meinheld-flask.sh
serve-sanic-own.sh
serve-uvicorn-sanic.sh
serve-uvicorn-starlette.sh
serve-uwsgi-bottle.sh
serve-uwsgi-bottle-own-proto.sh
serve-uwsgi-falcon.sh
serve-uwsgi-flask.sh
)

ADD_WORKER=(
  0
  0
  1
  0
  1
  1
  1
  0
  0
  0
  1
  1
  1
  1
)

#docker-compose down -v
#docker-compose up -d reverse-proxy postgres pgbouncer prometheus cadvisor
#sleep 5

#bash prepare_db.sh;

CONCURRENCY=(300)
NUM_CPUS=(1)

for c in "${CONCURRENCY[@]}"; do
  for n in "${NUM_CPUS[@]}"; do
    OUT_DIR=runs_${n}_${c}
    for ((i=0; i < ${#SERVERS[@]}; i++)) do

      mkdir -p $OUT_DIR
      command="${SERVERS[$i]}"
      must_add=${ADD_WORKER[$i]}

      if [[ $must_add -eq "1" ]]
      then
        workers=$((n * 2 + 1))
        POOL_SIZE=1
      else
        workers=$n
        POOL_SIZE=$((96 / n))
      fi

#      promplot


      echo ">>>>>>>>>>>>>>>>";
      echo "Running $command worker:$workers cpus:$n concurrency:$c pool_size:$POOL_SIZE!!";
      docker-compose stop python;
      POOL_SIZE=$POOL_SIZE CPU_COUNT=$n PWPWORKERS=$workers COMMAND=$command docker-compose up -d python;
      sleep 2;

      ab -c $c -n $REQUEST_COUNT http://localhost:8080/test > $OUT_DIR/"${command}.tx" ;
      echo;
      echo;
      echo "<<<<<<<<<<<<<<";
      echo;
    done
    sleep 10;
    bash plot_it.sh $OUT_DIR;
  done
done

