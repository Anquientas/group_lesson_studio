from typing import Optional

from .repository import EmployeeRepository, RoleRepository
from .schemas import (
    EmployeeDTO,
    EmployeeAddDTO,
    EmployeeChangeDTO,
    RoleDTO,
    RoleAddDTO,
    RoleChangeDTO
)


class EmployeeService:
    @staticmethod
    async def get_items(session) -> list[EmployeeDTO]:
        items = await EmployeeRepository.get_items(
            session=session
        )
        return items

    @staticmethod
    async def get_item(
        session,  # : AsyncSession,
        id: int
    ) -> Optional[EmployeeDTO]:
        item = await EmployeeRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_items_by_role(
        session,  # : AsyncSession,
        role_id: int
    ) -> Optional[EmployeeDTO]:
        items = await EmployeeRepository.get_items_by_role(
            session=session,
            role_id=role_id
        )
        return items

    @staticmethod
    async def add_item(
        session,  # : AsyncSession,
        data: EmployeeAddDTO
    ) -> EmployeeDTO:
        data_dict = data.model_dump()
        item = await EmployeeRepository.add_item(
            session=session,
            data=data_dict
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: EmployeeChangeDTO
    ) -> EmployeeDTO:
        data_dict = data.model_dump()
        item_new = await EmployeeRepository.change_item(
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
        item = await EmployeeRepository.delete_item(
            session=session,
            id=id
        )
        return item


class RoleService:
    @staticmethod
    async def get_items(session) -> list[RoleDTO]:
        items = await RoleRepository.get_items(
            session=session
        )
        return items

    @staticmethod
    async def get_item(
        session,  # : AsyncSession,
        id: int
    ) -> Optional[RoleDTO]:
        item = await RoleRepository.get_item(
            session=session,
            id=id
        )
        return item

    @staticmethod
    async def get_item_by_name(
        session,  # : AsyncSession,
        data: RoleAddDTO
    ) -> Optional[RoleDTO]:
        item = await RoleRepository.get_item_by_name(
            session=session,
            name=data.name
        )
        return item

    @staticmethod
    async def add_item(
        session,  # : AsyncSession,
        data: RoleAddDTO
    ) -> RoleDTO:
        data_dict = data.model_dump()
        item = await RoleRepository.add_item(
            session=session,
            data=data_dict
        )
        return item

    @staticmethod
    async def change_item(
        session,
        id: int,
        data: RoleChangeDTO
    ) -> RoleDTO:
        data_dict = data.model_dump()
        item_new = await RoleRepository.change_item(
            session=session,
            id=id,
            data=data_dict
        )
        return item_new
