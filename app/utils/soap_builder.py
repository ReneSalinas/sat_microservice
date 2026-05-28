from datetime import datetime
import uuid

def build_auth_xml():
    
    unique_id = str(uuid.uuid4())

    created = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    xml = f"""
    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
        
        <s:Header>
            <o:Security s:mustUnderstand="1"
            xmlns:o="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">

                <u:Timestamp u:Id="_0">
                    <u:Created>{created}</u:Created>
                    <u:Expires>{created}</u:Expires>
                </u:Timestamp>

            </o:Security>
        </s:Header>

        <s:Body>
            <Autentica xmlns="http://DescargaMasivaTerceros.gob.mx"/>
        </s:Body>

    </s:Envelope>
    """

    return xml