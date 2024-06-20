from pydantic import BaseModel, ConfigDict, Field


# DTO = Data Transfer Object
class GroupAddDTO(BaseModel):
    branch_id: int = Field(title='Филиал')
    teacher_id: int = Field(title='Преподаватель')
    name: str = Field(max_length=100, title='Название')
    age_min: int = Field(title='Минимальный возраст')
    age_max: int = Field(title='Максимальный возраст')

    model_config = ConfigDict(from_attributes=True)


class GroupDTO(GroupAddDTO):
    id: int


class GroupChangeDTO(BaseModel):
    branch_id: int = Field(title='Филиал')
    teacher_id: int = Field(title='Преподаватель')
    name: str = Field(max_length=100, title='Название')
    age_min: int = Field(title='Минимальный возраст')
    age_max: int = Field(title='Максимальный возраст')


class GroupStudentAddDTO(BaseModel):
    class_id: int = Field(title='Группа')
    student_id: int = Field(title='Ученик')

    # model_config = ConfigDict(from_attributes=True)
