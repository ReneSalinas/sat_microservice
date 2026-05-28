from fastapi import APIRouter, UploadFile, File, Form

from app.services.verificacion_service import verificar_solicitud

router = APIRouter(
    tags=["Verificacion"]
)


@router.post("/verificacion/{id_solicitud}")
async def verificacion(
    id_solicitud: str,
    cert_password: str = Form(...),
    cer_file: UploadFile = File(...),
    key_file: UploadFile = File(...)
):

    cer_bytes = await cer_file.read()
    key_bytes = await key_file.read()

    return verificar_solicitud(
        id_solicitud=id_solicitud,
        cert_password=cert_password,
        cer_bytes=cer_bytes,
        key_bytes=key_bytes
    )