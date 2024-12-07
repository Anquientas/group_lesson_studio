from typing import Optional

from sqlalchemy import select

from .models import Branch


class BranchRepository:
    @classmethod
    async def get_items(
        cls,
        session
    ) -> list[Branch]:
        query = select(Branch).filter(Branch.is_active)
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def get_item(
        cls,
        session,
        id: int
    ) -> Optional[Branch]:
        query = select(Branch).filter(
            Branch.id == id,
            Branch.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def get_item_by_name(
        cls,
        session,
        studio_id: int,
        name: str
    ) -> Optional[Branch]:
        query = select(Branch).filter(
            Branch.studio_id == studio_id,
            Branch.name == name,
            Branch.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def add_item(
        cls,
        session,
        data: dict
    ) -> Branch:
        item = Branch(**data)
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def change_item(
        cls,
        session,
        id: int,
        name: str
    ) -> Optional[Branch]:
        query = select(Branch).filter(
            Branch.id == id,
            Branch.is_active
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
        query = select(Branch).filter(
            Branch.id == id,
            Branch.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        item.is_active = False
        await session.commit()
        return item

    @staticmethod
    async def delete_items_by_studio_id(
        session,
        studio_id: int,
    ):
        query = select(Branch).filter(
            Branch.studio_id == studio_id,
            Branch.is_active
        )
        result = await session.execute(query)
        items = result.scalars().all()
        if items:
            for item in items:
                item.is_active = False
            await session.commit()
        return items
