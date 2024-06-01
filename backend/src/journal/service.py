from .exceptions import (
    ObjectIsExistException,
    ObjectNotActiveException,
    ObjectNotFoundException,
)
from .repository import StudioRepository
from .schemas import (
    StudioDTO,
    StudioAddDTO,
    StudioChangeDTO
)


class StudioService:
    @staticmethod
    async def get_studios() -> list[StudioDTO]:
        studios = await StudioRepository.get_studios()
        return studios

    @staticmethod
    async def add_studio(
        studio: StudioAddDTO,
    ) -> StudioDTO:
        number = await StudioRepository.get_count_by_name(studio)
        if number > 0:
            raise ObjectIsExistException
        studio = await StudioRepository.add_studio(studio)
        return studio

    @staticmethod
    async def get_studio(studio_id: int) -> StudioDTO:
        try:
            studio = await StudioRepository.get_studio(studio_id)
        except Exception:
            raise ObjectNotFoundException
        else:
            if not studio.is_active:
                raise ObjectNotActiveException
            studio_model = studio.model_dump()
            studio = StudioDTO.model_validate(studio_model)
            return studio

    @staticmethod
    async def change_studio(
        studio_id: int,
        studio: StudioChangeDTO
    ) -> StudioDTO:
        try:
            studio_old = await StudioRepository.get_studio(studio_id)
        except Exception:
            raise ObjectNotFoundException
        else:
            if not studio_old.is_active:
                raise ObjectNotActiveException
            number = await StudioRepository.get_count_by_name(studio)
            if number > 0 and studio_old.name != studio.name:
                raise ObjectIsExistException
        studio = await StudioRepository.change_studio(studio_id, studio)
        return studio
