import typing
import uuid

import strawberry
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import joinedload

import api
from api.connection.db import connection
from api.definitions.task import Task


@strawberry.type
class Query:
    @strawberry.field
    def task(self, id: uuid.UUID) -> Task:
        query = select(api.models.Task).where(api.models.Task.id == id).options(joinedload(api.models.Task.user))
        task = connection.execute(query).unique().scalar()
        print(task)
        return Task.from_instance(task)

    @strawberry.field
    def tasks(self) -> typing.List[Task]:
        query = select(api.models.Task).options(joinedload(api.models.Task.user))
        tasks = connection.execute(query).all()
        [print(task) for task in tasks]
        return [Task.from_instance(task) for task in tasks]


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_task(
        self, title: str, user_id: uuid.UUID
    ) -> uuid.UUID:
        task = {"title": title, "user_id": user_id}
        result = connection.execute(insert(api.models.Task), task)
        return result.inserted_primary_key[0]

    @strawberry.mutation
    def update_task(
        self, id: uuid.UUID, title: str, user: uuid.UUID
    ) -> str:
        result = connection.execute(
            update(api.models.Task).where(api.models.Task.id == id),
            {"title": title, "user": user},
        )
        return str(result.rowcount) + " Row(s) updated"

    @strawberry.mutation
    def delete_task(self, id: uuid.UUID) -> bool:
        result = connection.execute(delete(Task).where(api.models.Task.id == id))
        return result.rowcount > 0



