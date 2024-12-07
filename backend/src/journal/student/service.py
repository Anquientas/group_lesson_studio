from typing import Optional

from .repository import StudentRepository
from .schemas import (
    StudentDTO,
    StudentAddDTO,
    StudentChangeDTO
)


class StudentService:
    @staticmethod
    async def get_items(session) -> list[StudentDTO]:
        items = await StudentRepository.get_items(
            session=session
        )
        return items

    @staticmethod
    async def get_item(
        session,  # : AsyncSession,
        id: int
    ) -> Optional[StudentDTO]:
        item = await StudentRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_items_by_name(
        session,  # : AsyncSession,
        data: StudentAddDTO
    ) -> Optional[StudentDTO]:
        items = await StudentRepository.get_items_by_name(
            session=session,
            name=data.name
        )
        return items

    @staticmethod
    async def add_item(
        session,  # : AsyncSession,
        data: StudentAddDTO
    ) -> StudentDTO:
        data_dict = data.model_dump()
        item = await StudentRepository.add_item(
            session=session,
            data=data_dict
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: StudentChangeDTO
    ) -> StudentDTO:
        data_dict = data.model_dump()
        item_new = await StudentRepository.change_item(
            session=session,
            id=id,
            data=data_dict
        )
        return item_new

    @staticmethod
    async def delete_item(
        session,
        id: int,
    ):
        item = await StudentRepository.delete_item(
            session=session,
            id=id
        )
        return item
