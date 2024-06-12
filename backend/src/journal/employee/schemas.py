from pydantic import BaseModel, ConfigDict, Field

from .models import Gender


# DTO = Data Transfer Object
class EmployeeAddDTO(BaseModel):
    surname: str = Field(max_length=50, title='Фамилия')
    first_name: str = Field(max_length=50, title='Имя')
    last_name: str = Field(max_length=50, title='Отчество')
    gender: Gender = Field(title='Пол')
    phone: str = Field(max_length=12, title='Номер телефона')
    email: str = Field(max_length=150, title='E-mail')
    role_id: int = Field(title='Роль')

    model_config = ConfigDict(from_attributes=True)


class EmployeeDTO(EmployeeAddDTO):
    id: int


class EmployeeChangeDTO(BaseModel):
    surname: str = Field(max_length=50, title='Фамилия')
    first_name: str = Field(max_length=50, title='Имя')
    last_name: str = Field(max_length=50, title='Отчество')
    gender: Gender = Field(title='Пол')
    phone: str = Field(max_length=12, title='Номер телефона')
    email: str = Field(max_length=150, title='E-mail')
    role_id: int = Field(title='Роль')
