class Game():    
    def create_estrutura(self):
        self.estrutura = [[0,0,0],[0,0,0],[0,0,0]]

    def create_player(self):
        self.resposta = str(input('deseja ser o player 1? [s/n]'))
        if self.resposta == 's':
            self.player = 1
        else:
            self.player = 2

    def printa(self):
        print('    0    1   2')
        print('0:  {} |  {} | {}'.format(self.estrutura[0][0],self.estrutura[0][1],self.estrutura[0][2]))
        print('1:  {} |  {} | {}'.format(self.estrutura[1][0],self.estrutura[1][1],self.estrutura[1][2]))
        print('2:  {} |  {} | {}'.format(self.estrutura[2][0],self.estrutura[2][1],self.estrutura[2][2]))

    def pergunta(self):
        
        linha = int(input('linha: '))
        coluna = int(input('coluna: '))    
        self.atribui(linha,coluna)
