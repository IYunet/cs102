package caesar

func EncryptCaesar(plaintext string, shift int) string {
	var ciphertext string
	var language int = 26

	for i := 0; i < len(plaintext); i++ {
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

func DecryptCaesar(ciphertext string, shift int) string {
	var plaintext string
	var language int = 26

	for i := 0; i < len(ciphertext); i++ {
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
