from os import environ

import psycopg2
import psycopg2.pool
import random

from db_config import PG_HOST, PG_DATABASE, PG_USER, PG_PASSWORD, PG_PORT

pool = None



def get_pool():
    global pool
    if pool is None:
        pool = psycopg2.pool.SimpleConnectionPool(
            1, 4,
            host=PG_HOST,
            database=PG_DATABASE,
            user=PG_USER,
            password=PG_PASSWORD,
            port=PG_PORT,
        )
    return pool


max_n = 1000_000 - 1


def get_row():
    conn = get_pool().getconn()
    cursor = conn.cursor()
    index = random.randint(1, max_n)
    cursor.execute("SELECT a, b FROM test WHERE a = %s;", (index,))
    ((a, b),) = cursor.fetchall()
    cursor.close()
    get_pool().putconn(conn)
    return a, b
