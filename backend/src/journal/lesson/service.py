from typing import Optional

from .repository import (
    LessonRepository,
    LessonStudentRepository,
    LessonTypeRepository,
    StudentVisitRepository
)
from .schemas import (
    LessonDTO,
    LessonAddDTO,
    LessonChangeDTO,
    LessonStudentAddDTO,
    LessonStudentChangeDTO,
    LessonStudentDTO,
    LessonTypeDTO,
    LessonTypeAddDTO,
    LessonTypeChangeDTO,
    StudentVisitDTO,
    StudentVisitAddDTO,
    StudentVisitChangeDTO
)


class LessonService:
    @staticmethod
    async def get_items(session) -> list[LessonDTO]:
        items = await LessonRepository.get_items(session=session)
        return items

    @staticmethod
    async def get_item(
        session,  # : AsyncSession,
        id: int
    ) -> LessonDTO:
        item = await LessonRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_item_by_fields(
        session,  # : AsyncSession,
        data: LessonDTO
    ) -> LessonDTO:
        item = await LessonRepository.get_item_by_fields(
            session=session,
            data=data
        )
        return item

    @staticmethod
    async def add_item(
        session,  # : AsyncSession,
        data: LessonAddDTO
    ) -> LessonDTO:
        item = await LessonRepository.add_item(
            session=session,
            data=data
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: LessonChangeDTO
    ) -> LessonDTO:
        item_new = await LessonRepository.change_item(
            session=session,
            id=id,
            data=data
        )
        return item_new


class LessonTypeService:
    @staticmethod
    async def get_items(session) -> list[LessonTypeDTO]:
        items = await LessonTypeRepository.get_items(
            session=session
        )
        return items

    @staticmethod
    async def add_item(
        session,
        data: LessonTypeAddDTO
    ) -> LessonTypeDTO:
        item = await LessonTypeRepository.add_item(
            session=session,
            data=data
        )
        return item

    @staticmethod
    async def get_item(
        session,
        id: int
    ) -> Optional[LessonTypeDTO]:
        item = await LessonTypeRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_item_by_fields(
        session,
        data: LessonTypeAddDTO
    ) -> Optional[LessonTypeDTO]:
        item = await LessonTypeRepository.get_item_by_fields(
            session=session,
            data=data
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: LessonTypeChangeDTO
    ) -> LessonTypeDTO:
        item = await LessonTypeRepository.change_item(
            session=session,
            id=id,
            data=data
        )
        return item


class LessonStudentService:
    @staticmethod
    async def get_relations(
        session,
        id_lesson: int,
    ):
        relations = await LessonStudentRepository.get_relations(
            session=session,
            id_lesson=id_lesson,
        )
        return relations

    @staticmethod
    async def get_relation(
        session,
        id_lesson: int,
        id_student: int,
    ):
        relation = await LessonStudentRepository.get_relation(
            session=session,
            id_lesson=id_lesson,
            id_student=id_student
        )
        return relation

    @staticmethod
    async def add_relation(
        session,
        id_lesson: int,
        id_student: int,
    ):
        relation = await LessonStudentRepository.add_relation(
            session=session,
            id_lesson=id_lesson,
            id_student=id_student
        )
        return relation

    @staticmethod
    async def delete_relation(
        session,
        id_lesson: int,
        id_student: int,
    ):
        relation = await LessonStudentRepository.delete_relation(
            session=session,
            id_lesson=id_lesson,
            id_student=id_student
        )
        return relation


class StudentVisitService:
    @staticmethod
    async def get_items(session) -> list[StudentVisitDTO]:
        items = await StudentVisitRepository.get_items(
            session=session
        )
        return items

    @staticmethod
    async def get_item(
        session,
        id: int
    ) -> LessonTypeDTO:
        item = await StudentVisitRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_item_by_fields(
        session,
        data: LessonTypeAddDTO
    ) -> LessonTypeDTO:
        item = await StudentVisitRepository.get_item_by_fields(
            session=session,
            data=data
        )
        return item

    @staticmethod
    async def add_item(
        session,
        data: StudentVisitAddDTO
    ) -> StudentVisitDTO:
        item = await StudentVisitRepository.add_item(
            session=session,
            data=data
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: StudentVisitChangeDTO
    ) -> LessonTypeDTO:
        item = await StudentVisitRepository.change_item(
            session=session,
            id=id,
            data=data
        )
        return item
