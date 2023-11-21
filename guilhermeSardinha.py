'''*******************************************************************************
Autor: Guilherme Fernandes Sardinha
Componente Curricular: Algoritmos I
Sistema Operacional: Windows 11
Versão Python: 3.9.5
Concluido em: 29/09/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************'''

import random
import os
import copy

# função que organiza o tabuleiro do jogo.
def organizar_matriz(tabuleiro):
    global jogadas
    global score
    print(f'Score: {score}\tQuantidade de jogadas: {jogadas}')
    print()
    for l in range(0,4):
        for c in range(0,4):
            print(f'|   {tabuleiro[l][c]:>4}   |'.replace('0',' ').replace('1 24','1024').replace('2 48','2048'),end='')
        print()
    
    return tabuleiro

# função que gera um numero 2 ou 4 em uma posição vazia aleatória no tabuleiro.
def gerar_numero_aleatório(tabuleiro):
    posições_vazias = []
    numeros = [2, 4]
    for l in range(0, 4):
        for c in range(0, 4):
            if tabuleiro[l][c] == 0:
                posições_vazias.append((l, c))
    
    if posições_vazias:
        i, j = random.choice(posições_vazias)
        tabuleiro[i][j] = random.choice(numeros)

# função que realiza a soma dos números nas linhas, colunas e atualiza o score.
def soma(tabuleiro):
    global score
    if movimento == 'W':
        for i in range(0, 4):
            if tabuleiro[0][i] == tabuleiro[1][i]:
                tabuleiro[0][i] = tabuleiro[0][i] + tabuleiro[1][i]
                tabuleiro[1][i] = 0
                score += tabuleiro[0][i]

            if tabuleiro[1][i] == tabuleiro[2][i]:
                tabuleiro[1][i] = tabuleiro[1][i] + tabuleiro[2][i]
                tabuleiro[2][i] = 0
                score += tabuleiro[1][i]

            if tabuleiro[2][i] == tabuleiro[3][i]:
                tabuleiro[2][i] = tabuleiro[2][i] + tabuleiro[3][i]
                tabuleiro[3][i] = 0
                score += tabuleiro[2][i]
    
    elif movimento == 'S':
        for i in range(0, 4):
            if tabuleiro[3][i] == tabuleiro[2][i]:
                tabuleiro[3][i] = tabuleiro[3][i] + tabuleiro[2][i]
                tabuleiro[2][i] = 0
                score += tabuleiro[3][i]

            if tabuleiro[2][i] == tabuleiro[1][i]:
                tabuleiro[2][i] = tabuleiro[1][i] + tabuleiro[2][i]
                tabuleiro[1][i] = 0
                score += tabuleiro[2][i]

            if tabuleiro[1][i] == tabuleiro[0][i]:
                tabuleiro[1][i] = tabuleiro[1][i] + tabuleiro[0][i]
                tabuleiro[0][i] = 0
                score += tabuleiro[1][i]
    
    elif movimento == 'A':
        for i in range(0, 4):
            if tabuleiro[i][0] == tabuleiro[i][1]:
                tabuleiro[i][0] = tabuleiro[i][0] + tabuleiro[i][1]
                tabuleiro[i][1] = 0
                score += tabuleiro[i][0]

            if tabuleiro[i][1] == tabuleiro[i][2]:
                tabuleiro[i][1] = tabuleiro[i][1]+ tabuleiro[i][2]
                tabuleiro[i][2] = 0
                score += tabuleiro[i][1]

            if tabuleiro[i][2] == tabuleiro[i][3]:
                tabuleiro[i][2] = tabuleiro[i][2] + tabuleiro[i][3]
                tabuleiro[i][3] = 0
                score += tabuleiro[i][2]
    
    elif movimento == 'D':
        for i in range(0, 4):
            if tabuleiro[i][3] == tabuleiro[i][2]:
                tabuleiro[i][3] = tabuleiro[i][3] + tabuleiro[i][2]
                tabuleiro[i][2] = 0
                score += tabuleiro[i][3]

            if tabuleiro[i][2] == tabuleiro[i][1]:
                tabuleiro[i][2] = tabuleiro[i][2] + tabuleiro[i][1]
                tabuleiro[i][1] = 0
                score += tabuleiro[i][2]

            if tabuleiro[i][1] == tabuleiro[i][0]:
                tabuleiro[i][1] = tabuleiro[i][0] + tabuleiro[i][1]
                tabuleiro[i][0] = 0
                score += tabuleiro[i][1]

    return tabuleiro, score

