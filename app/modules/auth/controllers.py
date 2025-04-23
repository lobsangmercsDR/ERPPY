from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from app.modules.auth import schemas, services
from app.core.config import settings
from app.modules.auth.token import create_access_token
from app.modules.auth.models import User

router = APIRouter()


@router.post("/register", response_model=schemas.UserOut)
def register(user_data: schemas.UserCreate, db: Session = Depends(services.get_db)):
    return services.create_user(db, user_data)


@router.post("/login", response_model=schemas.Token)
def login(email: str, password: str, db: Session = Depends(services.get_db)):
    user = services.authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=schemas.UserOut)
def get_profile(current_user: User = Depends(services.get_current_user)):
    return current_user
