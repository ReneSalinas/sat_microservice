from app.services.sat_service import conectar_sat
import base64
import os


def descargar_paquete(package_id):

    sat = conectar_sat()

    metadata, paquete = sat.recover_comprobante_download(
        package_id
    )

    if paquete:

        contenido_zip = base64.b64decode(paquete)

        nombre_archivo = f"{package_id}.zip"

        with open(nombre_archivo, "wb") as f:
            f.write(contenido_zip)

        print(f"ZIP guardado: {nombre_archivo}")

        return {
            "success": True,
            "metadata": metadata,
            "package_id": package_id,
            "zip_file": nombre_archivo,
            "zip_base64": paquete
        }

    return {
        "success": False,
        "metadata": metadata,
        "message": "No se pudo descargar el paquete"
    }