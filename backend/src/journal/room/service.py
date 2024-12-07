from typing import Optional

from .repository import RoomRepository
from .schemas import (
    RoomDTO,
    RoomAddDTO,
    RoomChangeDTO
)


class RoomService:
    @staticmethod
    async def get_items(session) -> list[RoomDTO]:
        items = await RoomRepository.get_items(
            session=session
        )
        return items

    @staticmethod
    async def get_item(
        session,  # : AsyncSession,
        id: int
    ) -> Optional[RoomDTO]:
        item = await RoomRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_item_by_name(
        session,  # : AsyncSession,
        name: str
    ) -> Optional[RoomDTO]:
        item = await RoomRepository.get_item_by_name(
            session=session,
            name=name
        )
        return item

    @staticmethod
    async def add_item(
        session,  # : AsyncSession,
        data: RoomAddDTO
    ) -> RoomDTO:
        data_dict = data.model_dump()
        item = await RoomRepository.add_item(
            session=session,
            data=data_dict
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: RoomChangeDTO
    ) -> RoomDTO:
        item_new = await RoomRepository.change_item(
            session=session,
            id=id,
            name=data.name
        )
        return item_new

    @staticmethod
    async def delete_item(
        session,
        id: int,
    ):
        item = await RoomRepository.delete_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def delete_items_by_branch_id(
        session,
        branch_id: int,
    ):
        item = await RoomRepository.delete_items_by_branch_id(
            session=session,
            branch_id=branch_id
        )
        return item
