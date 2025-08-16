import cesar
import vigenere
import xor
import substituicao

def main():
    print("=== FERRAMENTA DE CRIPTOGRAFIA ===")
    print("1 - Cesar")
    print("2 - Vigenere")
    print("3 - XOR")
    print("4 - Substituicao")

    opcao = input("Escolha a cifra: ")

    acao = input("Deseja (E)ncriptar ou (D)ecriptar? ").lower()
    texto = input("Digite o texto: ")

    if opcao == "1":
        chave = int(input("Digite a chave (numero): "))
        if acao == "e":
            print("Resultado:", cesar.encrypt(texto, chave))
        else:
            print("Resultado:", cesar.decrypt(texto, chave))

    elif opcao == "2":
        chave = input("Digite a chave (palavra): ")
        if acao == "e":
            print("Resultado:", vigenere.encrypt(texto, chave))
        else:
            print("Resultado:", vigenere.decrypt(texto, chave))

    elif opcao == "3":
        chave = int(input("Digite a chave (numero): "))
        if acao == "e":
            print("Resultado:", xor.encrypt(texto, chave))
        else:
            print("Resultado:", xor.decrypt(texto, chave))

    elif opcao == "4":
        print("Obs: sera gerada uma chave de substituição aleatoria.")
        chave = substituicao.gerar_chave()
        print("Chave gerada:", chave)
        if acao == "e":
            print("Resultado:", substituicao.encrypt(texto, chave))
        else:
            print("Resultado:", substituicao.decrypt(texto, chave))

    else:
        print("Opcao invalida.")


if __name__ == "__main__":
    main()
