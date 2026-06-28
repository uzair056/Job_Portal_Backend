from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext

from models.user import User
from schemas.user import UserCreate, RecruiterUpdate

from repositories.recruiter_repository import (
    create_recruiter,
    delete_recruiter,
    get_all_recruiters,
    get_recruiter_by_id,
    update_recruiter,
)



# pwd_context = CryptContext(
#     schemes=["bcrypt"],
#     deprecated="auto"
# )

# create recruiter

def store_recruiter(db: Session, user: UserCreate):
    recruiter = User(
        name=user.name,
        email=user.email,
        password=(user.password),
        role="recruiter"
    )

    return create_recruiter(
        db,
        recruiter
    )
    
# get all recruiters
def index_recruiters(db: Session):
    return get_all_recruiters(db)



# update recruiter
def edit_recruiter(
    db: Session,
    id: int,
    user: RecruiterUpdate
):
    recruiter = get_recruiter_by_id(
        db,
        id
    )

    if not recruiter:
        raise HTTPException(
            status_code=404,
            detail="Recruiter not found"
        )

    recruiter.name = user.name
    recruiter.email = user.email

    return update_recruiter(
        db,
        recruiter
    )
    
# deleter recruiter
def destroy_recruiter(
    db: Session,
    id: int
):
    recruiter = get_recruiter_by_id(
        db,
        id
    )

    if not recruiter:
        raise HTTPException(
            status_code=404,
            detail="Recruiter not found"
        )

    return delete_recruiter(
        db,
        recruiter
    )