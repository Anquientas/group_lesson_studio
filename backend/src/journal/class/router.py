from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .service import ClassService,ClassStudentService
from .schemas import ClassAddDTO, ClassDTO, ClassChangeDTO


router = APIRouter(
    prefix='/classes',
    tags=['classes']
)


@router.get('/')
async def get_classes() -> list[ClassDTO]:
    classes = await ClassService.get_classes()
    return classes


@router.post('/', response_model=ClassDTO, status_code=201)
async def add_class(
    group: ClassAddDTO,
) -> ClassDTO:
    try:
        group = await ClassService.add_class(group)
        return group
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)


@router.get(
    '/{class_id}',
    response_model=ClassDTO
)
async def get_class(class_id: int) -> ClassDTO:
    try:
        group = await ClassService.get_class(class_id)
        return group
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.patch('/{class_id}')
async def change_class(
    group: ClassChangeDTO,
    class_id: int,
) -> ClassDTO:
    try:
        group = await ClassService.change_class(class_id)
        return group
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.delete('/{class_id}')
async def delete_class(
    class_id: int,
) -> None:
    try:
        await ClassService.delete_class(class_id)
        return JSONResponse(status_code=204, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.post('/{class_id}/student')
async def add_student_in_class(class_id: int, student_id: int):
    class_student = await ClassStudentService.add_student_in_class(class_id, student_id)
    return class_student


@router.delete('/{class_id}/student')
async def excluded_student_from_class(class_id: int, student_id: int):
    class_student = await ClassStudentService.excluded_student_from_class(class_id, student_id)
    return class_student
