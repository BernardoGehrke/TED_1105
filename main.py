import random

x = random.randint(1,100)
palpite = 1
print('Digite um número de 1 a 100:', end= " ")
valor = int(input())

if valor<x:
        print('Seu palpite foi menor')
elif valor>x:
        print('O seu palpite foi maior')
if not 1<= valor <=100:
        print('O número deve ser entre 1 e 100')
while valor is not x:
    palpite+=1
    valor = int(input("Digite um número de 1 a 100: "))
    if valor<x:
        print('Seu palpite foi menor')
    elif valor>x:
        print('O seu palpite foi maior')
    if not 1<= valor <=100:
        print('O número deve ser entre 1 e 100')
else:
    print("Parabéns! O número aleatório era",x,"! Você descobriu o número em",palpite, "tentativas!")
