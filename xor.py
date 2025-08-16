# Algoritmo para cifra de XOR

def encrypt(texto: str, chave: int) -> str:
    return "".join(chr(ord(c) ^ chave) for c in texto)


def decrypt(texto: str, chave: int) -> str:
    # XOR é reversível com a mesma chave
    return "".join(chr(ord(c) ^ chave) for c in texto)
