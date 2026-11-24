package com.acme;
import java.security.*;
import javax.crypto.*;

public class Crypto {
    public KeyPair ecKey() throws Exception {
        KeyPairGenerator g = KeyPairGenerator.getInstance("EC");
        g.initialize(256);
        return g.generateKeyPair();
    }
    public byte[] sign(PrivateKey k, byte[] d) throws Exception {
        Signature s = Signature.getInstance("SHA256withECDSA");
        s.initSign(k); s.update(d); return s.sign();
    }
    public byte[] sha1(byte[] d) throws Exception {
        return MessageDigest.getInstance("SHA-1").digest(d);
    }
    public byte[] tripleDes(byte[] d, SecretKey k) throws Exception {
        Cipher c = Cipher.getInstance("DESede/CBC/PKCS5Padding");
        c.init(Cipher.ENCRYPT_MODE, k); return c.doFinal(d);
    }
    public KeyAgreement dh() throws Exception {
        return KeyAgreement.getInstance("DH");
    }
    public SecretKey aes128() throws Exception {
        KeyGenerator g = KeyGenerator.getInstance("AES");
        g.init(128);
        return g.generateKey();
    }
    public SecretKey aes256() throws Exception {
        KeyGenerator g = KeyGenerator.getInstance("AES");
        g.init(256);
        return g.generateKey();
    }
}
