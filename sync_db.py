import random
from os import getenv

import psycopg2.pool

from db_config import PG_HOST, PG_DATABASE, PG_USER, PG_PASSWORD, PG_PORT, PG_POOL_SIZE
from gevent_proper_pool import ReallyThreadedConnectionPool

pool = None

if getenv("GEVENT"):
    Pool = ReallyThreadedConnectionPool
    max_conn = PG_POOL_SIZE
    min_conn = PG_POOL_SIZE
else:
    Pool = psycopg2.pool.SimpleConnectionPool
    max_conn = 1
    min_conn = 1


def get_pool():
    global pool

    if pool is None:
        pool = Pool(
            minconn=min_conn, maxconn=max_conn,
            host=PG_HOST,
            database=PG_DATABASE,
            user=PG_USER,
            password=PG_PASSWORD,
            port=PG_PORT,
        )
    return pool


max_n = 1000_000 - 1


def get_sleep(i: int) -> float:
    if i % 100 == 0:
        return .8
    if i % 20 == 0:
        return .2
    if i % 10 == 0:
        return .05
    return .01


def get_row():
    index = random.randint(1, max_n)
    sleep = get_sleep(index)
    conn = get_pool().getconn()
    cursor = conn.cursor()
    cursor.execute("WITH t AS (select pg_sleep(%s)) SELECT a, b FROM test, t WHERE a = %s;", (sleep, index,))
    ((a, b),) = cursor.fetchall()
    cursor.close()
    get_pool().putconn(conn)
    return a, b
