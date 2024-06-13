from typing import Optional
from sqlalchemy import func, select

from database import new_async_session

from ..exceptions import ObjectNotFoundException
from .models import Branch
from .schemas import BranchAddDTO, BranchDTO, BranchChangeDTO


class BranchRepository:
    @classmethod
    async def get_count_by_name(cls, data: BranchAddDTO) -> int:
        async with new_async_session() as session:
            query = select(func.count()).filter(
                Branch.name == data.name,
                Branch.studio_id == data.studio_id,
                Branch.is_active
            )
            number = await session.execute(query)
            return number.scalars().all()[0]

    @classmethod
    async def add_branch(cls, data: BranchAddDTO) -> BranchDTO:
        async with new_async_session() as session:
            branch_dict = data.model_dump()
            branch = Branch(**branch_dict)
            session.add(branch)
            await session.commit()
            return branch

    @classmethod
    async def get_branches(cls, studio_id: int) -> list[BranchDTO]:
        async with new_async_session() as session:
            query = select(Branch).filter(
                Branch.studio_id == studio_id,
                Branch.is_active
            )
            result = await session.execute(query)
            branches = result.scalars().all()
            return branches

    @classmethod
    async def get_branch(cls, branch_id: int) -> Optional[BranchDTO]:
        async with new_async_session() as session:
            query = select(Branch).filter(
                Branch.id == branch_id,
                Branch.is_active
            )
            result = await session.execute(query)
            branch = result.scalars().one_or_none()
            return branch

    @classmethod
    async def change_branch(
        cls,
        branch_id: int,
        data: BranchChangeDTO
    ) -> Optional[BranchDTO]:
        async with new_async_session() as session:
            query = select(Branch).filter(
                Branch.id == branch_id,
                Branch.is_active
            )
            result = await session.execute(query)
            branch = result.scalars().one()
            branch.name = data.name
            branch.address = data.address
            await session.commit()
            return branch

    @classmethod
    async def delete_branch(cls, branch_id: int):
        async with new_async_session() as session:
            query = select(Branch).filter(
                Branch.id == branch_id,
                Branch.is_active
            )
            result = await session.execute(query)
            branch = result.scalars().one_or_none()
            if not branch:
                raise ObjectNotFoundException
            branch.is_active = False
            await session.commit()
            return branch
