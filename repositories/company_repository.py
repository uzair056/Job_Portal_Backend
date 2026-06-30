from sqlalchemy.orm import Session
from models.company import Company


def create_company(
    db: Session,
    company: Company
):
    db.add(company)
    db.commit()
    db.refresh(company)

    return company


def get_company_by_user(
    db: Session,
    user_id: int
):
    return db.query(Company).filter(
        Company.user_id == user_id
    ).first()