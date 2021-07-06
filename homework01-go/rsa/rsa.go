package rsa

import (
	"errors"
	"math/big"
	"math/rand"
)

type Key struct {
	key int
	n   int
}

type KeyPair struct {
	Private Key
	Public  Key
}

func isPrime(n int) bool {
	if n == 1 {
		return false
	}
	for i := 2; i < n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func gcd(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func multiplicativeInverse(e int, phi int) int {
	var a, b = e, phi
	if b > a {
		a, b = b, a
	}
	s1 := []int{a}
	s2 := []int{b}
	n := 0
	for a%b != 0 {
		n++
		a, b = b, a%b
		s1 = append(s1, a)
		s2 = append(s2, b)
	}

	x := 0
	y := 1
	for n > 0 {
		a = s1[n-1]
		b = s2[n-1]
		x, y = y, x-(a/b)*y
		n--
	}
	if y < 0 {
		y += phi
	}
	return y % phi
}

func GenerateKeypair(p int, q int) (KeyPair, error) {
	if !isPrime(p) || !isPrime(q) {
		return KeyPair{}, errors.New("Both numbers must be prime.")
	} else if p == q {
		return KeyPair{}, errors.New("p and q can't be equal.")
	}

	n := p * q
	phi := (p - 1) * (q - 1)

	e := rand.Intn(phi-1) + 1
	g := gcd(e, phi)
	for g != 1 {
		e = rand.Intn(phi-1) + 1
		g = gcd(e, phi)
	}

	d := multiplicativeInverse(e, phi)
	return KeyPair{Key{e, n}, Key{d, n}}, nil
}

func Encrypt(pk Key, plaintext string) []int {
	cipher := []int{}
	n := new(big.Int)
	for _, ch := range plaintext {
		n = new(big.Int).Exp(
			big.NewInt(int64(ch)), big.NewInt(int64(pk.key)), nil)
		n = new(big.Int).Mod(n, big.NewInt(int64(pk.n)))
		cipher = append(cipher, int(n.Int64()))
	}
	return cipher
}

func Decrypt(pk Key, cipher []int) string {
	plaintext := ""
	n := new(big.Int)
	for _, ch := range cipher {
		n = new(big.Int).Exp(
			big.NewInt(int64(ch)), big.NewInt(int64(pk.key)), nil)
		n = new(big.Int).Mod(n, big.NewInt(int64(pk.n)))
		plaintext += string(rune(int(n.Int64())))
	}
	return plaintext
}
