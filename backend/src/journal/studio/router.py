from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from database import new_async_session
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
async def get_studios() -> list[StudioDTO]:
    """
    Функция получения списка студий.
    """
    async with new_async_session() as session:
        items = await StudioService.get_items(session=session)
        return items


@router.post(
    '',
    response_model=StudioDTO,
    status_code=201
)
async def add_studio(
    data: StudioAddDTO
):
    """
    Функция добавления студии.
    Проверка на существование студии с тем же именем среди активных.
    Если существует - возвращается ответ с кодом 400.
    """
    async with new_async_session() as session:
        item_check = await StudioService.get_item_by_name(
            session=session,
            name=data.name
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await StudioService.add_item(
            session=session,
            data=data
        )
        return item


@router.get(
    '/{studio_id}',
    response_model=StudioDTO
)
async def get_studio(studio_id: int) -> Optional[StudioDTO]:
    """
    Функция получения студии по ее id.
    Если студия не найдена - возвращается ответ с кодом 404.
    """
    async with new_async_session() as session:
        item = await StudioService.get_item(
            session=session,
            id=studio_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        return item


@router.patch(
    '/{studio_id}',
    response_model=StudioDTO
)
async def change_studio(
    data: StudioChangeDTO,
    studio_id: int,
):
    """
    Функция для изменения сведений о студии.
    Если студия не найдена - возвращается ответ с кодом 404.
    """
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
    # status_code=204
)
async def delete_studio(
    studio_id: int,
):
    """
    Функция удаления студии.
    Если студия не найдена - возвращается ответ с кодом 404.
    При успешном удалении возвращается ответ с кодом 204.
    """
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
        return JSONResponse(status_code=204, content=None)
