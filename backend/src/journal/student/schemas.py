from pydantic import BaseModel, ConfigDict, Field

from ..employee.models import Gender


# DTO = Data Transfer Object
class StudentAddDTO(BaseModel):
    surname: str = Field(max_length=50, title='Фамилия')
    first_name: str = Field(max_length=50, title='Имя')
    last_name: str = Field(max_length=50, title='Отчество')
    gender: Gender = Field(title='Пол')
    phone: str = Field(max_length=12, title='Номер телефона')
    email: str = Field(max_length=150, title='E-mail')

    model_config = ConfigDict(from_attributes=True)


class StudentDTO(StudentAddDTO):
    id: int


class StudentChangeDTO(BaseModel):
    surname: str = Field(max_length=50, title='Фамилия')
    first_name: str = Field(max_length=50, title='Имя')
    last_name: str = Field(max_length=50, title='Отчество')
    gender: Gender = Field(title='Пол')
    phone: str = Field(max_length=12, title='Номер телефона')
    email: str = Field(max_length=150, title='E-mail')
