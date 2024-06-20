from typing import Optional
from sqlalchemy import select

from database import new_async_session

from ..exceptions import ObjectNotFoundException
from .models import Group, GroupStudent
from .schemas import (
    GroupAddDTO,
    GroupDTO,
    GroupChangeDTO,
    GroupStudentAddDTO
)


class GroupRepository:
    @classmethod
    async def add_group(cls, data: GroupAddDTO) -> GroupDTO:
        async with new_async_session() as session:
            group_dict = data.model_dump()
            group = Group(**group_dict)
            session.add(group)
            await session.commit()
            return group

    @classmethod
    async def get_groups(cls) -> list[GroupDTO]:
        async with new_async_session() as session:
            query = select(Group).filter(
                Group.is_active
            )
            result = await session.execute(query)
            groups = result.scalars().all()
            return groups

    @classmethod
    async def get_group(cls, group_id: int) -> Optional[GroupDTO]:
        async with new_async_session() as session:
            query = select(Group).filter(
                Group.id == group_id,
                Group.is_active
            )
            result = await session.execute(query)
            group = result.scalars().one_or_none()
            return group

    @classmethod
    async def change_group(
        cls,
        group_id: int,
        data: GroupChangeDTO
    ) -> Optional[GroupDTO]:
        async with new_async_session() as session:
            query = select(Group).filter(
                Group.id == group_id,
                Group.is_active
            )
            result = await session.execute(query)
            group = result.scalars().one()
            group.name = data.name
            group.teacher_id = data.teacher_id
            group.age_min = data.age_min
            group.age_max = data.age_max
            await session.commit()
            return group

    @classmethod
    async def delete_group(cls, group_id: int):
        async with new_async_session() as session:
            query = select(Group).filter(
                Group.id == group_id,
                Group.is_active
            )
            result = await session.execute(query)
            group = result.scalars().one_or_none()
            if not group:
                raise ObjectNotFoundException
            group.is_active = False
            await session.commit()
            return group


class GroupStudentRepository:
    @classmethod
    async def add_student_in_group(
        cls,
        data: GroupStudentAddDTO
    ):  # -> GroupDTO:
        async with new_async_session() as session:
            group_student_dict = data.model_dump()
            group_student = GroupStudent(**group_student_dict)
            session.add(group_student)
            await session.commit()
            return group_student

    @classmethod
    async def excluded_student_from_group(
        cls,
        group_id: int,
        student_id: int
    ):  # -> GroupDTO:
        async with new_async_session() as session:
            query = select(GroupStudent).filter(
                GroupStudent.student_id == student_id,
                GroupStudent.group_id == group_id
            )
            result = await session.execute(query)
            row = result.scalars().one_or_none()
            row.is_excluded = True
            await session.commit()
            return row

    async def get_students_in_group(cls, group_id: int) -> list[int]:
        async with new_async_session() as session:
            query = select(GroupStudent.student_id).filter(
                GroupStudent.group_id == group_id
            )
            result = await session.execute(query)
            students = result.scalars().all()
            return students
