import random

palavra = ["python", "stefany", "mirela", "abacaxi", "emanuel"]
letras = []
chances = 6
ganhou = False

n = random.randint(0,4)
palavra_escolhida = palavra[n]
print(palavra_escolhida)

while True:
    for i in palavra_escolhida:
        if i.lower() in letras:
            print(i, end=" ")
        else:
            print('_', end=" ")
            
    print(f"Você tem {chances} chances")
    tentativa = input("Escolha uma letra para adivinhar: ") 
    letras.append(tentativa.lower())
    print(letras)
    
    if tentativa.lower() not in palavra_escolhida.lower():
        chances -= 1
        print(chances)
 
'''    ----------
    |         |
    |       \ O /
    |         |
    |        / \ 
    |
    -'''