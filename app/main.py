from fastapi import FastAPI
from app.core.database import Base, engine
from app.modules.auth.models import User
from app.modules.auth.controllers import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rutas
app.include_router(auth_router, prefix="/users", tags=["Users"])
