from datetime import datetime
import enum

from sqlalchemy import ForeignKey, String, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column

from database import Model


class Gender(enum.Enum):
    male = 'male'
    female = 'female'


class Role(Model):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(String(50))


class Stuff(Model):
    __tablename__ = 'stuff'

    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50))
    gender: Mapped[Gender]
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(150))
    role_id: Mapped[int] = mapped_column(ForeignKey('role.id'))
    created_at:  Mapped[datetime] = mapped_column(
        server_default=text('TIMEZONE("utc", now())')
    )
    changed_at: Mapped[TIMESTAMP]
    is_active: Mapped[bool] = mapped_column(default=True)
