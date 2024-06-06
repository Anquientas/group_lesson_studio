from typing import Optional
from sqlalchemy import func, select

from database import new_async_session

from ..exceptions import ObjectNotFoundException
from .models import Room
from .schemas import RoomAddDTO, RoomDTO


class RoomRepository:
    @classmethod
    async def get_count_by_name(cls, data: RoomAddDTO) -> int:
        async with new_async_session() as session:
            query = select(func.count()).filter(Room.name == data.name)
            number = await session.execute(query)
            return number.scalars().all()[0]

    @classmethod
    async def add_room(cls, data: RoomAddDTO) -> RoomDTO:
        async with new_async_session() as session:
            room_dict = data.model_dump()
            room = Room(**room_dict)
            session.add(room)
            await session.commit()
            return room

    @classmethod
    async def get_rooms(cls) -> list[RoomDTO]:
        async with new_async_session() as session:
            query = select(Room).filter(Room.is_active)
            result = await session.execute(query)
            rooms = result.scalars().all()
            return rooms

    @classmethod
    async def get_room(cls, room_id: int) -> Optional[RoomDTO]:
        async with new_async_session() as session:
            query = select(Room).filter(
                Room.id == room_id,
                Room.is_active
            )
            result = await session.execute(query)
            room = result.scalars().one_or_none()
            return room

    @classmethod
    async def change_room(
        cls,
        room_id: int,
        data: RoomAddDTO
    ) -> Optional[RoomDTO]:
        async with new_async_session() as session:
            query = select(Room).filter(
                Room.id == room_id,
                Room.is_active
            )
            result = await session.execute(query)
            room = result.scalars().one()
            room.name = data.name
            await session.commit()
            return room

    @classmethod
    async def delete_room(cls, room_id: int):
        async with new_async_session() as session:
            query = select(Room).filter(
                Room.id == room_id,
                Room.is_active
            )
            result = await session.execute(query)
            room = result.scalars().one_or_none()
            if not room:
                raise ObjectNotFoundException
            room.is_active = False
            await session.commit()
            return room
