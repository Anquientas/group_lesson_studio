from datetime import datetime, date, time
import enum

from sqlalchemy import ForeignKey, String, TIME, DATE, text, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Model


class LessonStatus(enum.Enum):
    plan = 'plan'
    over = 'over'
    confirmation = 'confirmation'


class LessonType(Model):
    __tablename__ = 'lesson_type'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)


class Lesson(Model):
    __tablename__ = 'lesson'

    id: Mapped[int] = mapped_column(primary_key=True)
    type_id: Mapped[int] = mapped_column(ForeignKey('lesson_type.id'))
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'))
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))
    date: Mapped[date]
    time_start: Mapped[time]
    time_end: Mapped[time]
    created_at:  Mapped[datetime] = mapped_column(
        # server_default=text('TIMEZONE("utc", now())')
        server_default=func.now()
    )
    status: Mapped[LessonStatus]


class StudentVisit(Model):
    __tablename__ = 'student_visit'

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(50), nullable=False)


class LessonStudent(Model):
    __tablename__ = 'lesson_student'

    id: Mapped[int] = mapped_column(primary_key=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey('lesson.id'))
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'))
    visit_id: Mapped[int] = mapped_column(ForeignKey('student_visit.id'))
    added_at:  Mapped[datetime] = mapped_column(
        # server_default=text('TIMEZONE("utc", now())')
        server_default=func.now()
    )
    exclusion: Mapped[bool]
