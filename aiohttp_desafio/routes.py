import pathlib

from aiohttp_desafio.views import index, state_city, index_api, state_city_api, state, city, city_api, state_api

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get('/', index, name='index')
    app.router.add_get('/state_city/{state_id}', state_city, name='state_city')
    app.router.add_get('/state', state, name='state')
    app.router.add_post('/state', state, name='state')
    app.router.add_get('/city', city, name='city')
    app.router.add_post('/city', city, name='city')

    app.router.add_get('/api', index_api, name='index_api')
    app.router.add_get('/api/{state_id}', state_city_api, name='state_city_api')
    app.router.add_post('/api/state', state_api, name='state_api')
    app.router.add_post('/api/city', city_api, name='city_api')
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=PROJECT_ROOT / 'static',
                          name='static')
