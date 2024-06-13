from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .service import StudioService
from .schemas import StudioAddDTO, StudioDTO


router = APIRouter(
    prefix='/studios',
    tags=['Studios']
)


@router.get('/')
async def get_studios() -> list[StudioDTO]:
    studios = await StudioService.get_studios()
    return studios


@router.post('/', response_model=StudioDTO, status_code=201)
async def add_studio(
    studio: StudioAddDTO,
) -> StudioDTO:
    try:
        studio = await StudioService.add_studio(studio)
        return studio
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)


@router.get(
    '/{studio_id}',
    response_model=StudioDTO
)
async def get_studio(studio_id: int) -> StudioDTO:
    try:
        studio = await StudioService.get_studio(studio_id)
        return studio
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.patch('/{studio_id}')
async def change_studio(
    studio: StudioAddDTO,
    studio_id: int,
) -> StudioDTO:
    try:
        studio = await StudioService.change_studio(studio_id, studio)
        return studio
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.delete('/{studio_id}')
async def delete_studio(
    studio_id: int,
) -> None:
    try:
        await StudioService.delete_studio(studio_id)
        return JSONResponse(status_code=204, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)
