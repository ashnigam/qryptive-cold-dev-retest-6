from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class Vault:
    def session_key(self):
        return AESGCM.generate_key(bit_length=128)

    def master_key(self):
        return AESGCM.generate_key(bit_length=256)

    def seal(self, key, nonce, data):
        return AESGCM(key).encrypt(nonce, data, None)
