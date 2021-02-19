def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    a_first = ord("a")
    z_last = ord("z")
    A_first = ord("A")
    Z_last = ord("Z")
    language = 26
    if int(len(keyword)) < int(len(plaintext)):
        keyword = keyword * int(len(plaintext))
        keyword = keyword[: len(plaintext)]
    for i, j in zip(keyword, plaintext):
        code_letter = ord(j)
        code_letter_keyword = ord(i)
        if a_first <= code_letter_keyword <= z_last:
            shift = code_letter_keyword - a_first
        elif A_first <= code_letter_keyword <= Z_last:
            shift = code_letter_keyword - A_first
        if a_first <= code_letter <= z_last:
            k = chr((code_letter - a_first + shift) % language + a_first)
            ciphertext += k
        elif A_first <= code_letter <= Z_last:
            k = chr((code_letter - A_first + shift) % language + A_first)
            ciphertext += k
        else:
            ciphertext += j

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    a_first = ord("a")
    z_last = ord("z")
    A_first = ord("A")
    Z_last = ord("Z")
    language = 26
    if int(len(keyword)) < int(len(ciphertext)):
        keyword = keyword * int(len(ciphertext))
        keyword = keyword[: len(ciphertext)]
    for i, j in zip(keyword, ciphertext):
        code_letter = ord(j)
        code_letter_keyword = ord(i)
        if a_first <= code_letter_keyword <= z_last:
            shift = code_letter_keyword - a_first
        elif A_first <= code_letter_keyword <= Z_last:
            shift = code_letter_keyword - A_first
        if a_first <= code_letter <= z_last:
            check_negative = code_letter - a_first - shift
            if check_negative < 0:
                check_negative = (language - (check_negative * (-1) % language)) % language
            k = chr(check_negative + a_first)
            plaintext += k
        elif A_first <= code_letter <= Z_last:
            check_negative = code_letter - A_first - shift
            if check_negative < 0:
                check_negative = (language - (check_negative * (-1) % language)) % language
            k = chr(check_negative + A_first)
            plaintext += k
        else:
            plaintext += j

    return plaintext
