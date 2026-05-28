from app.services.sat_service import conectar_sat
import inspect

sat = conectar_sat()

print(
    inspect.signature(
        sat.recover_comprobante_received_request
    )
)