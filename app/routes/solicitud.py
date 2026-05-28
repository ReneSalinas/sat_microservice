from fastapi import APIRouter, HTTPException
from app.schemas.sat_schemas import SolicitudRequest
from app.services.solicitud_service import crear_solicitud

router = APIRouter()


@router.post("/solicitud")
def solicitud(data: SolicitudRequest):

    if data.fecha_inicial >= data.fecha_final:

        raise HTTPException(
            status_code=400,
            detail="La fecha inicial debe ser menor a la final"
        )

    return crear_solicitud(
        fecha_inicial=data.fecha_inicial,
        fecha_final=data.fecha_final,
        rfc_emisor=data.rfc_emisor
    )