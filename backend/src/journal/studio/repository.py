from typing import Optional
from sqlalchemy import func, select

from database import new_async_session
from ..exceptions import ObjectNotFoundException
from .models import Studio
from .schemas import StudioAddDTO, StudioDTO


class StudioRepository:
    @classmethod
    async def get_count_by_name(cls, data: StudioAddDTO) -> int:
        async with new_async_session() as session:
            query = select(func.count()).filter(
                Studio.name == data.name,
                Studio.is_active
            )
            number = await session.execute(query)
            return number.scalars().all()[0]

    @classmethod
    async def add_studio(cls, data: StudioAddDTO) -> StudioDTO:
        async with new_async_session() as session:
            studio_dict = data.model_dump()
            studio = Studio(**studio_dict)
            session.add(studio)
            await session.commit()
            return studio

    @classmethod
    async def get_studios(cls) -> list[StudioDTO]:
        async with new_async_session() as session:
            query = select(Studio).filter(Studio.is_active)
            result = await session.execute(query)
            studios = result.scalars().all()
            return studios

    @classmethod
    async def get_studio(cls, studio_id: int) -> Optional[StudioDTO]:
        async with new_async_session() as session:
            query = select(Studio).filter(
                Studio.id == studio_id,
                Studio.is_active
            )
            result = await session.execute(query)
            studio = result.scalars().one_or_none()
            return studio

    @classmethod
    async def change_studio(
        cls,
        studio_id: int,
        data: StudioAddDTO
    ) -> Optional[StudioDTO]:
        async with new_async_session() as session:
            query = select(Studio).filter(
                Studio.id == studio_id,
                Studio.is_active
            )
            result = await session.execute(query)
            studio = result.scalars().one()
            studio.name = data.name
            await session.commit()
            return studio

    @classmethod
    async def delete_studio(cls, studio_id: int):
        async with new_async_session() as session:
            query = select(Studio).filter(
                Studio.id == studio_id,
                Studio.is_active
            )
            result = await session.execute(query)
            studio = result.scalars().one_or_none()
            if not studio:
                raise ObjectNotFoundException
            studio.is_active = False
            await session.commit()
            return studio
