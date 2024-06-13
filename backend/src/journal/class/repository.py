from typing import Optional
from sqlalchemy import func, select

from database import new_async_session

from ..exceptions import ObjectNotFoundException
from .models import Class, ClassStudent
from .schemas import (
    ClassAddDTO,
    ClassDTO,
    ClassChangeDTO,
    ClassStudentAddDTO
)


class ClassRepository:
    @classmethod
    async def add_class(cls, data: ClassAddDTO) -> ClassDTO:
        async with new_async_session() as session:
            group_dict = data.model_dump()
            group = Class(**group_dict)
            session.add(group)
            await session.commit()
            return group

    @classmethod
    async def get_classes(cls) -> list[ClassDTO]:
        async with new_async_session() as session:
            query = select(Class).filter(
                Class.is_active
            )
            result = await session.execute(query)
            classes = result.scalars().all()
            return classes

    @classmethod
    async def get_class(cls, class_id: int) -> Optional[ClassDTO]:
        async with new_async_session() as session:
            query = select(Class).filter(
                Class.id == class_id,
                Class.is_active
            )
            result = await session.execute(query)
            group = result.scalars().one_or_none()
            return group

    @classmethod
    async def change_class(
        cls,
        class_id: int,
        data: ClassChangeDTO
    ) -> Optional[ClassDTO]:
        async with new_async_session() as session:
            query = select(Class).filter(
                Class.id == class_id,
                Class.is_active
            )
            result = await session.execute(query)
            group = result.scalars().one()
            group.name = data.name
            group.teacher_id = data.teacher_id
            group.age_min = data.age_min
            group.age_max = data.age_max
            await session.commit()
            return group

    @classmethod
    async def delete_class(cls, class_id: int):
        async with new_async_session() as session:
            query = select(Class).filter(
                Class.id == class_id,
                Class.is_active
            )
            result = await session.execute(query)
            group = result.scalars().one_or_none()
            if not group:
                raise ObjectNotFoundException
            group.is_active = False
            await session.commit()
            return group


class ClassStudentRepository:
    @classmethod
    async def add_student_in_class(cls, data: ClassStudentAddDTO):  # -> ClassDTO:
        async with new_async_session() as session:
            class_student_dict = data.model_dump()
            class_student = ClassStudent(**class_student_dict)
            session.add(class_student)
            await session.commit()
            return class_student

    @classmethod
    async def excluded_student_from_class(
        cls,
        class_id: int,
        student_id: int
    ):  # -> ClassDTO:
        async with new_async_session() as session:
            query = select(ClassStudent).filter(
                ClassStudent.student_id == student_id,
                ClassStudent.class_id == class_id
            )
            result = await session.execute(query)
            row = result.scalars().one_or_none()
            row.is_excluded = True
            await session.commit()
            return row

    async def get_students_in_class(cls, class_id: int) -> list[int]:
        async with new_async_session() as session:
            query = select(ClassStudent.student_id).filter(
                ClassStudent.class_id == class_id
            )
            result = await session.execute(query)
            students = result.scalars().all()
            return students
