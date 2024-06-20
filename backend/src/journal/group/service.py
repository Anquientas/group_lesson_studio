from ..exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException
)
from .repository import GroupRepository, GroupStudentRepository
from .schemas import (
    GroupDTO,
    GroupAddDTO,
    GroupChangeDTO,
    GroupStudentAddDTO
)


class GroupService:
    @staticmethod
    async def get_groups() -> list[GroupDTO]:
        groups = await GroupRepository.get_groups()
        return groups

    @staticmethod
    async def add_group(data: GroupAddDTO) -> GroupDTO:
        group = await GroupRepository.add_group(data)
        return group

    @staticmethod
    async def get_group(group_id: int) -> GroupDTO:
        group = await GroupRepository.get_group(group_id)
        if not group:
            raise ObjectNotFoundException
        return group

    @staticmethod
    async def change_group(
        group_id: int,
        data: GroupChangeDTO
    ) -> GroupDTO:
        group = await GroupRepository.get_group(group_id)
        if not group:
            raise ObjectNotFoundException
        group = await GroupRepository.change_group(
            group_id,
            data
        )
        return group

    @staticmethod
    async def delete_group(group_id: int) -> GroupDTO:
        group = await GroupRepository.delete_group(group_id)
        return group


class GroupStudentService:
    @staticmethod
    async def add_student_in_group(id_group: int, id_student: int):
        group_student = await GroupStudentRepository.add_student_in_group(
            id_group,
            id_student
        )
        return group_student

    @staticmethod
    async def excluded_student_from_group(id_group: int, id_student: int):
        group_student = await GroupStudentRepository.excluded_student_from_group(
            id_group,
            id_student
        )
        return group_student
