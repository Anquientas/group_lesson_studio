from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .service import GroupService, GroupStudentService
from .schemas import GroupAddDTO, GroupDTO, GroupChangeDTO


router = APIRouter(
    prefix='/classes',
    tags=['classes']
)


@router.get('/')
async def get_groups() -> list[GroupDTO]:
    groups = await GroupService.get_groups()
    return groups


@router.post('/', response_model=GroupDTO, status_code=201)
async def add_group(
    group: GroupAddDTO,
) -> GroupDTO:
    try:
        group = await GroupService.add_group(group)
        return group
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)


@router.get(
    '/{group_id}',
    response_model=GroupDTO
)
async def get_group(group_id: int) -> GroupDTO:
    try:
        group = await GroupService.get_group(group_id)
        return group
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.patch('/{group_id}')
async def change_group(
    group: GroupChangeDTO,
    group_id: int,
) -> GroupDTO:
    try:
        group = await GroupService.change_group(group_id)
        return group
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.delete('/{group_id}')
async def delete_group(
    group_id: int,
) -> None:
    try:
        await GroupService.delete_group(group_id)
        return JSONResponse(status_code=204, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.post('/{group_id}/student')
async def add_student_in_group(group_id: int, student_id: int):
    group_student = await GroupStudentService.add_student_in_group(
        group_id,
        student_id
    )
    return group_student


@router.delete('/{group_id}/student')
async def excluded_student_from_group(group_id: int, student_id: int):
    group_student = await GroupStudentService.excluded_student_from_group(
        group_id,
        student_id
    )
    return group_student
