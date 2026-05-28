from fastapi import APIRouter
from app.schemas.sat_schemas import AuthRequest
from app.services.auth_service import autenticar_sat

router = APIRouter(
    prefix="/sat",
    tags=["SAT"]
)


@router.post("/auth")
def auth(data: AuthRequest):

    token = autenticar_sat(
        rfc=data.rfc,
        cert_password=data.cert_password,
        cert_path=data.cert_path,
        key_path=data.key_path
    )

    return {
        "success": True,
        "token": token
    }