from fastapi import APIRouter, UploadFile, File, Form

from app.services.descarga_service import descargar_paquete

router = APIRouter()


@router.post("/descarga/{package_id}")
async def descarga(
    package_id: str,
    cert_password: str = Form(...),
    cer_file: UploadFile = File(...),
    key_file: UploadFile = File(...)
):

    cer_bytes = await cer_file.read()
    key_bytes = await key_file.read()

    return descargar_paquete(
        package_id=package_id,
        cert_password=cert_password,
        cer_bytes=cer_bytes,
        key_bytes=key_bytes
    )