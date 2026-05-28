# from datetime import datetime, timedelta
# from app.services.sat_service import conectar_sat
# from app.config import settings

# def crear_solicitudEMITIDOS():

#     sat = conectar_sat()

#     fecha_final = datetime.now()
#     fecha_inicial = fecha_final - timedelta(days=7)

#     respuesta = sat.recover_comprobante_emitted_request(
#         fecha_inicial=fecha_inicial,
#         fecha_final=fecha_final,
#         rfc_emisor=settings.RFC,
#     )

#     return respuesta

# def crear_solicitud():

#     sat = conectar_sat()

#     fecha_final = datetime.now()
#     fecha_inicial = fecha_final - timedelta(days=7)

#     respuesta = sat.recover_comprobante_emitted_request(
#         fecha_inicial=fecha_inicial,
#         fecha_final=fecha_final,
#         rfc_emisor=settings.RFC,
#     )

#     return respuesta

from fastapi import HTTPException
from app.services.sat_service import conectar_sat


def crear_solicitud(
    fecha_inicial,
    fecha_final,
    rfc_emisor,
    cert_password,
    cer_bytes,
    key_bytes
):

    try:

        sat = conectar_sat(
            cert_password=cert_password,
            cer_bytes=cer_bytes,
            key_bytes=key_bytes
        )

        respuesta = sat.recover_comprobante_emitted_request(
            fecha_inicial=fecha_inicial,
            fecha_final=fecha_final,
            rfc_emisor=rfc_emisor
        )

        cod_estatus = respuesta.get("CodEstatus")

        if cod_estatus != "5000":

            raise HTTPException(
                status_code=400,
                detail=respuesta.get("Mensaje")
            )

        return respuesta

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )