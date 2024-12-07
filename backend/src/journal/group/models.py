from datetime import datetime

from sqlalchemy import ForeignKey, String, text, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Model


class Group(Model):
    __tablename__ = 'group'

    id: Mapped[int] = mapped_column(primary_key=True)
    branch_id: Mapped[int] = mapped_column(ForeignKey('branch.id'))
    teacher_id: Mapped[int] = mapped_column(ForeignKey('employee.id'))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age_min: Mapped[int]
    age_max: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        # server_default=text('TIMEZONE("utc", now())')
        server_default=func.now()
    )
    is_active: Mapped[bool] = mapped_column(default=True)


class GroupStudent(Model):
    __tablename__ = 'group_student'

    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'))
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'))
    is_excluded: Mapped[bool] = mapped_column(default=False)
