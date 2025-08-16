def gerar_chave(texto: str, chave: str) -> str:
    chave = chave.lower()
    return (chave * (len(texto) // len(chave) + 1))[:len(texto)]


def encrypt(texto: str, chave: str) -> str:
    resultado = ""
    chave = gerar_chave(texto, chave)
    for i, c in enumerate(texto):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            k = ord(chave[i].lower()) - ord('a')
            resultado += chr((ord(c) - base + k) % 26 + base)
        else:
            resultado += c
    return resultado


def decrypt(texto: str, chave: str) -> str:
    resultado = ""
    chave = gerar_chave(texto, chave)
    for i, c in enumerate(texto):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            k = ord(chave[i].lower()) - ord('a')
            resultado += chr((ord(c) - base - k) % 26 + base)
        else:
            resultado += c
    return resultado
