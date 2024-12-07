from typing import Optional
from sqlalchemy import select

from .models import Employee, Role


class EmployeeRepository:
    @classmethod
    async def get_items(
        cls,
        session
    ) -> list[Employee]:
        query = select(Employee).filter(Employee.is_active)
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def get_item(
        cls,
        session,
        id: int
    ) -> Optional[Employee]:
        query = select(Employee).filter(
            Employee.id == id,
            Employee.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def get_items_by_role(
        cls,
        session,
        role_id: int
    ) -> Optional[Employee]:
        query = select(Employee).filter(
            Employee.role_id == role_id,
            Employee.is_active
        )
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def add_item(
        cls,
        session,
        data: dict
    ) -> Employee:
        item = Employee(**data)
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def change_item(
        cls,
        session,
        id: int,
        data: dict
    ) -> Optional[Employee]:
        query = select(Employee).filter(
            Employee.id == id,
            Employee.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one()
        if data['surname'] and item.surname != data['surname']:
            item.surname = data['surname']
        if data['first_name'] and item.first_name != data['first_name']:
            item.first_name = data['first_name']
        if data['last_name'] and item.last_name != data['last_name']:
            item.last_name = data['last_name']
        if data['gender'] and item.gender != data['gender']:
            item.gender = data['gender']
        if data['phone'] and item.phone != data['phone']:
            item.phone = data['phone']
        if data['email'] and item.email != data['email']:
            item.email = data['email']
        if data['role_id'] and item.role_id != data['role_id']:
            item.role_id = data['role_id']
        await session.commit()
        return item

    @classmethod
    async def delete_item(
        cls,
        session,
        id: int
    ):
        query = select(Employee).filter(
            Employee.id == id,
            Employee.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        item.is_active = False
        await session.commit()
        return item


class RoleRepository:
    @classmethod
    async def get_items(
        cls,
        session
    ) -> list[Role]:
        query = select(Role)
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def get_item(
        cls,
        session,
        id: int
    ) -> Optional[Role]:
        query = select(Role).filter(
            Role.id == id
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def get_items_by_name(
        cls,
        session,
        name: str
    ) -> Optional[Role]:
        query = select(Role).filter(
            Role.name == name
        )
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def add_item(
        cls,
        session,
        data: dict
    ) -> Role:
        item = Role(**data)
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def change_item(
        cls,
        session,
        id: int,
        data: dict
    ) -> Optional[Role]:
        query = select(Role).filter(
            Role.id == id
        )
        result = await session.execute(query)
        item = result.scalars().one()
        if data['name'] and item.name != data['name']:
            item.name = data['name']
        await session.commit()
        return item
