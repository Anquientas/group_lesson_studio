from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .repository import BranchRepository
from .schemas import (
    BranchDTO,
    BranchAddDTO,
    BranchChangeDTO
)


class BranchService:
    @staticmethod
    async def get_branches(studio_id: int) -> list[BranchDTO]:
        branchs = await BranchRepository.get_branches(studio_id)
        return branchs

    @staticmethod
    async def add_branch(data: BranchAddDTO) -> BranchDTO:
        number = await BranchRepository.get_count_by_name(data)
        if number > 0:
            raise ObjectAlreadyExistsException
        branch = await BranchRepository.add_branch(data)
        return branch

    @staticmethod
    async def get_branch(branch_id: int) -> BranchDTO:
        branch = await BranchRepository.get_branch(branch_id)
        if not branch:
            raise ObjectNotFoundException
        return branch

    @staticmethod
    async def change_branch(
        branch_id: int,
        data: BranchChangeDTO
    ) -> BranchDTO:
        branch = await BranchRepository.get_branch(branch_id)
        if not branch:
            raise ObjectNotFoundException
        number = await BranchRepository.get_count_by_name(data)
        if number > 0 and branch.name != data.name:
            raise ObjectAlreadyExistsException
        branch = await BranchRepository.change_branch(branch_id, data)
        return branch

    @staticmethod
    async def delete_branch(branch_id: int) -> BranchDTO:
        branch = await BranchRepository.delete_branch(branch_id)
        return branch
