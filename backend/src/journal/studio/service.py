from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .repository import StudioRepository
from .schemas import (
    StudioDTO,
    StudioAddDTO
)


class StudioService:
    @staticmethod
    async def get_studios() -> list[StudioDTO]:
        studios = await StudioRepository.get_studios()
        return studios

    @staticmethod
    async def add_studio(data: StudioAddDTO) -> StudioDTO:
        number = await StudioRepository.get_count_by_name(data)
        if number > 0:
            raise ObjectAlreadyExistsException
        studio = await StudioRepository.add_studio(data)
        return studio

    @staticmethod
    async def get_studio(studio_id: int) -> StudioDTO:
        studio = await StudioRepository.get_studio(studio_id)
        if not studio:
            raise ObjectNotFoundException
        return studio

    @staticmethod
    async def change_studio(
        studio_id: int,
        data: StudioAddDTO
    ) -> StudioDTO:
        studio = await StudioRepository.get_studio(studio_id)
        if not studio:
            raise ObjectNotFoundException
        number = await StudioRepository.get_count_by_name(data)
        if number > 0 and studio.name != data.name:
            raise ObjectAlreadyExistsException
        studio = await StudioRepository.change_studio(studio_id, data)
        return studio

    @staticmethod
    async def delete_studio(studio_id: int) -> StudioDTO:
        studio = await StudioRepository.delete_studio(studio_id)
        return studio
