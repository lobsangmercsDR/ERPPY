from pydantic import BaseModel
from typing import Optional
from decimal import Decimal


class ItemBase(BaseModel):
    nombre: str
    tipo: str
    talla: str
    genero: str
    descripcion: Optional[str] = None
    estatus_renta: Optional[bool] = True
    condicion: str
    garantia: int
    precio_alquiler: Decimal
    marca: Optional[str] = None
    stock_total: int
    stock_alquilado: int = 0
    temporada: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemOut(ItemBase):
    id: int
    codigo: str

    class Config:
        orm_mode = True
