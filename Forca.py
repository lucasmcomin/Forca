and import random
import os
import time
from unicodedata import normalize


palavras = ("Zebra", "Vaca", "Cachorro", "Desfiladeiro", "Rabanete", "Raposa", "Tijolo", "Reboco",
           "Tomada", "Rápido", "Música", "Trompete", "Criança", "Responsabilidade","Oportunidade", "Esperança", "Parede", "Armamento", "Ar condicionado", "Salva-vidas", "Alto - Mar")


forca_desig={0:("|‾ ‾ ‾ ‾|",
                "|       |",
                "|       |",
                "|       |",
                "|_______|"),
             1:("|‾ ‾ ‾ ‾|",
                "|   o   |",
                "|       |",
                "|       |",
                "|_______|"),
             2:("|‾ ‾ ‾ ‾|",
                "|   o   |",
                "|   |   |",
                "|       |",
                "|_______|"),
             3:("|‾ ‾ ‾ ‾|",
                "|   o   |",
                "|  /|   |",
                "|       |",
                "|_______|"),
             4:("|‾ ‾ ‾ ‾|",
                "|   o   |",
                "|  /|\\  |",
                "|       |",
                "|_______|"),
             5:("|‾ ‾ ‾ ‾|",
                "|   o   |",
                "|  /|\\  |",
                "|  /    |",
                "|_______|"),
             6:("|‾ ‾ ‾ ‾|",
                "|   o   |",
                "|  /|\\  |",
                "|  / \\  |",
                "|_______|")}


def display_forca(error):
    for line in forca_desig[error]:
        print(line)
    print()

def fornecedor_palavra():
    palavra_secreta = random.choice(palavras)
    palavra_under = ["_"] * len(palavra_secreta)
    if " " in palavra_secreta:
        i = palavra_secreta.index(" ")
        palavra_under.insert(i, " ")
        palavra_under.pop()

    if "-" in palavra_secreta:
        i = palavra_secreta.index("-")
        palavra_under.insert(i, "-")
        palavra_under.pop()

    return palavra_secreta, palavra_under


def verifica_palpite(palpite, secreta, under_secreta):
    errou = True
    sec = normalize('NFKD', secreta).encode('ASCII','ignore').decode('ASCII')
    if palpite.lower() in sec.lower():
        for i in range(len(secreta)):
            if sec[i].lower() == palpite.lower():
                under_secreta[i] = secreta[i]
        errou = False
    return under_secreta, errou

def verifica_letra(palpite):
    if(len(palpite) == 1 and palpite.isalpha()):
        return True
    else:
        print("Opção inválida! Seu palpite deve ser uma letra!!!!!")
        return False


def imprimir_lista(lista):
    print(" ".join(lista))



def main():
    lista_palpite = []
    erros = 0
    secreta, under_secreta = fornecedor_palavra()
    rodar = True
    erros = 0

    while rodar:
        os.system('clear')
        print("**************************************")
        print("             JOGO DA FORCA            ")
        print("\n")
        display_forca(erros)
        imprimir_lista(under_secreta)
        print("\n")

        if not "_" in under_secreta:
            print("**********************  Parabéns!!! Você Ganhou  **********************")
            break

        if erros == 6:
            print("O jogo acabou, você perdeu!!!")
            print(f"A palavra secreta é: {secreta}")
            break

        palpite = input("Digite um palpite de letra: ")

        if not verifica_letra(palpite):
            time.sleep(3)
            continue

        if palpite in lista_palpite:
            print("\nPalpite já feito anteriormente, escolha outra letra!\n")
            time.sleep(3)
            continue

        lista_palpite.append(palpite)


        under_secreta, errou = verifica_palpite(palpite, secreta, under_secreta)

        if errou:
            erros +=1

if __name__ == '__main__':
    main()



