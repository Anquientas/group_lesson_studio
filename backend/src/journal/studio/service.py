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
        """
        Метод получения списка студий.
        """

        items = await StudioRepository.get_items(
            session=session
        )
        return items

    @staticmethod
    async def get_item(
        session,  # : AsyncSession,
        id: int
    ) -> Optional[StudioDTO]:
        """
        Метод получения студии.
        """

        item = await StudioRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_item_by_name(
        session,  # : AsyncSession,
        name: str
    ) -> Optional[StudioDTO]:
        """
        Метод получения студии по имени.
        """
        item = await StudioRepository.get_item_by_name(
            session=session,
            name=name
        )
        return item

    @staticmethod
    async def add_item(
        session,  # : AsyncSession,
        data: StudioAddDTO
    ) -> StudioDTO:
        """
        Метод добавления студии.
        """

        data_dict = data.model_dump()
        item = await StudioRepository.add_item(
            session=session,
            data=data_dict
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: StudioChangeDTO
    ) -> StudioDTO:
        """
        Метод изменения сведений о студии.
        """

        item_new = await StudioRepository.change_item(
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
        """
        Метод удаления студии.
        Предварительное удаление филиалов.
        """

        await BranchService.delete_items_by_studio_id(
            session=session,
            studio_id=id
        )
        # for item_dependent_id in item_dependent_ids:
        #     BranchService.delete_item(
        #         session=session,
        #         id=item_dependent_id
        #     )
        item = await StudioRepository.delete_item(
            session=session,
            id=id
        )
        return item
