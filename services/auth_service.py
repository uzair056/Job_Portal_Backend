from fastapi import HTTPException

from auth.jwt_handler import create_access_token
from repositories.auth_repository import (
    get_user_by_email
)


def login(
    db,
    user
):
    db_user = get_user_by_email(
        db,
        user.email
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if db_user.password != user.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "id": db_user.id,
            "name": db_user.name,
            "email": db_user.email,
            "role": db_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_in": 3600
    }