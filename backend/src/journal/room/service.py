from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .repository import RoomRepository
from .schemas import (
    RoomDTO,
    RoomAddDTO
)


class RoomService:
    @staticmethod
    async def get_rooms() -> list[RoomDTO]:
        rooms = await RoomRepository.get_rooms()
        return rooms

    @staticmethod
    async def add_room(data: RoomAddDTO) -> RoomDTO:
        number = await RoomRepository.get_count_by_name(data)
        if number > 0:
            raise ObjectAlreadyExistsException
        room = await RoomRepository.add_room(data)
        return room

    @staticmethod
    async def get_room(room_id: int) -> RoomDTO:
        room = await RoomRepository.get_room(room_id)
        if not room:
            raise ObjectNotFoundException
        return room

    @staticmethod
    async def change_Room(
        room_id: int,
        data: RoomAddDTO
    ) -> RoomDTO:
        room = await RoomRepository.get_room(room_id)
        if not room:
            raise ObjectNotFoundException
        number = await RoomRepository.get_count_by_name(data)
        if number > 0 and room.name != data.name:
            raise ObjectAlreadyExistsException
        room = await RoomRepository.change_room(room_id, data)
        return room

    @staticmethod
    async def delete_room(room_id: int) -> RoomDTO:
        room = await RoomRepository.delete_room(room_id)
        return room
