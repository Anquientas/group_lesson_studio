from typing import Optional

from sqlalchemy import func, select

from .models import Student


class StudentRepository:
    @classmethod
    async def get_items(
        cls,
        session
    ) -> list[Student]:
        query = select(Student).filter(Student.is_active)
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def get_item(
        cls,
        session,
        id: int
    ) -> Optional[Student]:
        query = select(Student).filter(
            Student.id == id,
            Student.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def get_items_by_name(
        cls,
        session,
        name: str
    ) -> Optional[Student]:
        query = select(Student).filter(
            Student.name == name,
            Student.is_active
        )
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def add_item(
        cls,
        session,
        data: dict
    ) -> Student:
        item = Student(**data)
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def change_item(
        cls,
        session,
        id: int,
        data: dict
    ) -> Optional[Student]:
        query = select(Student).filter(
            Student.id == id,
            Student.is_active
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
        await session.commit()
        return item

    @classmethod
    async def delete_item(
        cls,
        session,
        id: int
    ):
        query = select(Student).filter(
            Student.id == id,
            Student.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        item.is_active = False
        await session.commit()
        return item

    @classmethod
    async def reactive_item(
        cls,
        session,
        id: int
    ):
        query = select(Student).filter(
            Student.id == id,
            not Student.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        item.is_active = True
        await session.commit()
        return item
