from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .service import StudentService
from .schemas import StudentAddDTO, StudentDTO, StudentChangeDTO


router = APIRouter(
    prefix='/students',
    tags=['students']
)


@router.get('/')
async def get_students(studio_id: int) -> list[StudentDTO]:
    students = await StudentService.get_students(studio_id)
    return students


@router.post('/', response_model=StudentDTO, status_code=201)
async def add_student(
    student: StudentAddDTO,
) -> StudentDTO:
    try:
        student = await StudentService.add_student(student)
        return student
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)


@router.get(
    '/{student_id}',
    response_model=StudentDTO
)
async def get_student(student_id: int) -> StudentDTO:
    try:
        student = await StudentService.get_student(student_id)
        return student
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.patch('/{student_id}')
async def change_student(
    student: StudentChangeDTO,
    student_id: int,
) -> StudentDTO:
    try:
        student = await StudentService.change_student(student_id, student)
        return student
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.delete('/{student_id}')
async def delete_student(
    student_id: int,
) -> None:
    try:
        await StudentService.delete_student(student_id)
        return JSONResponse(status_code=204, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)
