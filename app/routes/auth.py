from fastapi import APIRouter, UploadFile, File, Form
from app.services.sat_service import autenticar_sat

router = APIRouter(
    prefix="/sat",
    tags=["SAT"]
)


@router.post("/auth")
async def auth(
    rfc: str = Form(...),
    cert_password: str = Form(...),
    cer_file: UploadFile = File(...),
    key_file: UploadFile = File(...)
):

    cer_bytes = await cer_file.read()
    key_bytes = await key_file.read()

    token = autenticar_sat(
        rfc=rfc,
        cert_password=cert_password,
        cer_bytes=cer_bytes,
        key_bytes=key_bytes
    )

    return {
        "success": True,
        "token": token
    }