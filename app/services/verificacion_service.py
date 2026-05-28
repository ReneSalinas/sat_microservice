from app.services.sat_service import conectar_sat

ESTADOS_SOLICITUD = {
    1: "Aceptada",
    2: "En proceso",
    3: "Terminada",
    4: "Error",
    5: "Rechazada"
}

def verificar_solicitud(
    id_solicitud,
    cert_password,
    cer_bytes,
    key_bytes
):

    sat = conectar_sat(
        cert_password=cert_password,
        cer_bytes=cer_bytes,
        key_bytes=key_bytes
    )

    respuesta = sat.recover_comprobante_status(
        id_solicitud
    )
    
    respuesta["EstadoDescripcion"] = ESTADOS_SOLICITUD.get(
        respuesta["EstadoSolicitud"],
        "Desconocido"
    )

    return respuesta