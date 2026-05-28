from app.services.verificacion_service import verificar_solicitud

respuesta = verificar_solicitud(
    "02de9d4e-129e-42b7-9b7e-25dcc6a5e5e7"
)

print(respuesta)