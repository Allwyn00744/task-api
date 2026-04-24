from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import UserModel
from schemas import UserRegister,UserLogin
from utils.hash import hash_password,verify_password
from utils.jwt_handler import create_access_token

def register_user_service(db: Session, user: UserRegister):
    existing_user = db.query(UserModel).filter(
        UserModel.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = UserModel(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user_service(db:Session, user:UserLogin):
    existing_user=db.query(UserModel).filter(UserModel.email==user.email).first()
    if not existing_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )
    is_password_correct = verify_password(user.password,existing_user.password)
    if not is_password_correct:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )
    token = create_access_token(
    {"user_id": existing_user.id}
    )

    return {
        "access_token": token
    }