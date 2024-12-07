from typing import Optional

from .repository import GroupRepository, GroupStudentRepository
from .schemas import (
    GroupDTO,
    GroupAddDTO,
    GroupChangeDTO,
    GroupStudentDTO
)


class GroupService:
    @staticmethod
    async def get_items(session) -> list[GroupDTO]:
        items = await GroupRepository.get_items(
            session=session
        )
        return items

    @staticmethod
    async def get_item(
        session,  # : AsyncSession,
        id: int
    ) -> Optional[GroupDTO]:
        item = await GroupRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_item_by_name(
        session,  # : AsyncSession,
        name: str
    ) -> Optional[GroupDTO]:
        item = await GroupRepository.get_item_by_name(
            session=session,
            name=name
        )
        return item

    @staticmethod
    async def add_item(
        session,  # : AsyncSession,
        data: GroupAddDTO
    ) -> GroupDTO:
        data_dict = data.model_dump()
        item = await GroupRepository.add_item(
            session=session,
            data=data_dict
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: GroupChangeDTO
    ) -> GroupDTO:
        data_dict = data.model_dump()
        item_new = await GroupRepository.change_item(
            session=session,
            id=id,
            name=data_dict
        )
        return item_new

    @staticmethod
    async def delete_item(
        session,
        id: int,
    ):
        item = await GroupRepository.delete_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def delete_items_by_branch_id(
        session,
        branch_id: int
    ):
        item = await GroupRepository.delete_items_by_branch_id(
            session=session,
            branch_id=branch_id
        )
        return item


class GroupStudentService:
    @staticmethod
    async def get_items(
        session,
        group_id: int
    ) -> list[GroupStudentDTO]:
        items = await GroupStudentRepository.get_items(
            session=session,
            group_id=group_id
        )
        return items

    async def get_item_by_ids(
        session,
        group_id: int,
        student_id: int
    ) -> GroupStudentDTO:
        item = await GroupStudentRepository.get_items(
            session=session,
            group_id=group_id,
            student_id=student_id
        )
        return item

    @staticmethod
    async def add_item(
        session,  # : AsyncSession,
        group_id: int,
        student_id: int
    ) -> GroupStudentDTO:
        item = await GroupRepository.add_item(
            session=session,
            group_id=group_id,
            student_id=student_id
        )
        return item

    @staticmethod
    async def delete_item(
        session,
        group_id: int,
        student_id: int
    ):
        item = await GroupRepository.delete_item(
            session=session,
            group_id=group_id,
            student_id=student_id
        )
        return item
