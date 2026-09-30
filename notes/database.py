from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from decouple import config

connection_URL = config("connection_URL")

engine = create_async_engine(connection_URL)

SessionFactory = async_sessionmaker(engine)