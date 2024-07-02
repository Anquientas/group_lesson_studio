from pydantic import BaseModel, ConfigDict, Field


# DTO = Data Transfer Object
class StudioAddDTO(BaseModel):
    name: str = Field(max_length=50, title='Название студии')

    model_config = ConfigDict(from_attributes=True)


class StudioDTO(StudioAddDTO):
    id: int


class StudioChangeDTO(BaseModel):
    name: str = Field(max_length=50, title='Название студии')
