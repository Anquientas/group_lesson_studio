from sqlalchemy import String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from database import Model
from ..stuff.models import Gender


class Student(Model):
    __tablename__ = 'stuff'

    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50))
    gender: Mapped[Gender]
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(150))
    created_at: Mapped[TIMESTAMP]
    changed_at: Mapped[TIMESTAMP]
    is_active: Mapped[bool] = mapped_column(default=True)
