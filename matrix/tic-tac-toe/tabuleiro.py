# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        #Verifica linha
        for l in range(0,3):
            soma = 0
            for c in range(0,3):
                soma = soma + self.matriz[l][c]
                if soma == 3:
                    return Tabuleiro.JOGADOR_0
                elif soma == 12:
                    return Tabuleiro.JOGADOR_X

        #Verifica coluna
        for a in range(0,3):
            soma = 0
            for b in range(0,3):
                soma = soma +self.matriz[b][a]
                if soma == 3:
                    return Tabuleiro.JOGADOR_0
                elif soma == 12:
                    return Tabuleiro.JOGADOR_X
        #Verifica diagonal principal
        soma = 0
        for i in range(0,3):
            soma = soma + self.matriz[i][i]
            if soma == 3:
                    return Tabuleiro.JOGADOR_0
            elif soma == 12:
                    return Tabuleiro.JOGADOR_X
        #Verifica diagonal secundaria
        soma = 0
        for i in range(0,3):
            soma = soma + self.matriz[2-i][i]
            if soma == 3:
                    return Tabuleiro.JOGADOR_0
            elif soma == 12:
                    return Tabuleiro.JOGADOR_X

        return Tabuleiro.DESCONHECIDO