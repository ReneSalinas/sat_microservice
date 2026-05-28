from fastapi import APIRouter, UploadFile, File, Form
from datetime import datetime

from app.services.solicitud_service import crear_solicitud

router = APIRouter(
    tags=["Solicitud"]
)


@router.post("/solicitud")
async def solicitud(
    fecha_inicial: datetime = Form(...),
    fecha_final: datetime = Form(...),
    rfc_emisor: str = Form(...),
    cert_password: str = Form(...),
    cer_file: UploadFile = File(...),
    key_file: UploadFile = File(...)
):

    cer_bytes = await cer_file.read()
    key_bytes = await key_file.read()

    return crear_solicitud(
        fecha_inicial=fecha_inicial,
        fecha_final=fecha_final,
        rfc_emisor=rfc_emisor,
        cert_password=cert_password,
        cer_bytes=cer_bytes,
        key_bytes=key_bytes
    )