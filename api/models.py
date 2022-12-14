from sqlalchemy.orm import declarative_base
import uuid as uuid_pkg

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from api.connection.db import Base


class User(Base):
    __tablename__ = "users"
    id: uuid_pkg.UUID = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid_pkg.uuid4)
    name: str = Column(String, nullable=False, unique=True)
    email: str = Column(String, nullable=False, unique=True)


class Task(Base):
    __tablename__ = "tasks"
    id: uuid_pkg.UUID = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid_pkg.uuid4())
    title: str = Column(String(64))

    user_id: uuid_pkg.UUID = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user: User = relationship("User")
