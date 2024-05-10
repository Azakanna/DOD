from app.application.hash import Hasher
from app.application.schemas import UserCreate
from app.db.models.user import User
from sqlalchemy.orm import Session


def get_user(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user

def create_new_user(user: UserCreate, db: Session):
    user = User(
        email=user.email,
        password=Hasher.generate_hash(user.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user