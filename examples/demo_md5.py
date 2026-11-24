"""Example only: shows how NOT to hash."""
import hashlib

def demo():
    return hashlib.md5(b"example").hexdigest()
