from pydantic import BaseModel, ConfigDict, Field

from ..employee.models import Gender


# DTO = Data Transfer Object
class ClassAddDTO(BaseModel):
    branch_id: int = Field(title='Филиал')
    teacher_id: int = Field(title='Преподаватель')
    name: str = Field(max_length=100, title='Название')
    age_min: int = Field(title='Минимальный возраст')
    age_max: int = Field(title='Максимальный возраст')

    model_config = ConfigDict(from_attributes=True)


class ClassDTO(ClassAddDTO):
    id: int


class ClassChangeDTO(BaseModel):
    branch_id: int = Field(title='Филиал')
    teacher_id: int = Field(title='Преподаватель')
    name: str = Field(max_length=100, title='Название')
    age_min: int = Field(title='Минимальный возраст')
    age_max: int = Field(title='Максимальный возраст')


class ClassStudentAddDTO(BaseModel):
    class_id: int = Field(title='Группа')
    student_id: int = Field(title='Ученик')

    # model_config = ConfigDict(from_attributes=True)
