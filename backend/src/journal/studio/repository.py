from typing import Optional

from sqlalchemy import select

from .models import Studio


class StudioRepository:
    @classmethod
    async def get_items(
        cls,
        session
    ) -> list[Studio]:
        query = select(Studio).filter(Studio.is_active)
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def get_item(
        cls,
        session,
        id: int
    ) -> Optional[Studio]:
        query = select(Studio).filter(
            Studio.id == id,
            Studio.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def get_item_by_name(
        cls,
        session,
        name: str
    ) -> Optional[Studio]:
        query = select(Studio).filter(
            Studio.name == name,
            Studio.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def add_item(
        cls,
        session,
        data: dict
    ) -> Studio:
        item = Studio(**data)
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def change_item(
        cls,
        session,
        id: int,
        name: str
    ) -> Optional[Studio]:
        query = select(Studio).filter(
            Studio.id == id,
            Studio.is_active
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
        query = select(Studio).filter(
            Studio.id == id,
            Studio.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        item.is_active = False
        await session.commit()
        return item
