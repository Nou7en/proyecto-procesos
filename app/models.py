from sqlalchemy import Boolean, Column, Float, Integer, String

from .database import Base


class Plato(Base):
    __tablename__ = "platos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False, index=True)
    descripcion = Column(String(255), nullable=True)
    precio = Column(Float, nullable=False)
    disponible = Column(Boolean, default=True)
