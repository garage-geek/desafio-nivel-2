from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String
)

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
