import random
from time import time

import aiopg

from sync_db import get_sleep

pool = None
from db_config import PG_HOST, PG_DATABASE, PG_USER, PG_PASSWORD, PG_PORT, PG_POOL_SIZE


async def get_pool():
    global pool
    if pool is None:
        pool = await aiopg.create_pool(
            dsn=f"dbname={PG_DATABASE} user={PG_USER} password={PG_PASSWORD} port={PG_PORT} host={PG_HOST}",
            minsize=PG_POOL_SIZE, maxsize=PG_POOL_SIZE,
        )
    return pool


max_n = 1000_000 - 1


async def get_row():
    pool = await get_pool()

    index = random.randint(1, max_n)
    sleep = get_sleep(index)
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("WITH t AS (select pg_sleep(%s)) SELECT a, b FROM test, t WHERE a = %s;", (sleep, index,))
            ((a, b),) = await cursor.fetchall()

    return a, b
