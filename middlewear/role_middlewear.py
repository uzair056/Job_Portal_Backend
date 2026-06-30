from fastapi import Depends, HTTPException, status

from auth.jwt_handler import get_current_user
from models.user import User


def role_required(allowed_roles: list):
    def checker(
        current_user: User = Depends(get_current_user)
    ):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Unauthorized"
            )

        return current_user

    return checker