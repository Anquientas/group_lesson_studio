from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from database import new_async_session
from .service import StudentService
from .schemas import (
    StudentDTO,
    StudentAddDTO,
    StudentChangeDTO
)


router = APIRouter(
    prefix='/students',
    tags=['Students']
)


@router.get('')
async def get_students() -> list[StudentDTO]:
    async with new_async_session() as session:
        items = await StudentService.get_items(session=session)
        return items


@router.post(
    '',
    response_model=StudentDTO,
    status_code=201
)
async def add_student(
    data: StudentAddDTO
):
    async with new_async_session() as session:
        item_check = await StudentService.get_item_by_name(
            session=session,
            data=data
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await StudentService.add_item(
            session=session,
            data=data
        )
        return item


@router.get(
    '/{student_id}',
    response_model=StudentDTO
)
async def get_student(student_id: int) -> Optional[StudentDTO]:
    async with new_async_session() as session:
        item = await StudentService.get_item(
            session=session,
            id=student_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        return item


@router.patch(
    '/{student_id}',
    response_model=StudentDTO
)
async def change_student(
    data: StudentChangeDTO,
    room_id: int
):
    async with new_async_session() as session:
        item_check = await StudentService.get_item(
            session=session,
            id=room_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        item = await StudentService.change_item(
            session=session,
            id=room_id,
            data=data
        )
        return item


@router.delete(
    '/{student_id}',
    # status_code=204
)
async def delete_student(
    student_id: int
):
    async with new_async_session() as session:
        item_check = await StudentService.get_item(
            session=session,
            id=student_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        await StudentService.delete_item(
            session=session,
            id=student_id
        )
        return JSONResponse(status_code=204, content=None)
