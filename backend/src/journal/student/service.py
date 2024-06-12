from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .repository import StudentRepository
from .schemas import (
    StudentDTO,
    StudentAddDTO,
    StudentChangeDTO
)


class StudentService:
    @staticmethod
    async def get_students() -> list[StudentDTO]:
        students = await StudentRepository.get_students()
        return students

    @staticmethod
    async def add_student(data: StudentAddDTO) -> StudentDTO:
        number = await StudentRepository.get_count_by_main_parameters(data)
        if number > 0:
            raise ObjectAlreadyExistsException
        student = await StudentRepository.add_student(data)
        return student

    @staticmethod
    async def get_student(student_id: int) -> StudentDTO:
        student = await StudentRepository.get_student(student_id)
        if not student:
            raise ObjectNotFoundException
        return student

    @staticmethod
    async def change_student(
        student_id: int,
        data: StudentChangeDTO
    ) -> StudentDTO:
        student = await StudentRepository.get_student(student_id)
        if not student:
            raise ObjectNotFoundException
        number = await StudentRepository.get_count_by_main_parameters(data)
        if (
            number > 0
            and student.surname != data.surname
            and student.first_name != data.first_name
            and student.phone != data.phone
        ):
            raise ObjectAlreadyExistsException
        student = await StudentRepository.change_student(
            student_id,
            data
        )
        return student

    @staticmethod
    async def delete_student(student_id: int) -> StudentDTO:
        student = await StudentRepository.reactive_student(student_id)
        return student
