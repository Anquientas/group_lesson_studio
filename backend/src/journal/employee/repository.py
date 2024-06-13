from typing import Optional
from sqlalchemy import func, select

from database import new_async_session

from ..exceptions import ObjectNotFoundException
from .models import Employee
from .schemas import EmployeeAddDTO, EmployeeDTO, EmployeeChangeDTO


class EmployeeRepository:
    @classmethod
    async def get_count_by_main_parameters(cls, data: EmployeeAddDTO) -> int:
        async with new_async_session() as session:
            query = select(func.count()).filter(
                Employee.surname == data.surname,
                Employee.first_name == data.first_name,
                Employee.phone == data.phone,
            )
            number = await session.execute(query)
            return number.scalars().all()[0]

    @classmethod
    async def add_employee(cls, data: EmployeeAddDTO) -> EmployeeDTO:
        async with new_async_session() as session:
            employee_dict = data.model_dump()
            employee = Employee(**employee_dict)
            session.add(employee)
            await session.commit()
            return employee

    @classmethod
    async def get_employees(cls) -> list[EmployeeDTO]:
        async with new_async_session() as session:
            query = select(Employee).filter(
                Employee.is_active
            )
            result = await session.execute(query)
            employees = result.scalars().all()
            return employees

    @classmethod
    async def get_employees_by_role(cls, role_id: int) -> list[EmployeeDTO]:
        async with new_async_session() as session:
            query = select(Employee).filter(
                Employee.role_id == role_id,
                Employee.is_active
            )
            result = await session.execute(query)
            employees = result.scalars().all()
            return employees

    @classmethod
    async def get_employee(cls, employee_id: int) -> Optional[EmployeeDTO]:
        async with new_async_session() as session:
            query = select(Employee).filter(
                Employee.id == employee_id,
                Employee.is_active
            )
            result = await session.execute(query)
            employee = result.scalars().one_or_none()
            return employee

    @classmethod
    async def change_employee(
        cls,
        employee_id: int,
        data: EmployeeChangeDTO
    ) -> Optional[EmployeeDTO]:
        async with new_async_session() as session:
            query = select(Employee).filter(
                Employee.id == employee_id,
                Employee.is_active
            )
            result = await session.execute(query)
            employee = result.scalars().one()
            employee.surname = data.surname
            employee.first_name = data.first_name
            employee.last_name = data.last_name
            employee.phone = data.phone
            employee.email = data.email
            await session.commit()
            return employee

    @classmethod
    async def delete_employee(cls, employee_id: int):
        async with new_async_session() as session:
            query = select(Employee).filter(
                Employee.id == employee_id,
                Employee.is_active
            )
            result = await session.execute(query)
            employee = result.scalars().one_or_none()
            if not employee:
                raise ObjectNotFoundException
            employee.is_active = False
            await session.commit()
            return employee
