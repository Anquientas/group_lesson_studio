from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .service import RoomService
from .schemas import RoomAddDTO, RoomDTO


router = APIRouter(
    prefix='/rooms',
    tags=['Rooms']
)


@router.get('/')
async def get_rooms() -> list[RoomDTO]:
    rooms = await RoomService.get_rooms()
    return rooms


@router.post('/', response_model=RoomDTO, status_code=201)
async def add_room(
    room: RoomAddDTO,
) -> RoomDTO:
    try:
        room = await RoomService.add_room(room)
        return room
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)


@router.get(
    '/{room_id}',
    response_model=RoomDTO
)
async def get_room(room_id: int) -> RoomDTO:
    try:
        room = await RoomService.get_room(room_id)
        return room
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.patch('/{room_id}')
async def change_Room(
    room: RoomAddDTO,
    room_id: int,
) -> RoomDTO:
    try:
        room = await RoomService.change_room(room_id, room)
        return room
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.delete('/{room_id}')
async def delete_Room(
    room_id: int,
) -> None:
    try:
        await RoomService.delete_room(room_id)
        return JSONResponse(status_code=204, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)
