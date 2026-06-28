from sqlalchemy.orm import Session

from models.user import User

# create user
def create_candidate(db, user):
    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



# update user
def update_candidate(db, user_id, user):
    candidate = db.query(User).filter(User.id == user_id).first()

    if not candidate:
        return None

    candidate.name = user.name
    candidate.email = user.email

    db.commit()
    db.refresh(candidate)

    return candidate

# delete user 

def delete_candidate(db, user_id):
    candidate = db.query(User).filter(User.id == user_id).first()

    if not candidate:
        return None

    db.delete(candidate)
    db.commit()

    return candidate

def get_all_candidates(db: Session):
    return db.query(User).filter(
        User.role == "candidate"
    ).all()

def get_candidate_by_id(db, user_id):
    return db.query(User).filter(User.id == user_id).first()



