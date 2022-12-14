import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL
from strawberry.extensions import Extension
from strawberry.tools import merge_types

from api.type.task import Mutation as TaskMutation
from api.type.task import Query as TaskQuery
from api.type.user import Mutation as UserMutation
from api.type.user import Query as UserQuery


router = APIRouter()
Query = merge_types("Query", (UserQuery, TaskQuery))
Mutation = merge_types("Mutation", (UserMutation, TaskMutation))

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

router.add_route("/graphql", graphql_app)
