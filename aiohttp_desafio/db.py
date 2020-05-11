import aiopg.sa
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String
)

__all__ = ['state', 'city']

meta = MetaData()

state = Table(
    'state', meta,

    Column('id', Integer, primary_key=True),
    Column('state_name', String(30), nullable=False)
)

city = Table(
    'city', meta,

    Column('id', Integer, primary_key=True),
    Column('city_name', String(50), nullable=False),

    Column('state_id',
           Integer,
           ForeignKey('state.id', ondelete='CASCADE'))
)


class RecordNotFound(Exception):
    """Requested record in database was not found"""


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


async def get_state(conn, state_id):
    result = await conn.execute(
        state.select()
            .where(state.c.id == state_id))
    state_record = await result.first()
    if not state_record:
        msg = "State with id: {} does not exists"
        raise RecordNotFound(msg.format(state_id))
    result = await conn.execute(
        city.select()
            .where(city.c.state_id == state_id)
            .order_by(city.c.id))
    cities_records = await result.fetchall()
    return state_record, cities_records


async def create_state(conn, state_name):
    stmt = state.insert().values(state_name=state_name)
    await conn.execute(stmt)


async def create_city(conn, city_name, state_id):
    stmt = city.insert().values(city_name=city_name, state_id=int(state_id))
    await conn.execute(stmt)
