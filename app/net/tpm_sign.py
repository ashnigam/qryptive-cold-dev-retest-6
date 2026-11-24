from tpm2_pytss import ESAPI, TPM2B_PUBLIC, TPMT_PUBLIC
from tpm2_pytss.constants import TPM2_ALG

def sign_in_tpm(digest):
    with ESAPI() as ectx:
        template = TPM2B_PUBLIC.parse("rsa2048:rsassa-sha256:null")
        handle, pub, *_ = ectx.create_primary(None, template)
        return ectx.sign(handle, digest, None, None)
