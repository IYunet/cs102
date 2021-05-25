package vigenere

import "strings"

func EncryptVigenere(plaintext string, keyword string) string {
	var ciphertext string
	var language int = 26

	razn := len(plaintext) - len(keyword)
	k_word := len(keyword)
	for i := 0; i < razn; i++ {
		keyword = keyword + string(keyword[i%k_word])
	}
	keyword = strings.ToLower(keyword)

	for i := 0; i < len(plaintext); i++ {
		shift := int(keyword[0]) - int('a')
		keyword = keyword[1:]
		sym_num := int(plaintext[i])
		if (int('A') <= sym_num) && (sym_num <= int('Z')) {
			sym_num = (int(sym_num)+shift-int('A'))%language + int('A')
		} else if (int('a') <= sym_num) && (sym_num <= int('z')) {
			sym_num = (int(sym_num)+shift-int('a'))%language + int('a')
		}
		ciphertext += string(rune(sym_num))
	}
	return ciphertext
}

func DecryptVigenere(ciphertext string, keyword string) string {
	var plaintext string
	var language int = 26

	razn := len(ciphertext) - len(keyword)
	k_word := len(keyword)
	for i := 0; i < razn; i++ {
		keyword = keyword + string(keyword[i%k_word])
	}
	keyword = strings.ToLower(keyword)

	for i := 0; i < len(ciphertext); i++ {
		shift := int(keyword[0]) - int('a')
		keyword = keyword[1:]
		sym_num := int(ciphertext[i])
		if (int('A') <= sym_num) && (sym_num <= int('Z')) {
			sym_num = (sym_num-shift-int('A')+language)%language + int('A')
		} else if (int('a') <= sym_num) && (sym_num <= int('z')) {
			sym_num = (sym_num-shift-int('a')+language)%language + int('a')
		}
		plaintext += string(rune(sym_num))
	}
	return plaintext
}
