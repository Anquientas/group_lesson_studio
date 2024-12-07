from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from database import new_async_session
from .service import RoomService
from .schemas import (
    RoomDTO,
    RoomAddDTO,
    RoomChangeDTO
)


router = APIRouter(
    prefix='/rooms',
    tags=['Rooms']
)


@router.get('')
async def get_rooms() -> list[RoomDTO]:
    async with new_async_session() as session:
        items = await RoomService.get_items(session=session)
        return items


@router.post(
    '',
    response_model=RoomDTO,
    status_code=201
)
async def add_room(
    data: RoomAddDTO
):
    async with new_async_session() as session:
        item_check = await RoomService.get_item_by_name(
            session=session,
            data=data
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await RoomService.add_item(
            session=session,
            data=data
        )
        return item


@router.get(
    '/{room_id}',
    response_model=RoomDTO
)
async def get_room(room_id: int) -> Optional[RoomDTO]:
    async with new_async_session() as session:
        item = await RoomService.get_item(
            session=session,
            id=room_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        return item


@router.patch(
    '/{room_id}',
    response_model=RoomDTO
)
async def change_room(
    data: RoomChangeDTO,
    room_id: int,
):
    async with new_async_session() as session:
        item_check = await RoomService.get_item(
            session=session,
            id=room_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        item = await RoomService.change_item(
            session=session,
            id=room_id,
            data=data
        )
        return item


@router.delete(
    '/{room_id}',
    # status_code=204
)
async def delete_room(
    room_id: int,
):
    async with new_async_session() as session:
        item_check = await RoomService.get_item(
            session=session,
            id=room_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        await RoomService.delete_item(
            session=session,
            id=room_id
        )
        return JSONResponse(status_code=204, content=None)
