from satcfdi.models.signer import Signer
from satcfdi.pacs.sat import SAT


def autenticar_sat(
    rfc,
    cert_password,
    cert_path,
    key_path
):

    with open(cert_path, "rb") as cer_file:
        cer = cer_file.read()

    with open(key_path, "rb") as key_file:
        key = key_file.read()

    fiel = Signer.load(
        certificate=cer,
        key=key,
        password=cert_password
    )

    sat = SAT(fiel)

    token = sat._get_token_comprobante()

    print("TOKEN SAT:")
    print(token)

    return token