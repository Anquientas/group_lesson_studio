from typing import Annotated
from fastapi import APIRouter, Depends

from .models import Studio
from .repository import StudioRepository
from .schemas import StudioAddDTO, StudioDTO, StudioChangeDTO


router = APIRouter(
    prefix='',
    tags=['Journal']
)

responses = {

}


@router.get('/studios/')
async def get_studios() -> list[StudioDTO]:
    studios = await StudioRepository.get_studios()
    # print('STUDIOS:', studios)
    return studios


@router.post('/studios/', response_model=StudioDTO)
async def add_studio(
    studio: StudioAddDTO
) -> StudioDTO:
    print(studio)
    studio = await StudioRepository.add_studio(studio)
    return studio


@router.get(
    '/studios/{studio_id}/',
    response_model=StudioDTO,
    responses={
        200: {
            'model': StudioDTO,
            'description': 'Successful Response',
            # 'content': Studio
        },
        404: {
            # 'model': None,
            'description': 'Not found',
            'content': None
        },
    }
)
async def get_studio(studio_id: int) -> StudioDTO:
    studio = await StudioRepository.get_studio(studio_id)
    # print('STUDIO:', studio)
    # print('STUDIO_TYPE:', type(studio))
    return studio


@router.patch('/studios/{studio_id}/')
async def change_studio(
    studio: Annotated[StudioChangeDTO, Depends()],
    # name: Annotated[str, None],
    # is_active: Annotated[bool, None],
    studio_id: int,
) -> StudioDTO:
    # studio = await StudioRepository.change_studio(studio_id, name, is_active)
    studio = await StudioRepository.change_studio(studio_id, studio)
    print('STUDIO:', studio)
    return studio


# @router.patch('/studios/{studio_id}/transactive/')
# async def transactive_studio(studio_id: int) -> StudioDTO:
#     studio = await StudioRepository.transactive_studio(studio_id)
#     print('STUDIO:', studio)
#     return studio


# @router.patch('/studios/{studio_id}/restoration/')
# async def restoration_studio(studio_id: int) -> StudioDTO:
#     studio = await StudioRepository.restoration_studio(studio_id)
#     print('STUDIO:', studio)
#     return studio


# @router.get('/studios/', status_code=200)
# async def get_studios(
#         response: Response,
#         session: AsyncSession = Depends(get_async_session)):
#     """
#     Получение списка студий.
#     """
#     try:
#         query = select(Studio)
#         result = await session.execute(query)
#         # return 'list studios'
#         return {
#             'status': 'success',
#             'data': result.all(),
#             'details': 'list studios'  # None
#         }
#     except Exception:
#         response.status_code = 500
#         detail={
#             'status': 'error',
#             'data': None,
#             'details': 'Какая-то ошибка со списком студий'
#         }
#         # return detail
#         raise HTTPException(status_code=500, detail=detail)
#         # raise HTTPException(status_code=500, detail={
#         #     'status': 'error',
#         #     'data': None,
#         #     'details': 'Какая-то ошибка со списком студий'
#         # })


# @router.post('/studios/')
# async def create_studio(
#     new_studio: Annotated[StudioAddDTO, Depends()],
#     session: AsyncSession = Depends(get_async_session)
# ):
#     # stmt
#     qwerty = new_studio.model_dump()
#     print('qwerty = ', qwerty)
#     statement = insert(Studio).values(**new_studio.model_dump())
#     print('new_studio = ', new_studio)
#     print('statement = ', statement)
#     # await session.execute(statement)
#     # await session.commit()
#     return 'create studio OK'


# @router.get('/studios/{studio_id}/', response_model=List(Studio))
# async def get_studio(studio_id: int):
#     return f'studio {studio_id}'


# @router.patch('/studios/{studio_id}/')
# async def change_studio(studio_id: int):
#     return f'change studio {studio_id} OK'


# @router.get('/studios/{studio_id}/branches/')
# async def get_branches(studio_id: int):
#     return f'list branches studio {studio_id}'


# @router.post('/studios/{studio_id}/branches/')
# async def create_branch(studio_id: int):
#     return f'create branche in studio {studio_id} OK'


# @router.get('/studios/{studio_id}/branches/{branche_id}/')
# async def get_branche(studio_id: int, branche_id: int):
#     return f'branche {branche_id} studio {studio_id}'


# @router.patch('/studios/{studio_id}/branches/{branche_id}/')
# async def change_branche(studio_id: int, branche_id: int):
#     return f'change branche {branche_id} studio {studio_id} OK'


# @router.get('/studios/{studio_id}/branches/{branche_id}/rooms/')
# async def get_rooms(studio_id: int, branche_id: int):
#     return f'list rooms branche {branche_id}'


# @router.post('/studios/{studio_id}/branches/{branche_id}/rooms/')
# async def create_room(studio_id: int, branche_id: int):
#     return f'create room in branche {branche_id} OK'


# @router.get('/studios/{studio_id}/branches/{branche_id}/rooms/{room_id}/')
# async def get_room(studio_id: int, branche_id: int, room_id: int):
#     return f'room {room_id} branche {branche_id}'


# @router.patch('/studios/{studio_id}/branches/{branche_id}/rooms/{room_id}/')
# async def change_room(studio_id: int, branche_id: int, room_id: int):
#     return f'change room {room_id} branche {branche_id} OK'


# @router.get('/studios/{studio_id}/branches/{branche_id}/classes/')
# async def get_classes(studio_id: int, branche_id: int):
#     return f'list classes branche {branche_id}'


# @router.post('/studios/{studio_id}/branches/{branche_id}/classes/')
# async def create_class(studio_id: int, branche_id: int):
#     return f'create class in branche {branche_id} OK'


# @router.get('/studios/{studio_id}/branches/{branche_id}/classes/{class_id}/')
# async def get_class(studio_id: int, branche_id: int, class_id: int):
#     return f'class {class_id} branche {branche_id}'


# @router.patch('/studios/{studio_id}/branches/{branche_id}/classes/{class_id}/')
# async def change_class(studio_id: int, branche_id: int, class_id: int):
#     return f'change class {class_id} branche {branche_id} OK'
