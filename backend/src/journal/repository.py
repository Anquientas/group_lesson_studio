from fastapi.responses import JSONResponse
from sqlalchemy import select

from database import new_async_session
# from .constants import StudioMessages
from .models import Studio
from .schemas import StudioAddDTO, StudioDTO, StudioChangeDTO


class StudioRepository:
    @classmethod
    async def add_studio(cls, data: StudioAddDTO) -> StudioDTO:
        async with new_async_session() as session:
            studio_dict = data.model_dump()
            # print(studio_dict)
            studio = Studio(**studio_dict)

            studios = select(Studio).filter(Studio.name == studio.name)
            # print('studios =', studios)
            studios = await session.execute(studios)
            # studios = studios.scalars().all()
            # print('studios execute =', studios)
            # if studio.name in studios:
            if studios:
                return JSONResponse(status_code=400, content=None)

            session.add(studio)
            # await session.flush()
            await session.commit()
            # print('studio after commit =', studio)
            return studio

    @classmethod
    async def get_studios(cls) -> list[StudioDTO]:
        async with new_async_session() as session:
            query = select(Studio).filter(Studio.is_active)
            result = await session.execute(query)
            studio_models = result.scalars().all()
            # print('STUDIO_MODELS:', studio_models)
            studio_schemas = [
                StudioDTO.model_validate(studio) for studio in studio_models
            ]
            # print('STUDIO_SCHEMAS:', studio_schemas)
            return studio_schemas

    @classmethod
    async def get_studio(cls, studio_id: int) -> StudioDTO:
        async with new_async_session() as session:
            query = select(Studio).filter(Studio.id == studio_id)
            result = await session.execute(query)
            studio_model = result.scalars().one_or_none()
            if not studio_model:
                return JSONResponse(status_code=404, content=None)
            if not studio_model.is_active:
                return JSONResponse(status_code=403, content=None)
            # print('STUDIO_MODEL:', studio_model)
            studio_schema = StudioDTO.model_validate(studio_model)
            # print('STUDIO_SCHEMA:', studio_schema)
            return studio_schema

    @classmethod
    async def change_studio(cls, studio_id: int, data: StudioChangeDTO):
        async with new_async_session() as session:
            query = select(Studio).filter(Studio.id == studio_id)
            result = await session.execute(query)
            studio = result.scalars().one_or_none()
            # print('studio_model =', studio)
            if not studio:
                return JSONResponse(status_code=404, content=None)
            if not studio.is_active:
                return JSONResponse(status_code=403, content=None)
            if data.name:
                studio.name = data.name
            studio.is_active = data.is_active
            session.add(studio)
            # await session.flush()
            await session.commit()
            # print('result studio =', studio)
            return studio
