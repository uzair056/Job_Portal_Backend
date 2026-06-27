from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.user import UserCreate, UserUpdate
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



@router.put("/update_candidate/{user_id}")
def update_candidate_route(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    return update_candidate(db, user_id, user)


@router.delete("/delete_candidate/{user_id}")
def delete_candidate_route(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_candidate(db, user_id)


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