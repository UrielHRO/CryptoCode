def encrypt(texto: str, chave: int) -> str:
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + chave) % 26 + base)
        else:
            resultado += c
    return resultado


def decrypt(texto: str, chave: int) -> str:
    return encrypt(texto, -chave)
