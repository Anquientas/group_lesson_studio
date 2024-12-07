from typing import Optional

from sqlalchemy import select

from .models import Group, GroupStudent


class GroupRepository:
    @classmethod
    async def get_items(
        cls,
        session
    ) -> list[Group]:
        query = select(Group).filter(Group.is_active)
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def get_item(
        cls,
        session,
        id: int
    ) -> Optional[Group]:
        query = select(Group).filter(
            Group.id == id,
            Group.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def get_item_by_name(
        cls,
        session,
        name: str
    ) -> Optional[Group]:
        query = select(Group).filter(
            Group.name == name,
            Group.is_active
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def add_item(
        cls,
        session,
        data: dict
    ) -> Group:
        item = Group(**data)
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def change_item(
        cls,
        session,
        id: int,
        name: str
    ) -> Optional[Group]:
        query = select(Group).filter(
            Group.id == id,
            Group.is_active
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
        query = select(Group).filter(
            Group.id == id,
            Group.is_active
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
        query = select(Group).filter(
            Group.branch_id == branch_id,
            Group.is_active
        )
        result = await session.execute(query)
        items = result.scalars().all()
        if items:
            for item in items:
                item.is_active = False
            await session.commit()
        return items


class GroupStudentRepository:
    @classmethod
    async def get_items(
        cls,
        session,
        group_id: int
    ) -> list[GroupStudent]:
        query = select(GroupStudent).filter(
            GroupStudent.group_id == group_id,
            not GroupStudent.is_excluded
        )
        result = await session.execute(query)
        items = result.scalars().all()
        return items

    @classmethod
    async def get_item_by_ids(
        cls,
        session,
        group_id: int,
        student_id: int
    ) -> GroupStudent:
        query = select(GroupStudent).filter(
            GroupStudent.group_id == group_id,
            GroupStudent.student_id == student_id,
            not GroupStudent.is_excluded
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        return item

    @classmethod
    async def add_item(
        cls,
        session,
        group_id: int,
        student_id: int
    ) -> GroupStudent:
        item = GroupStudent(
            group_id=group_id,
            student_id=student_id
        )
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def delete_item(
        cls,
        session,
        group_id: int,
        student_id: int
    ):
        query = select(GroupStudent).filter(
            GroupStudent.group_id == group_id,
            GroupStudent.student_id == student_id
        )
        result = await session.execute(query)
        item = result.scalars().one_or_none()
        item.is_excluded = True
        await session.commit()
        return item
