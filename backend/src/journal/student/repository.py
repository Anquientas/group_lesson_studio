from typing import Optional
from sqlalchemy import func, select

from database import new_async_session

from ..exceptions import ObjectNotFoundException
from .models import Student
from .schemas import StudentAddDTO, StudentDTO, StudentChangeDTO


class StudentRepository:
    @classmethod
    async def get_count_by_main_parameters(cls, data: StudentAddDTO) -> int:
        async with new_async_session() as session:
            query = select(func.count()).filter(
                Student.surname == data.surname,
                Student.first_name == data.first_name,
                Student.phone == data.phone,
            )
            number = await session.execute(query)
            return number.scalars().all()[0]

    @classmethod
    async def add_student(cls, data: StudentAddDTO) -> StudentDTO:
        async with new_async_session() as session:
            student_dict = data.model_dump()
            student = Student(**student_dict)
            session.add(student)
            await session.commit()
            return student

    @classmethod
    async def get_students(cls) -> list[StudentDTO]:
        async with new_async_session() as session:
            query = select(Student).filter(
                Student.is_active
            )
            result = await session.execute(query)
            students = result.scalars().all()
            return students

    @classmethod
    async def get_noactive_students(cls) -> list[StudentDTO]:
        async with new_async_session() as session:
            query = select(Student).filter(
                not Student.is_active
            )
            result = await session.execute(query)
            students = result.scalars().all()
            return students

    @classmethod
    async def get_student(cls, student_id: int) -> Optional[StudentDTO]:
        async with new_async_session() as session:
            query = select(Student).filter(
                Student.id == student_id,
                Student.is_active
            )
            result = await session.execute(query)
            student = result.scalars().one_or_none()
            return student

    @classmethod
    async def change_student(
        cls,
        student_id: int,
        data: StudentChangeDTO
    ) -> Optional[StudentDTO]:
        async with new_async_session() as session:
            query = select(Student).filter(
                Student.id == student_id,
                Student.is_active
            )
            result = await session.execute(query)
            student = result.scalars().one()
            student.surname = data.surname
            student.first_name = data.first_name
            student.last_name = data.last_name
            student.phone = data.phone
            student.email = data.email
            await session.commit()
            return student

    @classmethod
    async def reactive_student(cls, student_id: int):
        async with new_async_session() as session:
            query = select(Student).filter(
                Student.id == student_id
            )
            result = await session.execute(query)
            student = result.scalars().one_or_none()
            if not student:
                raise ObjectNotFoundException
            student.is_active = not student.is_active
            await session.commit()
            return student
