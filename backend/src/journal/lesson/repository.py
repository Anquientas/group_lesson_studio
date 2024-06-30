from typing import Optional

from sqlalchemy import select

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


class LessonRepository:
    @classmethod
    async def get_items(
        cls,
        session,
        group_id: int
    ) -> list[Lesson]:
        query = select(Lesson).filter(
            # Lesson.status_id == 0,
            Lesson.group_id == group_id
        )
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def get_item(
        cls,
        session,  # : AsyncSession,
        id: int
    ) -> Lesson:
        query = select(Lesson).filter(
            Lesson.id == id
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def get_item_by_fields(
        cls,
        session,  # : AsyncSession,
        data: Lesson
    ) -> Lesson:
        query = select(Lesson).filter(
            Lesson.group_id == data.group_id,
            Lesson.room_id == data.room_id,
            Lesson.type_id == data.type_id,
            Lesson.date == data.date,
            Lesson.time_start == data.time_start
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def add_item(
        cls,
        session,  # : AsyncSession,
        data: Lesson
    ) -> Lesson:
        data_dict = data.model_dump()
        item = Lesson(**data_dict)
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def change_item(
        cls,
        session,  # : AsyncSession,
        id: int,
        data: Lesson
    ) -> Lesson:
        query = select(Lesson).filter(
            Lesson.id == id
        )
        result = await session.execute(query)
        item = result.scalars().one()
        if item.type_id and item.type_id != data.type_id:
            item.type_id = data.type_id
        if item.room_id and item.room_id != data.room_id:
            item.room_id = data.room_id
        if item.date and item.date != data.date:
            item.date = data.date
        if item.time_start and item.time_start != data.time_start:
            item.time_start = data.time_start
        if item.time_end and item.time_end != data.time_end:
            item.time_end = data.time_end
        if item.status and item.status != data.status:
            item.status = data.status
        await session.commit()
        return item


class LessonTypeRepository:
    @classmethod
    async def get_items(
        cls,
        session
    ) -> LessonType:
        query = select(LessonType)
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def add_item(
        cls,
        session,
        data: LessonType
    ) -> LessonType:
        data_dict = data.model_dump()
        item = LessonType(**data_dict)
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def get_item(
        cls,
        session,
        id: int
    ) -> LessonType:
        query = select(LessonType).filter(
            LessonType.id == id
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def get_item_by_fields(
        cls,
        session,
        data: LessonType
    ) -> LessonType:
        query = select(LessonType).filter(
            LessonType.name == data.name
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def change_item(
        cls,
        session,
        id: int,
        data: LessonType
    ) -> Optional[LessonType]:
        query = select(LessonType).filter(
            LessonType.id == id,
        )
        result = await session.execute(query)
        item = result.scalars().one()
        item.name = data.name
        await session.commit()
        return item


class LessonStudentRepository:
    @classmethod
    async def get_relations(
        cls,
        session,
        lesson_id: int,
    ):  # -> LessonStudent:
        query = select(LessonStudent).filter(
            LessonStudent.lesson_id == lesson_id
        )
        result = await session.execute(query)
        relations = result.scalars().one_or_none()
        return relations

    @classmethod
    async def get_relation(
        cls,
        session,
        lesson_id: int,
        student_id: int
    ):  # -> LessonStudent:
        query = select(LessonStudent).filter(
            LessonStudent.lesson_id == lesson_id,
            LessonStudent.student_id == student_id
        )
        result = await session.execute(query)
        relations = result.scalars().one_or_none()
        return relations

    @classmethod
    async def add_relation(
        cls,
        session,
        lesson_id: int,
        student_id: int
    ):  # -> LessonStudent:
        relation = LessonStudent(
            lesson_id=lesson_id,
            student_id=student_id
        )
        session.add(relation)
        await session.commit()
        return relation

    @classmethod
    async def delete_relation(
        cls,
        session,
        lesson_id: int,
        student_id: int
    ):  # -> LessonStudent:
        query = select(LessonStudent).filter(
            LessonStudent.student_id == student_id,
            LessonStudent.lesson_id == lesson_id
        )
        result = await session.execute(query)
        relation = result.scalars().one_or_none()
        relation.is_excluded = True
        await session.commit()
        return relation


class StudentVisitRepository:
    @classmethod
    async def get_items(
        cls,
        session
    ) -> list[StudentVisit]:
        query = select(StudentVisit)
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def get_item(
        cls,
        session,
        id: int
    ) -> StudentVisit:
        query = select(StudentVisit).filter(
            StudentVisit.id == id
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def get_item_by_fields(
        cls,
        session,
        data: StudentVisit
    ) -> StudentVisit:
        query = select(StudentVisit).filter(
            StudentVisit.type == data.type
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def add_item(
        cls,
        session,
        data: StudentVisit
    ) -> StudentVisit:
        data_dict = data.model_dump()
        item = StudentVisit(**data_dict)
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def change_item(
        cls,
        session,
        id: int,
        data: StudentVisit
    ) -> StudentVisit:
        query = select(StudentVisit).filter(
            StudentVisit.id == id
        )
        result = await session.execute(query)
        item = result.scalars().one()
        if data.type and item.type != data.type:
            item.type = data.type
            await session.commit()
        return item
