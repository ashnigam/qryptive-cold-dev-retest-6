from jwcrypto import jwe, jwk

def encrypt_session(payload, key_json):
    key = jwk.JWK.from_json(key_json)
    token = jwe.JWE(payload, {"alg": "RSA-OAEP", "enc": "A256GCM"})
    token.add_recipient(key)
    return token.serialize()
