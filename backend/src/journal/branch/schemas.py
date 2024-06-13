from pydantic import BaseModel, ConfigDict, Field


# DTO = Data Transfer Object
class BranchAddDTO(BaseModel):
    studio_id: int = Field(title='Студия')
    name: str = Field(max_length=50, title='Название филиала')
    address: str = Field(title='Адрес филиала')

    model_config = ConfigDict(from_attributes=True)


class BranchDTO(BranchAddDTO):
    id: int


class BranchChangeDTO(BaseModel):
    name: str = Field(max_length=50, title='Название филиала')
    address: str = Field(title='Адрес филиала')

    # model_config = ConfigDict(from_attributes=True)
