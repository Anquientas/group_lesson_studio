from pydantic import BaseModel, ConfigDict, Field


# DTO = Data Transfer Object
class RoomAddDTO(BaseModel):
    branch_id: int = Field(title='Филиал')
    name: str = Field(max_length=50, title='Помещение')

    model_config = ConfigDict(from_attributes=True)


class RoomDTO(RoomAddDTO):
    id: int
    is_active: bool
