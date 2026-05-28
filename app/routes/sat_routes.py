from fastapi import APIRouter

from app.services.sat_service import autenticar_sat

router = APIRouter(
    prefix="/sat",
    tags=["SAT"]
)

@router.get("/auth")
def auth():

    response = autenticar_sat()

    return {
        "token": response
    }