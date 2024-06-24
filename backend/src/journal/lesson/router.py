from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .service import (
    LessonService,
    LessonStudentService,
    LessonTypeService,
    StudentVisitService
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


router = APIRouter(
    prefix='/lessons',
    tags=['lessons']
)


@router.get('/')
async def get_lessons() -> list[LessonDTO]:
    lessons = await LessonService.get_lessons()
    return lessons


@router.post('/', response_model=LessonDTO, status_code=201)
async def add_group(
    lesson: LessonAddDTO,
) -> LessonDTO:
    try:
        lesson = await LessonService.add_lesson(lesson)
        return lesson
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)


@router.get(
    '/{lesson_id}',
    response_model=LessonDTO
)
async def get_lesson(lesson_id: int) -> LessonDTO:
    try:
        lesson = await LessonService.get_lesson(lesson_id)
        return lesson
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.patch('/{lesson_id}')
async def change_lesson(
    lesson: LessonChangeDTO,
    lesson_id: int,
) -> LessonDTO:
    try:
        lesson = await LessonService.change_lesson(lesson_id)
        return lesson
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.post('/{lesson_id}/student')
async def add_student_in_lesson(lesson_id: int, student_id: int):
    lesson_student = await LessonStudentService.add_student_in_lesson(
        lesson_id,
        student_id
    )
    return lesson_student


@router.delete('/{lesson_id}/student')
async def excluded_student_from_lesson(lesson_id: int, student_id: int):
    lesson_student = await LessonStudentService.excluded_student_from_lesson(
        lesson_id,
        student_id
    )
    return lesson_student


@router.get('/student_visit')
async def get_student_visits() -> list[StudentVisitDTO]:
    student_visits = await StudentVisitService.get_student_visits()
    return student_visits


@router.post(
    '/student_visit',
    response_model=StudentVisitDTO,
    status_code=201
)
async def add_student_visit(
    student_visit: StudentVisitAddDTO,
) -> StudentVisitDTO:
    try:
        student_visit = await StudentVisitService.add_student_visit(
            student_visit
        )
        return student_visit
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)


@router.get(
    'student_visit/{student_visit_id}',
    response_model=StudentVisitDTO
)
async def get_student_visit(student_visit_id: int) -> StudentVisitDTO:
    try:
        student_visit = await StudentVisitService.get_student_visit(
            student_visit_id
        )
        return student_visit
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.patch('student_visit/{student_visit_id}')
async def change_student_visit(
    student_visit: StudentVisitChangeDTO,
    student_visit_id: int,
) -> StudentVisitDTO:
    try:
        student_visit = await StudentVisitService.change_student_visit(
            student_visit_id
        )
        return student_visit
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.get('/lesson_type')
async def get_lesson_types() -> list[LessonTypeDTO]:
    lesson_types = await LessonTypeService.get_lesson_types()
    return lesson_types


@router.post('/lesson_type', response_model=LessonTypeDTO, status_code=201)
async def add_lesson_type(
    lesson_type: LessonTypeAddDTO,
) -> LessonTypeDTO:
    try:
        lesson_type = await LessonTypeService.add_lesson_type(lesson_type)
        return lesson_type
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)


@router.get(
    'lesson_type/{lesson_type_id}',
    response_model=LessonTypeDTO
)
async def get_lesson_type(lesson_type_id: int) -> LessonTypeDTO:
    try:
        lesson_type = await LessonTypeService.get_lesson_type(lesson_type_id)
        return lesson_type
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.patch('lesson_type/{lesson_type_id}')
async def change_lesson_type(
    lesson_type: LessonTypeChangeDTO,
    lesson_type_id: int,
) -> LessonTypeDTO:
    try:
        lesson_type = await LessonTypeService.change_lesson_type(
            lesson_type_id
        )
        return lesson_type
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)
