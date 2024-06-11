import time
import random
import listadeplavras
#Aqui você declara as cores
vermelho = '\033[31m'
verde = '\033[32m'
Azulo = '\033[34m'
Amarelo = '\033[33m'

#Aqui é
print('-=-'*20)
print('-=-'*6, "JOGO DA FORCA",'-=-'*6)
print('-=-'*20)

#Aqui você escolhe as opções
print("Gerando palavras...")
print("Escolha uma categoria: ")
print(Amarelo,'''1 - Fácil
2 - Média
3 - Dificil''')
print('-=-'*20)

opcao = input(str(" Digite a opçao desejada: "))
print(verde, "Aguarde, gerando palavras...")
time.sleep(5)

while opcao not in ["1", "2", "3", "4"]:
    print("Opção inválida. Tente novamente.")
    opcao = input(str("Digite a opçao desejada: "))

if  opcao == "1":
  palavras = listadeplavras.palavras_facil

elif opcao == "2":
  palavras = listadeplavras.palavras_medias

elif opcao == "3":
  palavras = listadeplavras.palavras_dificil

else:
    print("Opção inválida. Tente novamente.")
    exit()

palavra_secreta = random.choice(palavras)


letras_usuario = []
chances = 4
ganhou = False

while True:
    # Aqui vamos criar a lógica do jogo
    for letra in palavra_secreta:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chances")
    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra_secreta.lower():
        chances -= 1

    ganhou = True
    for letra in palavra_secreta:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break


if ganhou:
    print('-=-'*20)
    print(f"Parabéns, você ganhou. A palavra era: {palavra_secreta}")
    print('-=-'*20)
else:
    print('-=-'*20)
    print(f" Você perdeu! A palavra era: {palavra_secreta}")
    print('-=-'*20)