from satcfdi.models.signer import Signer
from satcfdi.pacs.sat import SAT


def conectar_sat(
    cert_password,
    cer_bytes,
    key_bytes
):

    fiel = Signer.load(
        certificate=cer_bytes,
        key=key_bytes,
        password=cert_password
    )

    sat = SAT(fiel)

    return sat