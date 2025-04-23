from sqlalchemy import Column, Integer, String, Text, Boolean, Numeric
from app.core.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    talla = Column(String(20), nullable=False)
    genero = Column(String(10), nullable=False)
    codigo = Column(String(30), unique=True, index=True, nullable=False)
    descripcion = Column(Text, nullable=True)
    estatus_renta = Column(Boolean, default=True)
    condicion = Column(String(30), nullable=False)
    garantia = Column(Integer, nullable=False)
    precio_alquiler = Column(Numeric(10, 2), nullable=False)
    marca = Column(String(50), nullable=True)
    stock_total = Column(Integer, nullable=False, default=1)
    stock_alquilado = Column(Integer, nullable=False, default=0)
    temporada = Column(String(50), nullable=True)
