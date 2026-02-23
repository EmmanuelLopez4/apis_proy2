from fastapi import APIRouter, HTTPException
from services.biometrico_service import BiometricoService

router = APIRouter(prefix="/biometrico", tags=["Biometrico"])


@router.get("/")
def home():
    return {"message": "API de Acceso Biométrico funcionando"}


@router.post("/registrar")
def registrar(nombre: str, cantidad: int = 10):
    try:
        return BiometricoService.registrar_usuario(nombre, cantidad)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/acceso")
def acceso():
    try:
        return BiometricoService.validar_acceso()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/eliminar/{nombre}")
def eliminar(nombre: str):
    try:
        return BiometricoService.eliminar_usuario(nombre)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))