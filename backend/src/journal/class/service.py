from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .repository import ClassRepository, ClassStudentRepository
from .schemas import (
    ClassDTO,
    ClassAddDTO,
    ClassChangeDTO,
    ClassStudentAddDTO
)


class ClassService:
    @staticmethod
    async def get_classes() -> list[ClassDTO]:
        students = await ClassRepository.get_classes()
        return students

    @staticmethod
    async def add_class(data: ClassAddDTO) -> ClassDTO:
        group = await ClassRepository.add_class(data)
        return group

    @staticmethod
    async def get_class(class_id: int) -> ClassDTO:
        group = await ClassRepository.get_class(class_id)
        if not group:
            raise ObjectNotFoundException
        return group

    @staticmethod
    async def change_class(
        class_id: int,
        data: ClassChangeDTO
    ) -> ClassDTO:
        group = await ClassRepository.get_class(class_id)
        if not group:
            raise ObjectNotFoundException
        group = await ClassRepository.change_class(
            class_id,
            data
        )
        return group

    @staticmethod
    async def delete_class(class_id: int) -> ClassDTO:
        group = await ClassRepository.delete_class(class_id)
        return group


class ClassStudentService:
    @staticmethod
    async def add_student_in_class(id_class: int, id_student: int):
        class_student = await ClassStudentRepository.add_student_in_class(
            id_class,
            id_student
        )
        return class_student

    @staticmethod
    async def excluded_student_from_class(id_class: int, id_student: int):
        class_student = await ClassStudentRepository.excluded_student_from_class(
            id_class,
            id_student
        )
        return class_student
