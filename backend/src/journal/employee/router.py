from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .service import EmployeeService
from .schemas import EmployeeAddDTO, EmployeeDTO, EmployeeChangeDTO


router = APIRouter(
    prefix='/employees',
    tags=['employees']
)


@router.get('/')
async def get_employees(studio_id: int) -> list[EmployeeDTO]:
    employees = await EmployeeService.get_employees(studio_id)
    return employees


@router.post('/', response_model=EmployeeDTO, status_code=201)
async def add_employee(
    employee: EmployeeAddDTO,
) -> EmployeeDTO:
    try:
        employee = await EmployeeService.add_employee(employee)
        return employee
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)


@router.get(
    '/{employee_id}',
    response_model=EmployeeDTO
)
async def get_employee(employee_id: int) -> EmployeeDTO:
    try:
        employee = await EmployeeService.get_employee(employee_id)
        return employee
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.get(
    '/{role_id}',
    response_model=EmployeeDTO
)
async def get_employees_by_role(role_id: int) -> EmployeeDTO:
    try:
        employees = await EmployeeService.get_employees_by_role(role_id)
        return employees
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.patch('/{employee_id}')
async def change_employee(
    employee: EmployeeChangeDTO,
    employee_id: int,
) -> EmployeeDTO:
    try:
        employee = await EmployeeService.change_employee(employee_id, employee)
        return employee
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.delete('/{employee_id}')
async def delete_employee(
    employee_id: int,
) -> None:
    try:
        await EmployeeService.delete_employee(employee_id)
        return JSONResponse(status_code=204, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)
