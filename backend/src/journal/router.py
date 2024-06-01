from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .exceptions import (
    ObjectIsExistException,
    ObjectNotActiveException,
    ObjectNotFoundException,
)
from .service import StudioService
from .schemas import StudioAddDTO, StudioDTO, StudioChangeDTO


router = APIRouter(
    prefix='',
    tags=['Journal']
)


@router.get('/studios/')
async def get_studios() -> list[StudioDTO]:
    studios = await StudioService.get_studios()
    return studios


@router.post('/studios/', response_model=StudioDTO)
async def add_studio(
    studio: StudioAddDTO,
) -> StudioDTO:
    try:
        studio = await StudioService.add_studio(studio)
        return studio
    except ObjectIsExistException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotActiveException:
        return JSONResponse(status_code=403, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.get(
    '/studios/{studio_id}/',
    response_model=StudioDTO
)
async def get_studio(studio_id: int) -> StudioDTO:
    try:
        studio = await StudioService.get_studio(studio_id)
        return studio
    except ObjectNotActiveException:
        return JSONResponse(status_code=403, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)
    except Exception as exception:
        print(exception)
        return exception


@router.patch('/studios/{studio_id}/')
async def change_studio(
    studio: StudioChangeDTO,
    studio_id: int,
) -> StudioDTO:
    try:
        studio = await StudioService.change_studio(studio_id, studio)
        return studio
    except ObjectIsExistException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotActiveException:
        return JSONResponse(status_code=403, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)
