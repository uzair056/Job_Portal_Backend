from fastapi import HTTPException
from repositories.user_repository import (
    create_candidate as repo_create_candidate,
    update_candidate as repo_update_candidate,
    delete_candidate as repo_delete_candidate,
    get_all_candidates as repo_get_all_candidates,
    get_candidate_by_id as repo_get_candidate_by_id,
)



def create_candidate(db, user):
    return repo_create_candidate(db, user)

def update_candidate(db, user_id, user):
    candidate = repo_update_candidate(db, user_id, user)

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found."
        )

    return candidate


def delete_candidate(db, user_id):
    candidate = repo_delete_candidate(db, user_id)

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found."
        )

    return {
        "message": "Candidate deleted successfully."
    }
    
    
def get_all_candidates(db):
    return repo_get_all_candidates(db)


def get_candidate_by_id(db, user_id):
    candidate = repo_get_candidate_by_id(db, user_id)

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found."
        )

    return candidate