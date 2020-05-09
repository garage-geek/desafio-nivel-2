from aiohttp import web
import aiohttp_jinja2
import db


@aiohttp_jinja2.template('index.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.state.select())
        records = await cursor.fetchall()
        states = [dict(s) for s in records]
        return {"states": states}


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
