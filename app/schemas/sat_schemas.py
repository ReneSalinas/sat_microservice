from pydantic import BaseModel
from datetime import datetime


class AuthRequest(BaseModel):

    rfc: str
    cert_password: str
    cert_path: str
    key_path: str


class SolicitudRequest(BaseModel):

    fecha_inicial: datetime
    fecha_final: datetime
    rfc_emisor: str