# inspect_vigencia.py

from app.services.sat_service import conectar_sat

sat = conectar_sat()

cert = sat.signer

print(cert.certificate.get_notBefore())
print(cert.certificate.get_notAfter())