from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import user_schema
from app.repositories.organization_repository import OrganizationRepository
from app.repositories.user_repository import UserRepository
from app.services.organization_service import OrganizationService
from app.utils.jwt import require_admin

router = APIRouter(tags=["Organizations"])

@router.put("/admin/org/{org_id}/user/{user_id}", response_model=user_schema.UserOut)
def add_user_to_org(
    org_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(require_admin)
):
    org_service = OrganizationService(
        OrganizationRepository(db),
        UserRepository(db)
    )
    try:
        updated_user = org_service.add_user_to_org(user_id, org_id)
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
