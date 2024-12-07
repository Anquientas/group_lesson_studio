from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from database import new_async_session
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
    tags=['Lessons']
)


@router.get('')
async def get_lessons() -> list[LessonDTO]:
    async with new_async_session() as session:
        items = await LessonService.get_items(session)
        return items


@router.post('', response_model=LessonDTO, status_code=201)
async def add_lesson(
    data: LessonAddDTO,
) -> LessonDTO:
    async with new_async_session() as session:
        item_check = await LessonService.get_item_by_fields(
            session=session,
            data=data
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item_add = await LessonService.add_item(
            session=session,
            data=data
        )
        return item_add


@router.get(
    '/{lesson_id}',
    response_model=LessonDTO
)
async def get_lesson(lesson_id: int) -> LessonDTO:
    async with new_async_session() as session:
        item = await LessonService.get_item(
            session=session,
            id=lesson_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        return item


@router.patch('/{lesson_id}')
async def change_lesson(
    lesson: LessonChangeDTO,
    lesson_id: int,
) -> LessonDTO:
    async with new_async_session() as session:
        item_check = await LessonService.get_item(
            session=session,
            id=lesson_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        item = await LessonService.change_item(
            session=session,
            id=lesson_id,
            data=lesson
        )
        return item


@router.get('/types')
async def get_lesson_types() -> list[LessonTypeDTO]:
    async with new_async_session() as session:
        items = await LessonTypeService.get_items(session=session)
        return items


@router.post(
    '/types',
    response_model=LessonTypeDTO,
    status_code=201
)
async def add_lesson_type(
    data: LessonTypeAddDTO,
) -> LessonTypeDTO:
    async with new_async_session() as session:
        item_check = await LessonTypeService.get_item_by_fields(
            session=session,
            data=data
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await LessonTypeService.add_item(data)
        return item


@router.get(
    '/types/{type_id}',
    response_model=LessonTypeDTO
)
async def get_lesson_type(type_id: int) -> LessonTypeDTO:
    async with new_async_session() as session:
        item = await LessonTypeService.get_item(
            session=session,
            id=type_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        return item


@router.patch('/types/{type_id}')
async def change_lesson_type(
    data: LessonTypeChangeDTO,
    type_id: int,
) -> LessonTypeDTO:
    async with new_async_session() as session:
        item = await LessonTypeService.get_item(
            session=session,
            id=type_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        item = await LessonTypeService.change_item(
            session=session,
            id=type_id,
            data=data
        )
        return item


@router.get('/{lesson_id}/students')
async def get_students_in_lesson(
    lesson_id: int
):
    async with new_async_session() as session:
        relations = await LessonStudentService.get_relations(
            session=session,
            lesson_id=lesson_id,
        )
        return relations


@router.get('/{lesson_id}/students/{student_id}')
async def get_student_in_lesson(
    lesson_id: int,
    student_id: int
):
    async with new_async_session() as session:
        relation = await LessonStudentService.get_relation(
            session=session,
            lesson_id=lesson_id,
            student_id=student_id
        )
        return relation


@router.post('/{lesson_id}/students/{student_id}')
async def add_student_in_lesson(
    lesson_id: int,
    student_id: int
):
    async with new_async_session() as session:
        relation_check = await LessonStudentService.get_relation(
            session=session,
            lesson_id=lesson_id,
            student_id=student_id
        )
        if relation_check:
            return JSONResponse(status_code=400, content=None)
        relation = await LessonStudentService.add_relation(
            session=session,
            lesson_id=lesson_id,
            student_id=student_id
        )
        return relation


@router.delete('/{lesson_id}/students/{student_id}')
async def excluded_student_from_lesson(
    lesson_id: int,
    student_id: int
):
    async with new_async_session() as session:
        relation_check = await LessonStudentService.get_relation(
            session=session,
            lesson_id=lesson_id,
            student_id=student_id
        )
        if not relation_check:
            return JSONResponse(status_code=404, content=None)
        relation = await LessonStudentService.delete_relation(
            session=session,
            lesson_id=lesson_id,
            student_id=student_id
        )
        return relation


@router.get('/student_visit_types')
async def get_student_visit_types() -> list[StudentVisitDTO]:
    async with new_async_session() as session:
        items = await StudentVisitService.get_items(
            session=session
        )
        return items


@router.post(
    '/student_visits_types',
    response_model=StudentVisitDTO,
    status_code=201
)
async def add_student_visit_type(
    data: StudentVisitAddDTO
) -> StudentVisitDTO:
    async with new_async_session() as session:
        item_check = await StudentVisitService.get_item_by_fields(
            session=session,
            data=data
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await StudentVisitService.add_item(
            session=session,
            data=data
        )
        return item


@router.get('/student_visit_types/{type_id}')
async def get_student_visit_type(
    type_id: int
) -> Optional[StudentVisitDTO]:
    async with new_async_session() as session:
        item = await StudentVisitService.get_item(
            session=session,
            id=type_id
        )
        return item


@router.patch('/student_visit_types/{type_id}')
async def change_student_visit_type(
    type_id: int,
    data: StudentVisitChangeDTO
) -> StudentVisitDTO:
    async with new_async_session() as session:
        item_check = await StudentVisitService.get_item(
            session=session,
            id=type_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        item = await StudentVisitService.change_item(
            session=session,
            id=type_id,
            data=data
        )
        return item
