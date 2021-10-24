import json
from aiohttp import web
import aiopg

from async_db import get_row, get_pool


async def handle(request):
    a, b = await get_row()
    return web.Response(text=json.dumps({
                                            "a": str(a).zfill(10),
                                            "b": b
                                        }))


async def close_db(app_):
    pool = await get_pool()
    pool.close()
    await pool.wait_closed()


app = web.Application()
app.on_shutdown.append(close_db)
app.add_routes([web.get('/test', handle)])
