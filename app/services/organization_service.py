from app.repositories.organization_repository import OrganizationRepository
from app.repositories.user_repository import UserRepository
from app.models.user import User, RoleEnum
from app.utils.jwt import get_password_hash

class OrganizationService:
    def __init__(self, org_repo: OrganizationRepository, user_repo: UserRepository):
        self.org_repo = org_repo
        self.user_repo = user_repo

    def add_user_to_org(self, user_id: int, org_id: int):
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        org = self.org_repo.get_by_id(org_id)
        if not org:
            raise ValueError("Organization not found")

        user.organization_id = org_id
        return self.user_repo.update(user)
