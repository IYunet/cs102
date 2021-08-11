import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    a_first = ord("a")
    z_last = ord("z")
    A_first = ord("A")
    Z_last = ord("Z")
    language = 26
    for i in range(len(plaintext)):
        code_letter = ord(plaintext[i])
        if a_first <= code_letter <= z_last:
            k = chr((code_letter - a_first + shift) % language + a_first)
            ciphertext += k
        elif A_first <= code_letter <= Z_last:
            k = chr((code_letter - A_first + shift) % language + A_first)
            ciphertext += k
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    a_first = ord("a")
    z_last = ord("z")
    A_first = ord("A")
    Z_last = ord("Z")
    language = 26
    for i in range(len(ciphertext)):
        code_letter = ord(ciphertext[i])
        if a_first <= code_letter <= z_last:
            check_negative = code_letter - a_first - shift
            if check_negative < 0:
                check_negative = (
                    language - (check_negative * (-1) % language)
                ) % language
            k = chr(check_negative + a_first)
            plaintext += k
        elif A_first <= code_letter <= Z_last:
            check_negative = code_letter - A_first - shift
            if check_negative < 0:
                check_negative = (
                    language - (check_negative * (-1) % language)
                ) % language
            k = chr(check_negative + A_first)
            plaintext += k
        else:
            plaintext += ciphertext[i]

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
