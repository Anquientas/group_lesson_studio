from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .repository import EmployeeRepository
from .schemas import (
    EmployeeDTO,
    EmployeeAddDTO,
    EmployeeChangeDTO
)


class EmployeeService:
    @staticmethod
    async def get_employees() -> list[EmployeeDTO]:
        employees = await EmployeeRepository.get_employees()
        return employees

    @staticmethod
    async def add_employee(data: EmployeeAddDTO) -> EmployeeDTO:
        number = await EmployeeRepository.get_count_by_main_parameters(data)
        if number > 0:
            raise ObjectAlreadyExistsException
        employee = await EmployeeRepository.add_employee(data)
        return employee

    @staticmethod
    async def get_employee(employee_id: int) -> EmployeeDTO:
        employee = await EmployeeRepository.get_employee(employee_id)
        if not employee:
            raise ObjectNotFoundException
        return employee

    @staticmethod
    async def change_employee(
        employee_id: int,
        data: EmployeeChangeDTO
    ) -> EmployeeDTO:
        employee = await EmployeeRepository.get_employee(employee_id)
        if not employee:
            raise ObjectNotFoundException
        number = await EmployeeRepository.get_count_by_main_parameters(data)
        if (
            number > 0
            and employee.surname != data.surname
            and employee.first_name != data.first_name
            and employee.phone != data.phone
        ):
            raise ObjectAlreadyExistsException
        employee = await EmployeeRepository.change_employee(
            employee_id,
            data
        )
        return employee

    @staticmethod
    async def delete_employee(employee_id: int) -> EmployeeDTO:
        employee = await EmployeeRepository.delete_employee(employee_id)
        return employee

    @staticmethod
    async def get_employees_by_role(role_id: int) -> list[EmployeeDTO]:
        employees = await EmployeeRepository.get_employees_by_role(role_id)
        return employees
