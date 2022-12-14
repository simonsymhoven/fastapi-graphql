import uuid
import strawberry
from api.models import User as UserModel


@strawberry.type
class User:
    id: uuid.UUID
    name: str
    email: str

    @classmethod
    def from_instance(cls, instance: UserModel):
        return cls(
            id=instance.id,
            name=instance.name,
            email=instance.email
        )

