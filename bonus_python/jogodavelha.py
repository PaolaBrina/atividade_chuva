while True: 
    n = input("Você deseja jogar o jogo da velha?(S/N) ").upper()
    if n == "S":
        a = [[0,0,0] , [0,0,0] , [0,0,0]]
        jogada = 1
        if jogada == 1:
           print("Jogador X")
           for i in range(len(a)):
             print(a[i])
           l = int(input("Digite o valor da linha. [0, 1, 2]" ))
           c = int(input("Digite o valor da coluna. [0, 1, 2]" ))
           a[l][c] = "X"
           jogada += 1
        elif jogada == 2:
           print("Jogador O")
           for i in range(len(a)):
             print(a[i])
           l = int(input("Digite o valor da linha. [0, 1, 2]" ))
           c = int(input("Digite o valor da coluna. [0, 1, 2]" ))
           a[l][c] = "O"
           jogada -=1
        else:
            print("empate")       
        break
    if n == "N":
        print("Saindo do programa!")
        break
    if n != "N" or n != "S":
        print('Resposta invalida! Digite novamente: ')


''' print(a[2][0])'''
    
    
'''
Implementação do Jogo da Velha em Python

Dois jogadores "X" e "O", alternam turnos para marcar um espaço vazio no tabuleiro.
O objetivo é conseguir três marcas consecutivas (horizontal, vertical ou diagonal) para ganhar o jogo.
O jogo pode terminar em empate se não houver mais espaços vazios no tabuleiro.

Cada jogador insere sua marca em uma posição vazia no tabuleiro.


Garanta que o programa valide as entradas dos jogadores, verifique as vitórias e determine se houve um empate.
Exiba o tabuleiro após cada jogada e informe o vencedor ou o empate quando o jogo terminar.


Lembre-os de que as posições são numeradas de 1 a 3 e devem ser convertidas para índices válidos na matriz (de 0 a 2).
Valide se a posição escolhida está vazia antes de permitir que um jogador faça sua jogada.

Um jogador vence se conseguir três marcas consecutivas (horizontal, vertical ou diagonal).
•
Informe o vencedor ao final do jogo ou declare um empate se não houver mais espaços vazios no tabuleiro.'''