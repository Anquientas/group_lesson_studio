from typing import Optional
from sqlalchemy import select

from database import new_async_session

from ..exceptions import ObjectNotFoundException
from .models import Lesson, LessonStudent, LessonType, StudentVisit
from .schemas import (
    LessonAddDTO,
    LessonDTO,
    LessonChangeDTO,
    LessonStudentAddDTO,
    LessonTypeAddDTO,
    LessonTypeDTO,
    LessonTypeChangeDTO,
    StudentVisitAddDTO,
    StudentVisitDTO,
    StudentVisitChangeDTO
)


class LessonTypeRepository:
    @classmethod
    async def add_lesson_type(cls, data: LessonTypeAddDTO) -> LessonTypeDTO:
        async with new_async_session() as session:
            lesson_type_dict = data.model_dump()
            lesson_type = LessonType(**lesson_type_dict)
            session.add(lesson_type)
            await session.commit()
            return lesson_type

    @classmethod
    async def get_lesson_types(cls) -> list[LessonTypeDTO]:
        async with new_async_session() as session:
            query = select(LessonType)
            result = await session.execute(query)
            lesson_types = result.scalars().all()
            return lesson_types

    @classmethod
    async def get_lesson_type(cls, lesson_type_id: int) -> LessonTypeDTO:
        async with new_async_session() as session:
            query = select(LessonType).filter(
                LessonType.id == lesson_type_id
            )
            result = await session.execute(query)
            lesson_type = result.scalars().one_or_none()
            return lesson_type

    @classmethod
    async def change_lesson_type(
        cls,
        lesson_type_id: int,
        data: LessonTypeChangeDTO
    ) -> Optional[LessonTypeDTO]:
        async with new_async_session() as session:
            query = select(LessonType).filter(
                LessonType.id == lesson_type_id,
            )
            result = await session.execute(query)
            lesson_type = result.scalars().one()
            lesson_type.name = data.name
            await session.commit()
            return lesson_type


class StudentVisitRepository:
    @classmethod
    async def add_student_visit(
        cls,
        data: StudentVisitAddDTO
    ) -> StudentVisitDTO:
        async with new_async_session() as session:
            student_visit_dict = data.model_dump()
            student_visit = StudentVisit(**student_visit_dict)
            session.add(student_visit)
            await session.commit()
            return student_visit

    @classmethod
    async def get_student_visits(cls) -> list[StudentVisitDTO]:
        async with new_async_session() as session:
            query = select(StudentVisit)
            result = await session.execute(query)
            student_visit = result.scalars().all()
            return student_visit

    @classmethod
    async def get_student_visit(
        cls,
        student_visit_id: int
    ) -> StudentVisitDTO:
        async with new_async_session() as session:
            query = select(StudentVisit).filter(
                StudentVisit.id == student_visit_id
            )
            result = await session.execute(query)
            student_visit = result.scalars().one_or_none()
            return student_visit

    @classmethod
    async def change_student_visit(
        cls,
        student_visit_id: int,
        data: StudentVisitChangeDTO
    ) -> StudentVisitDTO:
        async with new_async_session() as session:
            query = select(StudentVisit).filter(
                StudentVisit.id == student_visit_id,
            )
            result = await session.execute(query)
            student_visit = result.scalars().one()
            student_visit.type = data.type
            await session.commit()
            return student_visit


class LessonRepository:
    @classmethod
    async def add_lesson(cls, data: LessonAddDTO) -> LessonDTO:
        async with new_async_session() as session:
            lesson_dict = data.model_dump()
            lesson = Lesson(**lesson_dict)
            session.add(lesson)
            await session.commit()
            return lesson

    @classmethod
    async def get_lessons(cls, group_id: int) -> list[LessonDTO]:
        async with new_async_session() as session:
            query = select(Lesson).filter(
                Lesson.status_id == 0,
                Lesson.group_id == group_id
            )
            result = await session.execute(query)
            lessons = result.scalars().all()
            return lessons

    @classmethod
    async def get_lesson(cls, lesson_id: int) -> LessonDTO:
        async with new_async_session() as session:
            query = select(Lesson).filter(
                Lesson.id == lesson_id
            )
            result = await session.execute(query)
            lesson = result.scalars().one_or_none()
            return lesson

    @classmethod
    async def change_lesson(
        cls,
        lesson_id: int,
        data: LessonChangeDTO
    ) -> LessonDTO:
        async with new_async_session() as session:
            query = select(Lesson).filter(
                Lesson.id == lesson_id
            )
            result = await session.execute(query)
            lesson = result.scalars().one()
            lesson.type_id = data.type_id
            lesson.room_id = data.room_id
            lesson.date = data.date
            lesson.time_start = data.time_start
            lesson.time_end = data.time_end
            lesson.status = data.status
            await session.commit()
            return lesson


class LessonStudentRepository:
    @classmethod
    async def add_student_in_lesson(
        cls,
        data: LessonStudentAddDTO
    ):  # -> LessonStudentDTO:
        async with new_async_session() as session:
            lesson_student_dict = data.model_dump()
            lesson_student = LessonStudent(**lesson_student_dict)
            session.add(lesson_student)
            await session.commit()
            return lesson_student

    @classmethod
    async def excluded_student_from_lesson(
        cls,
        lesson_id: int,
        student_id: int
    ):  # -> LessonStudentDTO:
        async with new_async_session() as session:
            query = select(LessonStudent).filter(
                LessonStudent.student_id == student_id,
                LessonStudent.lesson_id == lesson_id
            )
            result = await session.execute(query)
            row = result.scalars().one_or_none()
            row.is_excluded = True
            await session.commit()
            return row

    async def get_students_lesson(cls, lesson_id: int) -> list[int]:
        async with new_async_session() as session:
            query = select(LessonStudent.student_id).filter(
                LessonStudent.lesson_id == lesson_id
            )
            result = await session.execute(query)
            students = result.scalars().all()
            return students
