import random
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.modules.inventory.schemas import ItemCreate
from app.modules.inventory.models import Item


def generar_codigo(tipo: str, db: Session) -> str:
    prefix = tipo.strip().upper()[:3]
    while True:
        numero = random.randint(1000, 9999)
        codigo = f"{prefix}{numero}"
        if not db.scalar(select(Item).where(Item.codigo == codigo)):
            return codigo


def crear_item(db: Session, data: ItemCreate) -> Item:
    codigo = generar_codigo(data.tipo, db)
    item = Item(**data.model_dump(), codigo=codigo)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def listar_items(db: Session):
    return db.query(Item).all()


def rentar_item(db: Session, item_id: int) -> Item:
    item: Item | None = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")

    # Accede a valores concretos
    if (item.stock_total - item.stock_alquilado) <= 0:  # type: ignore
        raise HTTPException(
            status_code=400, detail="No hay unidades disponibles para alquilar")

    item.stock_alquilado += 1  # type: ignore # ✅ Valor real, no expresión SQL
    db.commit()
    db.refresh(item)
    return item


def devolver_item(db: Session, item_id: int) -> Item:
    item: Item | None = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")

    if item.stock_alquilado <= 0:  # type: ignore
        raise HTTPException(
            status_code=400, detail="No hay unidades en alquiler para devolver")

    item.stock_alquilado -= 1  # type: ignore # ✅ Valor real
    db.commit()
    db.refresh(item)
    return item
