from fastapi import FastAPI
from app.core.database import Base, engine
from app.modules.auth.models import User
from app.modules.inventory.models import Item
from app.modules.auth.controllers import router as auth_router
from app.modules.inventory.controllers import router as inventory_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rutas
app.include_router(auth_router, prefix="/users", tags=["Users"])
app.include_router(inventory_router, prefix="/inventory", tags=["Inventario"])


@app.get("/")
def home():
    return {"message": "ERP backend activo"}
