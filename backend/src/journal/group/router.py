from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from database import new_async_session
from .service import GroupService, GroupStudentService
from .schemas import (
    GroupDTO,
    GroupAddDTO,
    GroupChangeDTO,
    GroupStudentDTO
)


router = APIRouter(
    prefix='/groups',
    tags=['Groups']
)


@router.get('')
async def get_groups() -> list[GroupDTO]:
    async with new_async_session() as session:
        items = await GroupService.get_items(session=session)
        return items


@router.post(
    '',
    response_model=GroupDTO,
    status_code=201
)
async def add_group(
    data: GroupAddDTO
):
    async with new_async_session() as session:
        item_check = await GroupService.get_item_by_name(
            session=session,
            name=data.name
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await GroupService.add_item(
            session=session,
            data=data
        )
        return item


@router.get(
    '/{group_id}',
    response_model=GroupDTO
)
async def get_group(group_id: int) -> Optional[GroupDTO]:
    async with new_async_session() as session:
        item = await GroupService.get_item(
            session=session,
            id=group_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        return item


@router.patch(
    '/{group_id}',
    response_model=GroupDTO
)
async def change_group(
    data: GroupChangeDTO,
    group_id: int,
):
    async with new_async_session() as session:
        item_check = await GroupService.get_item(
            session=session,
            id=group_id,
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        item = await GroupService.change_item(
            session=session,
            id=group_id,
            data=data
        )
        return item


@router.delete(
    '/{group_id}',
    # status_code=204
)
async def delete_group(
    group_id: int,
):
    async with new_async_session() as session:
        item_check = await GroupService.get_item(
            session=session,
            id=group_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        await GroupService.delete_item(
            session=session,
            id=group_id
        )
        return JSONResponse(status_code=204, content=None)


@router.get('/{group_id}/students')
async def get_students_in_group(group_id: int) -> list[GroupStudentDTO]:
    async with new_async_session() as session:
        items = await GroupStudentService.get_items(
            session=session,
            group_id=group_id
        )
        return items


@router.post(
    '/{group_id}/students/{student_id}',
    response_model=GroupStudentDTO,
    status_code=201
)
async def add_student_in_group(
    group_id: int,
    student_id: int
):
    async with new_async_session() as session:
        item_check = await GroupStudentService.get_item_by_ids(
            session=session,
            group_id=group_id,
            student_id=student_id
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await GroupStudentService.add_item(
            session=session,
            group_id=group_id,
            student_id=student_id
        )
        return item


@router.delete(
    '/{group_id}/students/{student_id}',
    # status_code=204
)
async def excluded_student_from_group(
    group_id: int,
    student_id: int
):
    async with new_async_session() as session:
        item_check = await GroupStudentService.get_item_by_ids(
            session=session,
            group_id=group_id,
            student_id=student_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        await GroupStudentService.delete_item(
            session=session,
            group_id=group_id,
            student_id=student_id
        )
        return JSONResponse(status_code=204, content=None)
