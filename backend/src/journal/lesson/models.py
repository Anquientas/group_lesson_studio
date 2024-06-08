import enum

from sqlalchemy import ForeignKey, String, TIMESTAMP, TIME, DATE
from sqlalchemy.orm import Mapped, mapped_column

from database import Model


class LessonStatus(enum.Enum):
    plan = 'plan'
    over = 'over'
    confirmation = 'confirmation'


class LessonType(Model):
    __tablename__ = 'lesson_type'

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(100), nullable=False)


class Lesson(Model):
    __tablename__ = 'lesson'

    id: Mapped[int] = mapped_column(primary_key=True)
    type_id: Mapped[int] = mapped_column(ForeignKey('type.id'))
    class_id: Mapped[int] = mapped_column(ForeignKey('class.id'))
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))
    date: Mapped[DATE]
    time_start: Mapped[TIME]
    time_end: Mapped[TIME]
    created_at: Mapped[TIMESTAMP]
    changed_at: Mapped[TIMESTAMP]
    status_id: Mapped[LessonStatus]


class StudentVisit(Model):
    __tablename__ = 'student_visit'

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(50), nullable=False)


class LessonStudent(Model):
    __tablename__ = 'lesson_student'

    id: Mapped[int] = mapped_column(primary_key=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey('lesson.id'))
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'))
    visit_id: Mapped[int] = mapped_column(ForeignKey('visit.id'))
    added_at: Mapped[TIMESTAMP]
    excluded_at: Mapped[TIMESTAMP]
