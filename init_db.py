from sqlalchemy import create_engine, MetaData

from aiohttp_desafio.settings import config
from aiohttp_desafio.db import state, city

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[state, city])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(state.insert(), [
        {'state_name': 'Minas Gerais'},
        {'state_name': 'Rio Grande do Sul'},

    ])
    conn.execute(city.insert(), [
        {'city_name': 'Belo Horizonte', 'state_id': 1},
        {'city_name': 'Sabará', 'state_id': 1},
        {'city_name': 'Caxias do Sul', 'state_id': 2},
    ])
    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
