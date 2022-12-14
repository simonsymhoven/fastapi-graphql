from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from api.core.config import settings


def get_url():
    user = settings.POSTGRES_USER
    password = settings.POSTGRES_PASSWORD
    db = settings.POSTGRES_DB
    server = settings.POSTGRES_SERVER
    return f"postgresql://{user}:{password}@{server}/{db}"


engine = create_engine(
    get_url(),
    future=True,
    echo=True
)

Base = declarative_base()
Base.metadata.create_all(engine)

connection = engine.connect()
