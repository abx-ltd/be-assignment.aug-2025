from sqlalchemy.orm import Session
from app.models.organization import Organization
from app.models.user import User

class OrganizationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, org_id: int):
        return self.db.query(Organization).filter(Organization.id == org_id).first()
