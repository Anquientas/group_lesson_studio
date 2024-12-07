from typing import Optional

from ..room.service import RoomService
from ..group.service import GroupService
from .repository import BranchRepository
from .schemas import (
    BranchDTO,
    BranchAddDTO,
    BranchChangeDTO
)


class BranchService:
    @staticmethod
    async def get_items(session) -> list[BranchDTO]:
        items = await BranchRepository.get_items(
            session=session
        )
        return items

    @staticmethod
    async def get_item(
        session,  # : AsyncSession,
        id: int
    ) -> Optional[BranchDTO]:
        item = await BranchRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_item_by_name(
        session,  # : AsyncSession,
        studio_id: int,
        name: str
    ) -> Optional[BranchDTO]:
        item = await BranchRepository.get_item_by_name(
            session=session,
            studio_id=studio_id,
            name=name
        )
        return item

    @staticmethod
    async def add_item(
        session,  # : AsyncSession,
        data: BranchAddDTO
    ) -> BranchDTO:
        data_dict = data.model_dump()
        item = await BranchRepository.add_item(
            session=session,
            data=data_dict
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: BranchChangeDTO
    ) -> BranchDTO:
        item_new = await BranchRepository.change_item(
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
        await RoomService.delete_items_by_branch_id(
            session=session,
            branch_id=id
        )
        await GroupService.delete_items_by_branch_id(
            session=session,
            branch_id=id
        )
        item = await BranchRepository.delete_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def delete_items_by_studio_id(
        session,
        studio_id: int,
    ):
        items = await BranchRepository.delete_items_by_studio_id(
            session=session,
            studio_id=studio_id
        )
        return items
