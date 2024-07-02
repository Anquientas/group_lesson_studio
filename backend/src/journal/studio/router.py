from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ...database import new_async_session
from .service import StudioService
from .schemas import (
    StudioDTO,
    StudioAddDTO,
    StudioChangeDTO
)


router = APIRouter(
    prefix='/studios',
    tags=['Studios']
)


@router.get('')
async def get_studios() -> Optional[list[StudioDTO]]:
    async with new_async_session() as session:
        items = await StudioService.get_studios(session=session)
        return items


@router.post(
    '',
    response_model=StudioDTO,
    status_code=201
)
async def add_studio(
    data: StudioAddDTO
) -> Optional[StudioDTO]:
    async with new_async_session() as session:
        item_check = await StudioService.get_item_by_fields(
            session=session,
            data=data
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await StudioService.add_item(
            session=session,
            data=data
        )
        return item


@router.get('/{studio_id}')
async def get_studio(studio_id: int) -> Optional[StudioDTO]:
    async with new_async_session() as session:
        item = await StudioService.get_item(
            session=session,
            id=studio_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        return item


@router.patch('/{studio_id}')
async def change_studio(
    data: StudioChangeDTO,
    studio_id: int,
) -> Optional[StudioDTO]:
    async with new_async_session() as session:
        item_check = await StudioService.get_item(
            session=session,
            id=studio_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        item = await StudioService.change_item(
            session=session,
            id=studio_id,
            data=data
        )
        return item


@router.delete(
    '/{studio_id}',
    status_code=204
)
async def delete_studio(
    studio_id: int,
):
    async with new_async_session() as session:
        item_check = await StudioService.get_item(
            session=session,
            id=studio_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        item = await StudioService.delete_item(
            session=session,
            id=studio_id
        )
        return item
