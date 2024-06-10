from datetime import datetime

from sqlalchemy import ForeignKey, String, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column

from database import Model


class Class(Model):
    __tablename__ = 'class'

    id: Mapped[int] = mapped_column(primary_key=True)
    branch_id: Mapped[int] = mapped_column(ForeignKey('branch.id'))
    teacher_id: Mapped[int] = mapped_column(ForeignKey('stuff.id'))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age_min: Mapped[int]
    age_max: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        server_default=text('TIMEZONE("utc", now())')
    )
    is_active: Mapped[bool] = mapped_column(default=True)


class ClassStudent(Model):
    __tablename__ = 'class_student'

    id: Mapped[int] = mapped_column(primary_key=True)
    class_id: Mapped[int] = mapped_column(ForeignKey('class.id'))
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'))
    added_at: Mapped[datetime] = mapped_column(
        server_default=text('TIMEZONE("utc", now())')
    )
    excluded_at: Mapped[TIMESTAMP]
