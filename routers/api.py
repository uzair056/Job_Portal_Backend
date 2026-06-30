from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.auth import LoginSchema
from schemas.company import CompanyCreate
from services.auth_service import login
from models.user import User
from middlewear.role_middlewear import role_required
from auth.jwt_handler import get_current_user
from database import get_db
from schemas.user import RecruiterUpdate, UserCreate, UserUpdate
from services.recruiter_service import  (
destroy_recruiter,
edit_recruiter,
index_recruiters,
store_recruiter
)
from services.company_service import  (

store_company
)
from services.user_service import (
    create_candidate,
    update_candidate,
    delete_candidate,
    get_all_candidates,
    get_candidate_by_id,
)
router = APIRouter()

# candidates operations


@router.post("/create_candidate")
def create_candidate_route(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_candidate(db, user)


# update candidate
@router.put("/update_candidate/{user_id}")
def update_candidate_route(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    return update_candidate(db, user_id, user)

# delete candidate
@router.delete("/delete_candidate/{user_id}")
def delete_candidate_route(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_candidate(db, user_id)

# get all candidates
@router.get("/candidates")
def get_all_candidates_route(
    db: Session = Depends(get_db)
):
    return get_all_candidates(db)


@router.get("/candidate/{user_id}")
def get_candidate_by_id_route(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_candidate_by_id(db, user_id)

# recruiters 
# create recruiter

@router.post("/create_recruiters")
def create_recruiter_route(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return store_recruiter(db, user)


# get all recruiters

@router.get("/recruiters")
def get_recruiters(
    db: Session = Depends(get_db)
):
    return index_recruiters(db)

# update recruiter

@router.put("/update_recruiter/{id}")
def update_recruiter(
    id: int,
    user: RecruiterUpdate,
    db: Session = Depends(get_db)
):
    return edit_recruiter(
        db,
        id,
        user
    )
    
    
# delete recruiter

@router.delete("/delete_recruiter/{id}")
def delete_recruiter(
    id: int,
    db: Session = Depends(get_db)
):
    return destroy_recruiter(
        db,
        id
    )
    
    
# login route

@router.post("/login")
def login_route(
    user: LoginSchema,
    db: Session = Depends(get_db)
):
    return login(
        db,
        user
    )


@router.post("/companies")
def create_company(
    company: CompanyCreate,
    current_user=Depends(
        role_required(["admin", "recruiter"])
    ),
    db: Session = Depends(get_db)
):
    return store_company(
        db,
        current_user,
        company
    )