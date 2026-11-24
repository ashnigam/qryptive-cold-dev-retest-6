from Crypto.Cipher import DES, ARC4, Blowfish
from Crypto.Random import get_random_bytes

def old_des(key, data):
    return DES.new(key, DES.MODE_CBC, get_random_bytes(8)).encrypt(data)

def old_rc4(key, data):
    return ARC4.new(key).encrypt(data)

def old_bf(key, data):
    return Blowfish.new(key, Blowfish.MODE_ECB).encrypt(data)
