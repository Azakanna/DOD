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
        password=Hasher().generate_hash(user.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(email: str, password: str, db: Session):
    user = get_user(email=email, db=db)
    if not user:
        return False
    if not Hasher().check_password(password, user.password):
        return False
    return user

def get_users(db: Session):
    return db.query(User).all()