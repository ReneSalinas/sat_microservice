from satcfdi.models.signer import Signer
from app.config import settings

with open(settings.CERT_PATH, "rb") as cer_file:
    cer = cer_file.read()

with open(settings.KEY_PATH, "rb") as key_file:
    key = key_file.read()

fiel = Signer.load(
    certificate=cer,
    key=key,
    password=settings.CERT_PASSWORD
)

print("RFC:", fiel.rfc)
print("Nombre:", fiel.legal_name)