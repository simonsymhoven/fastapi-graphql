from api.connection.db import meta
from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String

users = Table(
    "user",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(length=255)),
    Column("age", Integer),
    Column("email", String(length=255)),
    Column("password", String(length=255))
)
