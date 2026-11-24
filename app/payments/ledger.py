import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography.hazmat.primitives import hashes

def checksum(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()

def fingerprint(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()

def new_signing_key():
    return rsa.generate_private_key(public_exponent=65537, key_size=3072)

def sign_entry(rsa_key, entry: bytes):
    return rsa_key.sign(entry, padding.PKCS1v15(), hashes.SHA256())

def audit_key():
    return ec.generate_private_key(ec.SECP256R1())

def sign_audit(ec_key, entry: bytes):
    return ec_key.sign(entry, ec.ECDSA(hashes.SHA256()))
