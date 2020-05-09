from aiohttp import web
import aiohttp_jinja2
import jinja2

from aiohttp_desafio.settings import config, BASE_DIR
from aiohttp_desafio.routes import setup_routes
from aiohttp_desafio.db import close_pg, init_pg
from aiohttp_desafio.middlewares import setup_middlewares

app = web.Application()
app['config'] = config
aiohttp_jinja2.setup(app,
                     loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiohttp_desafio' / 'templates')))
setup_routes(app)
setup_middlewares(app)
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app)
