from fastapi import APIRouter
from app.services.verificacion_service import verificar_solicitud

router = APIRouter()


@router.get("/verificacion/{id_solicitud}")
def verificacion(id_solicitud: str):

    respuesta = verificar_solicitud(id_solicitud)

    return respuesta