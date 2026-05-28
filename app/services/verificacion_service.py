from app.services.sat_service import conectar_sat

ESTADOS_SOLICITUD = {
    1: "Aceptada",
    2: "En proceso",
    3: "Terminada",
    4: "Error",
    5: "Rechazada"
}

def verificar_solicitud(id_solicitud):

    sat = conectar_sat()

    respuesta = sat.recover_comprobante_status(
        id_solicitud
    )
    
    respuesta["EstadoDescripcion"] = ESTADOS_SOLICITUD.get(
        respuesta["EstadoSolicitud"],
        "Desconocido"
    )

    return respuesta