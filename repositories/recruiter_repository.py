from sqlalchemy.orm import Session
from models.user import User


def create_recruiter(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_all_recruiters(db: Session):
    return db.query(User).filter(
        User.role == "recruiter"
    ).all()


def get_recruiter_by_id(db: Session, id: int):
    return db.query(User).filter(
        User.id == id,
        User.role == "recruiter"
    ).first()


def update_recruiter(
    db: Session,
    recruiter: User
):
    db.commit()
    db.refresh(recruiter)

    return recruiter

def delete_recruiter(db: Session, recruiter: User):
    db.delete(recruiter)
    db.commit()

    return {
        "message": "Recruiter deleted successfully"
    }