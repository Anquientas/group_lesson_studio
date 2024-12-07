from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from database import new_async_session
from ..studio.service import StudioService
from .service import BranchService
from .schemas import (
    BranchDTO,
    BranchAddDTO,
    BranchChangeDTO
)


router = APIRouter(
    prefix='/branches',
    tags=['Branches']
)


@router.get('')
async def get_branches() -> list[BranchDTO]:
    async with new_async_session() as session:
        items = await BranchService.get_items(session=session)
        return items


@router.post(
    '',
    response_model=BranchDTO,
    status_code=201
)
async def add_branch(
    data: BranchAddDTO
):
    async with new_async_session() as session:
        studio_check = await StudioService.get_item(
            session=session,
            id=data.studio_id
        )
        if not studio_check:
            return JSONResponse(status_code=400, content=None)
        item_check = await BranchService.get_item_by_name(
            session=session,
            studio_id=data.studio_id,
            name=data.name
        )
        if item_check:
            return JSONResponse(status_code=400, content=None)
        item = await BranchService.add_item(
            session=session,
            data=data
        )
        return item


@router.get(
    '/{branch_id}',
    response_model=BranchDTO
)
async def get_branch(branch_id: int) -> Optional[BranchDTO]:
    async with new_async_session() as session:
        item = await BranchService.get_item(
            session=session,
            id=branch_id
        )
        if not item:
            return JSONResponse(status_code=404, content=None)
        return item


@router.patch(
    '/{branch_id}',
    response_model=BranchDTO
)
async def change_branch(
    data: BranchChangeDTO,
    branch_id: int,
):
    async with new_async_session() as session:
        item_check = await BranchService.get_item(
            session=session,
            id=branch_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        item = await BranchService.change_item(
            session=session,
            id=branch_id,
            data=data
        )
        return item


@router.delete(
    '/{branch_id}',
    # status_code=204
)
async def delete_branch(
    branch_id: int,
):
    async with new_async_session() as session:
        item_check = await BranchService.get_item(
            session=session,
            id=branch_id
        )
        if not item_check:
            return JSONResponse(status_code=404, content=None)
        await BranchService.delete_item(
            session=session,
            id=branch_id
        )
        return JSONResponse(status_code=204, content=None)
