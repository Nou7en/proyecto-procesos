from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PlatoBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=120)
    descripcion: Optional[str] = Field(default=None, max_length=255)
    precio: float = Field(..., gt=0)
    disponible: bool = True


class PlatoCreate(PlatoBase):
    pass


class PlatoUpdate(BaseModel):
    nombre: Optional[str] = Field(default=None, min_length=2, max_length=120)
    descripcion: Optional[str] = Field(default=None, max_length=255)
    precio: Optional[float] = Field(default=None, gt=0)
    disponible: Optional[bool] = None


class Plato(PlatoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
