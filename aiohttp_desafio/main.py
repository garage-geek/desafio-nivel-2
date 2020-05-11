import logging
import sys

import aiohttp_jinja2
import jinja2
from aiohttp import web

from aiohttp_desafio.db import close_pg, init_pg
from aiohttp_desafio.middlewares import setup_middlewares
from aiohttp_desafio.routes import setup_routes
from aiohttp_desafio.settings import get_config


async def init_app(argv=None):

    app = web.Application()

    app['config'] = get_config(argv)

    # setup Jinja2 template renderer
    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('aiohttp_desafio', 'templates'))

    # create db connection on startup, shutdown on exit
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    # setup views and routes
    setup_routes(app)

    setup_middlewares(app)

    return app


def main(argv):
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(argv)

    config = get_config(argv)
    web.run_app(app,
                host=config['host'],
                port=config['port'])


if __name__ == '__main__':
    main(sys.argv[1:])
