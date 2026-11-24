package main

import (
	"crypto/md5"
	"crypto/rand"
	"crypto/rsa"
	"crypto/tls"
	"crypto/ecdh"
)

func main() {
	k, _ := rsa.GenerateKey(rand.Reader, 2048)
	_ = k
	x, _ := ecdh.X25519().GenerateKey(rand.Reader)
	_ = x
	_ = md5.Sum([]byte("edge"))
	_ = &tls.Config{MinVersion: tls.VersionTLS11}
}
