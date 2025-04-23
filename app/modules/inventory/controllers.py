from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi.encoders import jsonable_encoder
from app.modules.inventory import schemas, services
from app.core.database import get_db

router = APIRouter(tags=["Inventario"])


@router.post("/", response_model=schemas.ItemOut)
def crear_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return services.crear_item(db, item)


@router.get("/", response_model=List[schemas.ItemOut])
def listar_items(db: Session = Depends(get_db)):
    items = services.listar_items(db)
    return [
        {
            **jsonable_encoder(item),
            "stock_disponible": item.stock_total - item.stock_alquilado
        } for item in items
    ]


@router.patch("/{item_id}/rentar", response_model=schemas.ItemOut)
def rentar_item(item_id: int, db: Session = Depends(get_db)):
    return services.rentar_item(db, item_id)


@router.patch("/{item_id}/devolver", response_model=schemas.ItemOut)
def devolver_item(item_id: int, db: Session = Depends(get_db)):
    return services.devolver_item(db, item_id)
