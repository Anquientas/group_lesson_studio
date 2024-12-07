from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, types

from .models import LessonStatus


# DTO = Data Transfer Object
class LessonTypeAddDTO(BaseModel):
    name: str = Field(max_length=100, title='Тип урока')

    model_config = ConfigDict(from_attributes=True)


class LessonTypeDTO(LessonTypeAddDTO):
    id: int


class LessonTypeChangeDTO(BaseModel):
    name: str = Field(max_length=100, title='Тип урока')


class LessonAddDTO(BaseModel):
    type_id: int = Field(title='Тип урока')
    group_id: int = Field(title='Группа')
    room_id: int = Field(title='Помещение')
    date: types.NaiveDatetime = Field(title='Дата')
    time_start: types.NaiveDatetime = Field(title='Начало')
    time_end: types.NaiveDatetime = Field(title='Окончание')

    model_config = ConfigDict(from_attributes=True)


class LessonDTO(LessonAddDTO):
    id: int
    status_id: int = Field(title='Статус')


class LessonChangeDTO(BaseModel):
    type_id: int = Field(title='Тип урока')
    class_id: int = Field(title='Группа')
    room_id: int = Field(title='Помещение')
    date: types.NaiveDatetime = Field(title='Дата')
    time_start: types.NaiveDatetime = Field(title='Начало')
    time_end: types.NaiveDatetime = Field(title='Окончание')
    status: LessonStatus = Field(title='Статус')


class StudentVisitAddDTO(BaseModel):
    type: str = Field(max_length=50, title='Тип посещаемости')

    model_config = ConfigDict(from_attributes=True)


class StudentVisitDTO(LessonTypeAddDTO):
    id: int


class StudentVisitChangeDTO(BaseModel):
    type: str = Field(max_length=50, title='Тип посещаемости')


class LessonStudentAddDTO(BaseModel):
    lesson_id: int = Field(title='Урок')
    student_id: int = Field(title='Ученик')
    visit_id: int = Field(title='Посещение')

    model_config = ConfigDict(from_attributes=True)


class LessonStudentDTO(LessonStudentAddDTO):
    id: int
    excluded_at: bool = Field(title='Исключение')


class LessonStudentChangeDTO(BaseModel):
    visit_id: int = Field(title='Посещение')
    excluded_at: bool = Field(title='Исключение')