# função que reorganiza os numeros nas linhas e colunas do tabuleiro após as somas com base na movimentação realizada.
def organizar_numeros(direção, numeros_organizados):
    if direção == 'W':
        for i in range(0, 4):
            if numeros_organizados[0][i] == 0:
                numeros_organizados[0][i] = numeros_organizados[1][i]
                numeros_organizados[1][i] = 0
            if numeros_organizados[1][i] == 0:
                numeros_organizados[1][i] = numeros_organizados[2][i]
                numeros_organizados[2][i] = 0
            if numeros_organizados[2][i] == 0:
                numeros_organizados[2][i] = numeros_organizados[3][i]
                numeros_organizados[3][i] = 0
    
    if direção == 'S':
        for i in range(0, 4):
            if numeros_organizados[3][i] == 0:
                numeros_organizados[3][i] = numeros_organizados[2][i]
                numeros_organizados[2][i] = 0
            if numeros_organizados[2][i] == 0:
                numeros_organizados[2][i] = numeros_organizados[1][i]
                numeros_organizados[1][i] = 0
            if numeros_organizados[1][i] == 0:
                numeros_organizados[1][i] = numeros_organizados[0][i]
                numeros_organizados[0][i] = 0

    if direção == 'A':
        for i in range(0, 4):
            if numeros_organizados [i][0] == 0:
                numeros_organizados[i][0] = numeros_organizados[i][1]
                numeros_organizados[i][1] = 0
            if numeros_organizados [i][1] == 0:
                numeros_organizados[i][1] = numeros_organizados[i][2]
                numeros_organizados[i][2] = 0
            if numeros_organizados [i][2] == 0:
                numeros_organizados[i][2] = numeros_organizados[i][3]
                numeros_organizados[i][3] = 0
    
    if direção == 'D':
        for i in range(0, 4):
            if numeros_organizados [i][3] == 0:
                numeros_organizados[i][3] = numeros_organizados[i][2]
                numeros_organizados[i][2] = 0
            if numeros_organizados [i][2] == 0:
                numeros_organizados[i][2] = numeros_organizados[i][1]
                numeros_organizados[i][1] = 0
            if numeros_organizados [i][1] == 0:
                numeros_organizados[i][1] = numeros_organizados[i][0]
                numeros_organizados[i][0] = 0

    return numeros_organizados

# função que verifica o tabuleiro para identificar vitória ou derrota, encerrando a partida.
def verificar_fim_jogo(tabuleiro):
    global sair_do_loop
    tem_soma = False
    elementos = []
    for l in tabuleiro:
        for c in l:
            elementos.append(c)

    if elementos.count(2048) >= 1:
        sair_do_loop = 2
    
    for i in range(0, 4):
        if tabuleiro[0][i] == tabuleiro[1][i]:
            tem_soma = True
        if tabuleiro[1][i] == tabuleiro[2][i]:
            tem_soma = True
        if tabuleiro[2][i] == tabuleiro[3][i]:
            tem_soma = True
        if tabuleiro[i][0] == tabuleiro[i][1]:
            tem_soma = True
        if tabuleiro[i][1] == tabuleiro[i][2]:
            tem_soma = True
        if tabuleiro[i][3] == tabuleiro[i][2]:
            tem_soma = True

    if elementos.count(0) == 0:
        if tem_soma == True:
            sair_do_loop = 0
        else:
            sair_do_loop = 1

