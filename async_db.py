import random
import aiopg

pool = None
from db_config import PG_HOST, PG_DATABASE, PG_USER, PG_PASSWORD, PG_PORT


async def get_pool():
    global pool
    if pool is None:
        pool = await aiopg.create_pool(
            f"dbname={PG_DATABASE} user={PG_USER} password={PG_PASSWORD} port={PG_PORT} host={PG_HOST}")
    return pool


max_n = 1000_000 - 1


async def get_row():
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            index = random.randint(1, max_n)
            await cursor.execute("SELECT a, b FROM test WHERE a = %s", (index,))
            ((a, b),) = await cursor.fetchall()
    return a, b
