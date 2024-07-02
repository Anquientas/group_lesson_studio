from typing import Optional

from .repository import StudioRepository
from .schemas import (
    StudioDTO,
    StudioAddDTO,
    StudioChangeDTO
)
from ..branch.service import BranchService


class StudioService:
    @staticmethod
    async def get_items(session) -> list[StudioDTO]:
        items = await StudioRepository.get_items(
            session=session
        )
        return items

    @staticmethod
    async def get_item(
        session,  # : AsyncSession,
        id: int
    ) -> Optional[StudioDTO]:
        item = await StudioRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_item_by_fields(
        session,  # : AsyncSession,
        data: StudioAddDTO
    ) -> Optional[StudioDTO]:
        item = await StudioRepository.get_item_by_fields(
            session=session,
            data=data
        )
        return item

    @staticmethod
    async def add_item(
        session,  # : AsyncSession,
        data: StudioAddDTO
    ) -> StudioDTO:
        item = await StudioRepository.add_item(
            session=session,
            data=data
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: StudioChangeDTO
    ) -> StudioDTO:
        item_new = await StudioRepository.change_item(
            session=session,
            id=id,
            data=data
        )
        return item_new

    @staticmethod
    async def delete_item(
        session,
        id: int,
    ):
        item_dependent_ids = await BranchService.get_item_ids(
            session=session,
            id=id
        )
        for item_dependent_id in item_dependent_ids:
            BranchService.delete_item(
                session=session,
                id=item_dependent_id
            )
        item = await StudioRepository.delete_item(
            session=session,
            id=id
        )
        return item
