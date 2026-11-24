from cryptography.hazmat.primitives.asymmetric import ec, x25519, dh

def ecdh_flow(peer_public):
    key = ec.generate_private_key(ec.SECP256R1())
    return key.exchange(ec.ECDH(), peer_public)

def x25519_flow(peer_public):
    key = x25519.X25519PrivateKey.generate()
    return key.exchange(peer_public)

def dh_flow(peer_public, p, g):
    parameters = dh.DHParameterNumbers(p, g).parameters()
    key = parameters.generate_private_key()
    return key.exchange(peer_public)
