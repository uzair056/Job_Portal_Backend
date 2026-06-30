from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.company import Company
from models.user import User
from schemas.company import CompanyCreate

from repositories.company_repository import (
    create_company,
    get_company_by_user
)


def store_company(
    db: Session,
    current_user: User,
    company: CompanyCreate
):
    if current_user.role not in [
        "admin",
        "recruiter"
    ]:
        raise HTTPException(
            status_code=403,
            detail="You cannot create company."
        )

    if current_user.role == "recruiter":
        existing_company = get_company_by_user(
            db,
            current_user.id
        )

        if existing_company:
            raise HTTPException(
                status_code=400,
                detail="Recruiter can create only one company."
            )

    new_company = Company(
        name=company.name,
        email=company.email,
        city=company.city,
        country=company.country,
        address=company.address,
        website=company.website,
        description=company.description,
        logo=company.logo,
        user_id=current_user.id
    )

    return create_company(
        db,
        new_company
    )