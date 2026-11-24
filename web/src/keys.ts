import { createHash, generateKeyPairSync, createDiffieHellman, createECDH, createCipheriv, diffieHellman } from 'crypto';

export const sha1 = (s: string) => createHash('sha1').update(s).digest('hex');
export const ecKey = () => generateKeyPairSync('ec', { namedCurve: 'P-256' });
export const rsaKey = () => generateKeyPairSync('rsa', { modulusLength: 2048 });
export const xa = generateKeyPairSync('x25519');
export const xb = generateKeyPairSync('x25519');
export const shared = diffieHellman({ privateKey: xa.privateKey, publicKey: xb.publicKey });
export const classicDh = () => createDiffieHellman(2048);
export const cbc128 = (key: Buffer, iv: Buffer) => createCipheriv('aes-128-cbc', key, iv);
export const gcm256 = (key: Buffer, iv: Buffer) => createCipheriv('aes-256-gcm', key, iv);
