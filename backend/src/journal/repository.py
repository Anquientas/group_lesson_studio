from sqlalchemy import func, select

from database import new_async_session

from .models import Studio
from .schemas import StudioAddDTO, StudioDTO, StudioChangeDTO, StudioActiveDTO


class StudioRepository:
    @staticmethod
    async def get_count_by_name(studio: StudioAddDTO) -> int:
        async with new_async_session() as session:
            query = select(func.count()).filter(Studio.name == studio.name)
            number = await session.execute(query)
            return number.scalars().all()[0]

    @classmethod
    async def add_studio(cls, studio: StudioAddDTO) -> StudioDTO:
        async with new_async_session() as session:
            studio_dict = studio.model_dump()
            studio = Studio(**studio_dict)
            session.add(studio)
            await session.commit()
            return studio

    @classmethod
    async def get_studios(cls) -> list[StudioDTO]:
        async with new_async_session() as session:
            query = select(Studio).filter(Studio.is_active)
            result = await session.execute(query)
            studio_models = result.scalars().all()
            studio_schemas = [
                StudioDTO.model_validate(studio) for studio in studio_models
            ]
            return studio_schemas

    @classmethod
    async def get_studio(cls, studio_id: int) -> StudioActiveDTO:
        async with new_async_session() as session:
            query = select(Studio).filter(Studio.id == studio_id)
            result = await session.execute(query)
            studio_model = result.scalars().one_or_none()
            studio_schema = StudioActiveDTO.model_validate(studio_model)
            return studio_schema

    @classmethod
    async def change_studio(cls, studio_id: int, data: StudioChangeDTO):
        async with new_async_session() as session:
            query = select(Studio).filter(Studio.id == studio_id)
            result = await session.execute(query)
            studio = result.scalars().one_or_none()
            if data.name:
                studio.name = data.name
            studio.is_active = data.is_active
            await session.commit()
            return studio
