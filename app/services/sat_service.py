from satcfdi.pacs.sat import SAT
from satcfdi.models.signer import Signer
from app.config import settings


def conectar_sat():

    with open(settings.CERT_PATH, "rb") as cer_file:
        cer = cer_file.read()

    with open(settings.KEY_PATH, "rb") as key_file:
        key = key_file.read()

    fiel = Signer.load(
        certificate=cer,
        key=key,
        password=settings.CERT_PASSWORD
    )

    sat = SAT(fiel)

    return sat