# função que executa as funções de soma, movimento, numero aleatório e verifica se a jogada é válida ou não.
def movimento_matriz(movimento, tabuleiro):
    global jogadas
    # criação de matriz copia utilizada para validar jogada
    matriz_copiada = copy.deepcopy(tabuleiro)
    tabuleiro = organizar_numeros(movimento, tabuleiro)
    tabuleiro = organizar_numeros(movimento, tabuleiro)
    tabuleiro, score = soma(tabuleiro)
    tabuleiro = organizar_numeros(movimento, tabuleiro)
    tabuleiro = organizar_numeros(movimento, tabuleiro)
    # validação da jogada
    if matriz_copiada != tabuleiro:
        gerar_numero_aleatório(tabuleiro)
        jogadas += 1
    tabuleiro = (organizar_matriz(tabuleiro))
    verificar_fim_jogo(tabuleiro)

    return tabuleiro, score

# função que mostra para o usuário se ele ganhou ou perdeu e atualiza o valor do recorde e histórico de partidas.
def mensagem_fim_jogo():
    global sair_do_loop
    global recorde
    global score
    global jogadas
    global historico

    decisão = ' '
    if sair_do_loop == 1:
        decisão = 'Perdeu'

    elif sair_do_loop == 2:
        decisão = 'Ganhou'

    print(f'Você {decisão}!\nQuantidade de jogadas: {jogadas}\nScore: {score}')
    if score > recorde[0]:
        recorde[0] = score
        recorde[1] = jogadas
        print(f'Seu Recorde foi atualizado!\nNovo Record: score - {recorde[0]}| jogadas - {recorde[1]}')
    elif score == recorde[0]:
        if jogadas < recorde[1]:
            recorde[0] = score
            recorde[1] = jogadas
            print(f'Seu Recorde foi atualizado!\nNovo Record: score - {recorde[0]}| jogadas - {recorde[1]}')
    historico.append([score, jogadas])

# programa principal.
if __name__ == '__main__':
    print('-='*30)
    print('2048'.center(60))
    print('-='*30)
    print()

    # lista que armazena os dados referentes ao recorde e ao histórico de partidas.
    recorde = [0,0]
    historico = []

    # loop que determina o inicio do jogo e possibilita o recomeço de jogo.
    recomeço = 'S'
    while recomeço == 'S':
        # determinação de variáveis importantes para o funcionamento do programa.
        sair_do_loop = 0
        score = 0
        jogadas = 0

        # definição do tabuleiro do jogo.
        matriz = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

        gerar_numero_aleatório(matriz)
        gerar_numero_aleatório(matriz)
        organizar_matriz(matriz)
        print(f'\nRecorde atual: score - {recorde[0]} | jogadas - {recorde[1]}\n')

        # loop que acomoda as funções necessárias para o funcionamento de cada partida.
        while sair_do_loop == 0:

            # declaração da variavel que armazena o dado de jogada possivel ou não
            

            # input que define a direção da soma e movimento dos numeros no tabuleiro
            print()
            movimento = input('Digite o movimento desejado. W-cima / S-baixo / A-esquerda / D-direita: ').upper()
            os.system('cls')

            # comando realizados para validar a entrada do usuário e executar o movimento desejado.
            if movimento in ('W', 'A', 'S', 'D'):
                matriz, score = movimento_matriz(movimento, matriz)
            
            else:
                print('caracter inválido. Digite novamente.')
                organizar_matriz(matriz)

        # função que mostra se o usuário ganhou ou perdeu e atualiza o recorde e o histórico de partidas.
        mensagem_fim_jogo()

        # loop e condicional que permitem o acesso ao histórico de partidas
        verificação = True          # variavel que quebra o loop while utilizado para tratar erros
        while verificação == True:
            pergunta = input('Deseja consultar o histórico? [S/N]').upper()
            os.system('cls')
            if pergunta == 'S':
                print('historico de partidas')
                print('-=' * 15)
                print('Score\tjogada')
                for i in historico:
                    for j in i:
                        print(j, '\t', end=' ')
                    print()
                    print('--'*15)
                verificação = False
            elif pergunta == 'N':
                verificação = False
            else:
                print('caracter inválido. Digite novamente')

        # loop e condicional que permitem o recomeço de jogo ou o fim do programa
        verificação = True           # variavel que quebra o loop while utilizado para tratar erros
        while verificação == True:
            recomeço = input('Deseja jogar novamente? [S/N]').upper()
            os.system('cls') 
            if recomeço == 'S':
                verificação = False
            elif recomeço == 'N':
                verificação = False
            else:
                print('caracter inválido. Digite novamente')   