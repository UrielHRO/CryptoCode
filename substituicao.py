# Algoritmo para cifras de Substituição 
import string
import random

# Gera automaticamente um alfabeto embaralhado
def gerar_chave():
    letras = list(string.ascii_lowercase)
    random.shuffle(letras)
    return dict(zip(string.ascii_lowercase, letras))


def encrypt(texto: str, chave: dict) -> str:
    resultado = ""
    for c in texto.lower():
        if c in chave:
            resultado += chave[c]
        else:
            resultado += c
    return resultado


def decrypt(texto: str, chave: dict) -> str:
    reversa = {v: k for k, v in chave.items()}
    resultado = ""
    for c in texto.lower():
        if c in reversa:
            resultado += reversa[c]
        else:
            resultado += c
    return resultado
