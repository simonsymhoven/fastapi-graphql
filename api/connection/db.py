from sqlalchemy import create_engine, MetaData
from api.core.config import settings


def get_url():
    user = settings.POSTGRES_USER
    password = settings.POSTGRES_PASSWORD
    db = settings.POSTGRES_DB
    server = settings.POSTGRES_SERVER
    return f"postgresql://{user}:{password}@{server}/{db}"


SQLALCHEMY_DATABASE_URL = get_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
meta = MetaData()
connection = engine.connect()
