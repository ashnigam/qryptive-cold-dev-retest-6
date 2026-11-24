import ssl

def make_client():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.minimum_version = ssl.TLSVersion.TLSv1
    ctx.load_default_certs()
    return ctx
