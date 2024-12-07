from typing import Optional
from sqlalchemy import select

from .models import Room


class RoomRepository:
    @classmethod
    async def get_items(
        cls,
        session
    ) -> list[Room]:
        query = select(Room).filter(Room.is_active)
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def get_item(
        cls,
        session,
        id: int
    ) -> Optional[Room]:
        query = select(Room).filter(
            Room.id == id,
            Room.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def get_item_by_name(
        cls,
        session,
        name: str
    ) -> Optional[Room]:
        query = select(Room).filter(
            Room.name == name,
            Room.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def add_item(
        cls,
        session,
        data: dict
    ) -> Room:
        item = Room(**data)
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def change_item(
        cls,
        session,
        id: int,
        name: str
    ) -> Optional[Room]:
        query = select(Room).filter(
            Room.id == id,
            Room.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one()
        if name and item.name != name:
            item.name = name
        await session.commit()
        return item

    @classmethod
    async def delete_item(
        cls,
        session,
        id: int
    ):
        query = select(Room).filter(
            Room.id == id,
            Room.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        item.is_active = False
        await session.commit()
        return item

    @classmethod
    async def delete_items_by_branch_id(
        cls,
        session,
        branch_id: int,
    ):
        query = select(Room).filter(
            Room.branch_id == branch_id,
            Room.is_active
        )
        result = await session.execute(query)
        items = result.scalars().all()
        if items:
            for item in items:
                item.is_active = False
            await session.commit()
        return items
