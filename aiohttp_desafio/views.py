import json
from aiohttp import web
import aiohttp_jinja2
from aiohttp_desafio import db


def redirect(router, route_name):
    location = router[route_name].url_for()
    return web.HTTPFound(location)


@aiohttp_jinja2.template('index.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.state.select())
        records = await cursor.fetchall()
        states = [dict(s) for s in records]
        return {'states': states}


@aiohttp_jinja2.template('detail.html')
async def state_city(request):
    async with request.app['db'].acquire() as conn:
        state_id = request.match_info['state_id']
        try:
            state, cities = await db.get_state(conn,
                                               state_id)
        except db.RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))
        return {
            'state': state,
            'cities': cities
        }


@aiohttp_jinja2.template('state.html')
async def state(request):
    if request.method == 'POST':
        form = await request.post()

        async with request.app['db'].acquire() as conn:
            await db.create_state(conn, form['state_name'])
            raise redirect(request.app.router, 'index')
    return {}


@aiohttp_jinja2.template('city.html')
async def city(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.state.select())
        records = await cursor.fetchall()
        states = [dict(s) for s in records]
    return {'states': states}


async def index_api(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.state.select())
        records = await cursor.fetchall()
        states = [dict(s) for s in records]
        response_obj = {'status': 'success', 'states': states}
        return web.Response(text=json.dumps(response_obj), status=200)


async def state_city_api(request):
    async with request.app['db'].acquire() as conn:
        state_id = request.match_info['state_id']
        try:
            state, cities = await db.get_state(conn,
                                               state_id)
            state = dict(state)
            cities = [dict(c) for c in cities]
        except db.RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))
        response_obj = {'status': 'success', 'state': state, 'cities': cities}
        return web.Response(text=json.dumps(response_obj), status=200)
