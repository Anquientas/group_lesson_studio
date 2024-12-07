from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from database import new_async_session
from .service import EmployeeService, RoleService
from .schemas import (
    EmployeeDTO,
    EmployeeAddDTO,
    EmployeeChangeDTO,
    RoleDTO,
    RoleAddDTO,
    RoleChangeDTO,
)


router = APIRouter(
    prefix='/employees',
    tags=['Employees']
)


@router.get('')
async def get_employees() -> list[EmployeeDTO]:
    async with new_async_session() as session:
        items = await EmployeeService.get_items(session=session)
        return items


@router.post(
    '',
    response_model=EmployeeDTO,
    status_code=201
)
async def add_employee(
    data: EmployeeAddDTO
):
    async with new_async_session() as session:
        item_check = await EmployeeService.get_item_by_name(
            session=session,
            data=data
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await EmployeeService.add_item(
            session=session,
            data=data
        )
        return item


@router.get(
    '/{employee_id}',
    response_model=EmployeeDTO
)
async def get_employee(employee_id: int) -> Optional[EmployeeDTO]:
    async with new_async_session() as session:
        item = await EmployeeService.get_item(
            session=session,
            id=employee_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        return item


@router.patch(
    '/{employee_id}',
    response_model=EmployeeDTO
)
async def change_employee(
    data: EmployeeChangeDTO,
    room_id: int
):
    async with new_async_session() as session:
        item_check = await EmployeeService.get_item(
            session=session,
            id=room_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        item = await EmployeeService.change_item(
            session=session,
            id=room_id,
            data=data
        )
        return item


@router.delete(
    '/{employee_id}',
    # status_code=204
)
async def delete_employee(
    employee_id: int
):
    async with new_async_session() as session:
        item_check = await EmployeeService.get_item(
            session=session,
            id=employee_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        await EmployeeService.delete_item(
            session=session,
            id=employee_id
        )
        return JSONResponse(status_code=204, content=None)


@router.get(
    '/{role_id}',
    response_model=EmployeeDTO
)
async def get_employees_by_role(role_id: int) -> list[EmployeeDTO]:
    async with new_async_session() as session:
        items = await EmployeeService.get_items_by_role(
            session=session,
            id=role_id
        )
        return items


@router.get('/roles')
async def get_roles() -> list[RoleDTO]:
    async with new_async_session() as session:
        items = await RoleService.get_items(session=session)
        return items


@router.post(
    '/roles',
    response_model=RoleDTO,
    status_code=201
)
async def add_role(
    data: RoleAddDTO
):
    async with new_async_session() as session:
        item_check = await RoleService.get_item_by_name(
            session=session,
            data=data
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await RoleService.add_item(
            session=session,
            data=data
        )
        return item


@router.get(
    '/roles/{role_id}',
    response_model=RoleDTO
)
async def get_role(role_id: int) -> Optional[RoleDTO]:
    async with new_async_session() as session:
        item = await RoleService.get_item(
            session=session,
            id=role_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        return item


@router.patch(
    'roles/{role_id}',
    response_model=RoleDTO
)
async def change_role(
    data: RoleChangeDTO,
    role_id: int
):
    async with new_async_session() as session:
        item_check = await RoleService.get_item(
            session=session,
            id=role_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        item = await RoleService.change_item(
            session=session,
            id=role_id,
            data=data
        )
        return item
