from pydantic import BaseModel, ConfigDict, Field


# DTO = Data Transfer Object
class StudioAddDTO(BaseModel):
    name: str = Field(max_length=50, title='Название студии')

    model_config = ConfigDict(from_attributes=True)


class StudioDTO(StudioAddDTO):
    id: int


class BranchAddDTO(BaseModel):
    name: str
    address: str


class BranchDTO(BranchAddDTO):
    id: int
    is_active: bool


class RoomAddDTO(BaseModel):
    name: str


class RoomDTO(RoomAddDTO):
    id: int
    is_active: bool
