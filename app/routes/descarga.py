from fastapi import APIRouter
from app.services.descarga_service import descargar_paquete

router = APIRouter()


@router.get("/descarga/{package_id}")
def descarga(package_id: str):

    respuesta = descargar_paquete(package_id)

    return respuesta