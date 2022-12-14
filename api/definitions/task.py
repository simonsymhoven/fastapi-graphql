import uuid
import strawberry

from api.definitions.user import User
from api.models import Task as TaskModel


@strawberry.type
class Task:
    id: uuid.UUID
    title: str

    instance: strawberry.Private[TaskModel]

    @strawberry.field
    def user(self) -> User:
        return User.from_instance(self.instance.user)

    @classmethod
    def from_instance(cls, instance: TaskModel):
        return cls(
            instance=instance,
            id=instance.id,
            title=instance.title
        )