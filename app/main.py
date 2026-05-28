from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.solicitud import router as solicitud_router
from app.routes.verificacion import router as verificacion_router
from app.routes.descarga import router as descarga_router

app = FastAPI()

app.include_router(solicitud_router)
app.include_router(verificacion_router)
app.include_router(descarga_router)
app.include_router(auth_router)

@app.get("/")
def home():

    return {
        "message": "SAT Microservice Running"
    }