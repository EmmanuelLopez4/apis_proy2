# models/usuario.py

from pydantic import BaseModel, Field
from typing import Optional


class UsuarioCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=50)


class UsuarioResponse(BaseModel):
    mensaje: str


class AccesoResponse(BaseModel):
    acceso: str
    usuario: Optional[str] = None
    mensaje: Optional[str] = None