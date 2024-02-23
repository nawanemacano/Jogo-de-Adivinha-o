from random import randint

seu_nome = input("olá! Qual o seu nome? ")
print(f'Okay!) {seu_nome}, eu estou escolhendo um número de 1 até 10. Você consegue adivinhar qual?
      ')
numero_adivinhado = randint(1, 10)
numero_tentativas = 3

for tentativa in range(1, numero_tentativas):
    numero_escolhido = int(input("Escolha um número: "))
    if numero_escolhido == numero_adivinhado:
        print(f'Você acertou em {numero_tentativas} tentativas: O número era {numero_adivinhado}!')
    break
elif numero_escolhido > numero_adivinhado:
print("Escolha um número menor")
else:
print("Escolha um número maior:")
print("Obrigada por jogar!")