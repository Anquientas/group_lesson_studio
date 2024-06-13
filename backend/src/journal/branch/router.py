from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .service import BranchService
from .schemas import BranchAddDTO, BranchDTO, BranchChangeDTO


router = APIRouter(
    prefix='/branches',
    tags=['Branches']
)


@router.get('/')
async def get_branches(studio_id: int) -> list[BranchDTO]:
    branchs = await BranchService.get_branches(studio_id)
    return branchs


@router.post('/', response_model=BranchDTO, status_code=201)
async def add_branch(
    branch: BranchAddDTO,
) -> BranchDTO:
    try:
        branch = await BranchService.add_branch(branch)
        return branch
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)


@router.get(
    '/{branch_id}',
    response_model=BranchDTO
)
async def get_branch(branch_id: int) -> BranchDTO:
    try:
        branch = await BranchService.get_branch(branch_id)
        return branch
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.patch('/{branch_id}')
async def change_branch(
    branch: BranchChangeDTO,
    branch_id: int,
) -> BranchDTO:
    try:
        branch = await BranchService.change_branch(branch_id, branch)
        return branch
    except ObjectAlreadyExistsException:
        return JSONResponse(status_code=400, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)


@router.delete('/{branch_id}')
async def delete_branch(
    branch_id: int,
) -> None:
    try:
        await BranchService.delete_branch(branch_id)
        return JSONResponse(status_code=204, content=None)
    except ObjectNotFoundException:
        return JSONResponse(status_code=404, content=None)
