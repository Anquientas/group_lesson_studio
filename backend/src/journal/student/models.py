from datetime import datetime

from sqlalchemy import String, text, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Model
from ..employee.models import Gender


class Student(Model):
    __tablename__ = 'student'

    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50))
    gender: Mapped[Gender]
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(150))
    created_at:  Mapped[datetime] = mapped_column(
        # server_default=text('TIMEZONE("utc", now())')
        server_default=func.now()
    )
    is_active: Mapped[bool] = mapped_column(default=True)
