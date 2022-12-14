import typing
import uuid

import strawberry
from sqlalchemy import select, insert, update, delete

import api
from api.connection.db import connection
from api.definitions.user import User


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: uuid.UUID) -> User:
        return connection.execute(select(api.models.User).where(api.models.User.id == id)).fetchone()

    @strawberry.field
    def users(self) -> typing.List[User]:
        return connection.execute(select(api.models.User)).fetchall()


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(
        self, name: str, email: str
    ) -> uuid.UUID:
        user = {"name": name, "email": email}
        result = connection.execute(insert(api.models.User), user)
        return result.inserted_primary_key[0]

    @strawberry.mutation
    def update_user(
        self, id: uuid.UUID, name: str, email: str
    ) -> str:
        result = connection.execute(
            update(api.models.User).where(api.models.User.id == id),
            {"name": name, "email": email},
        )
        return str(result.rowcount) + " Row(s) updated"

    @strawberry.mutation
    def delete_user(self, id: uuid.UUID) -> bool:
        result = connection.execute(delete(api.models.User).where(api.models.User.id == id))
        return result.rowcount > 0



