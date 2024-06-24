from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .repository import (
    LessonRepository,
    LessonStudentRepository,
    LessonTypeRepository,
    StudentVisitRepository
)
from .schemas import (
    LessonDTO,
    LessonAddDTO,
    LessonChangeDTO,
    LessonStudentAddDTO,
    LessonStudentChangeDTO,
    LessonStudentDTO,
    LessonTypeDTO,
    LessonTypeAddDTO,
    LessonTypeChangeDTO,
    StudentVisitDTO,
    StudentVisitAddDTO,
    StudentVisitChangeDTO
)


class LessonTypeService:
    @staticmethod
    async def get_lesson_types() -> list[LessonTypeDTO]:
        lesson_types = await LessonTypeRepository.get_lesson_types()
        return lesson_types

    @staticmethod
    async def add_lesson_type(data: LessonTypeAddDTO) -> LessonTypeDTO:
        lesson_type = await LessonTypeRepository.add_lesson_type(data)
        return lesson_type

    @staticmethod
    async def get_lesson_type(lessson_type_id: int) -> LessonTypeDTO:
        lesson_type = await LessonTypeRepository.get_lesson_type(
            lessson_type_id
        )
        if not lesson_type:
            raise ObjectNotFoundException
        return lesson_type

    @staticmethod
    async def change_lesson_type(
        lesson_type_id: int,
        data: LessonTypeChangeDTO
    ) -> LessonTypeDTO:
        lesson_type = await LessonTypeRepository.get_lesson_type(
            lesson_type_id
        )
        if not lesson_type:
            raise ObjectNotFoundException
        lesson_type_new = await LessonTypeRepository.change_lesson_type(
            lesson_type_id,
            data
        )
        return lesson_type_new


class StudentVisitService:
    @staticmethod
    async def get_student_visits() -> list[StudentVisitDTO]:
        student_visits = await StudentVisitRepository.get_student_visit()
        return student_visits

    @staticmethod
    async def add_student_visit(data: StudentVisitAddDTO) -> StudentVisitDTO:
        student_visit = await StudentVisitRepository.add_student_visit(data)
        return student_visit

    @staticmethod
    async def get_student_visit(student_visit_id: int) -> LessonTypeDTO:
        student_visit = await StudentVisitRepository.get_student_visit(
            student_visit_id
        )
        if not student_visit:
            raise ObjectNotFoundException
        return student_visit

    @staticmethod
    async def change_student_visit(
        student_visit_id: int,
        data: StudentVisitChangeDTO
    ) -> LessonTypeDTO:
        student_visit = await StudentVisitRepository.get_student_visit(
            student_visit_id
        )
        if not student_visit:
            raise ObjectNotFoundException
        student_visit_new = await StudentVisitRepository.change_student_visit(
            student_visit_id,
            data
        )
        return student_visit_new


class LessonService:
    @staticmethod
    async def get_lessons() -> list[LessonDTO]:
        lessons = await LessonRepository.get_lessons()
        return lessons

    @staticmethod
    async def add_lesson(data: LessonAddDTO) -> LessonDTO:
        lesson = await LessonRepository.add_lesson(data)
        return lesson

    @staticmethod
    async def get_lesson(id_lesson: int) -> LessonDTO:
        lesson = await LessonRepository.get_lesson(id_lesson)
        if not lesson:
            raise ObjectNotFoundException
        return lesson

    @staticmethod
    async def change_lesson(
        id_lesson: int,
        data: LessonChangeDTO
    ) -> LessonDTO:
        lesson = await LessonRepository.get_lesson(id_lesson)
        if not lesson:
            raise ObjectNotFoundException
        lesson_new = await LessonRepository.change_lesson(
            id_lesson,
            data
        )
        return lesson_new


class LessonStudentService:
    @staticmethod
    async def add_student_in_lesson(id_lesson: int, id_student: int):
        lesson_student = await LessonStudentRepository.add_student_in_lesson(
            id_lesson,
            id_student
        )
        return lesson_student

    @staticmethod
    async def excluded_student_from_lesson(id_lesson: int, id_student: int):
        lesson_student = (
            await LessonStudentRepository.excluded_student_from_lesson(
                id_lesson,
                id_student
            )
        )
        return lesson_student
