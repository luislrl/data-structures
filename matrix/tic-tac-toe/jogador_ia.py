from random import randint
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):
        matriz = self.matriz
        DESCONHECIDO = Tabuleiro.DESCONHECIDO

        # R1: Linha, coluna e diagonais
        for l in range(3):
            soma = 0
            espacoLivre = None
            for c in range(3):
                soma += matriz[l][c]
                if matriz[l][c] == DESCONHECIDO:
                    espacoLivre = (l, c)
            #Ganha ou defende
            if soma == 2 and espacoLivre:
                return espacoLivre
            if soma == 8 and espacoLivre:
                return espacoLivre

        for c in range(3):
            soma = 0
            espacoLivre = None
            for l in range(3):
                soma += matriz[l][c]
                if matriz[l][c] == DESCONHECIDO:
                    espacoLivre = (l, c)
            if soma == 2 and espacoLivre:
                return espacoLivre
            if soma == 8 and espacoLivre:
                return espacoLivre

        soma = 0
        espacoLivre = None
        for i in range(3):
            soma += matriz[i][i]
            if matriz[i][i] == DESCONHECIDO:
                espacoLivre = (i, i)
        if soma == 2 and espacoLivre:
            return espacoLivre
        if soma == 8 and espacoLivre:
            return espacoLivre

        soma = 0
        espacoLivre = None
        for i in range(3):
            soma += matriz[2 - i][i]
            if matriz[2 - i][i] == DESCONHECIDO:
                espacoLivre = (2 - i, i)
        if soma == 2 and espacoLivre:
            return espacoLivre
        if soma == 8 and espacoLivre:
            return espacoLivre

        # R2: Tenta criar duas sequências
        for l in range(3):
            for c in range(3):
                if matriz[l][c] == DESCONHECIDO:
                    # Simula uma jogada da IA
                    matriz[l][c] = Tabuleiro.JOGADOR_0
                    conta_somas = 0

                    soma_linha = 0
                    for col in range(3):
                        soma_linha += matriz[l][col]
                    if soma_linha == 2:
                        conta_somas += 1

                    soma_coluna = 0
                    for linha in range(3):
                        soma_coluna += matriz[linha][c]
                    if soma_coluna == 2:
                        conta_somas += 1

                    if l == c:
                        somaDiagP = 0
                        for i in range(3):
                            somaDiagP += matriz[i][i]
                        if somaDiagP == 2:
                            conta_somas += 1

                    if l + c == 2:
                        somaDiagSec = 0
                        for i in range(3):
                            somaDiagSec += matriz[2 - i][i]
                        if somaDiagSec == 2:
                            conta_somas += 1

                    # Desfaz a jogada simulada
                    matriz[l][c] = DESCONHECIDO

                    # Se criar duas ou mais sequências de soma = 2, retorna a posição
                    if conta_somas >= 2:
                        return (l, c)

        # R3: Jogada no centro
        if matriz[1][1] == DESCONHECIDO:
            return (1, 1)

        # R4: Jogada no canto oposto
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for i in range(4):
            x, y = cantos[i]
            ox, oy = cantos[3 - i]
            if matriz[x][y] == Tabuleiro.JOGADOR_X and matriz[ox][oy] == DESCONHECIDO:
                return (ox, oy)

        # R5: Jogada em qualquer canto vazio
        for x, y in cantos:
            if matriz[x][y] == DESCONHECIDO:
                return (x, y)

        # R6: Jogada arbitrária
        for l in range(3):
            for c in range(3):
                if matriz[l][c] == DESCONHECIDO:
                    return (l, c)

        # Nenhuma jogada disponível
        return None
