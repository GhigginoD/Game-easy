class Game():    
    def __init__(self):
        self.create_player()
        self.create_estrutura()
        self.menu()

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
        
    def atribui(self,linha,coluna):
        self.estrutura[linha][coluna] == 1

    def verifica(self):
        for line in self.estrutura:
            if line == [1,1,1]:
                self.resultado = 1
                break
            elif line == [-1,-1,-1]:
                self.resultado = 2
                break

        if ((self.estrutura[0][0] and self.estrutura[1][1] and self.estrutura[2][2])== [1,1,1]):
            self.resultado = 1
            
        elif  ((self.estrutura[0][2] and self.estrutura[1][1]and self.estrutura[2][0]) ==  [1,1,1]):
            self.resultado = 1
            
        elif((self.estrutura[0][0] and self.estrutura[1][1] and self.estrutura[2][2]) == [-1,-1,-1]):
            self.resultado = 2
            
        elif ((self.estrutura[0][2] and self.estrutura[1][1]and self.estrutura[2][0]) == [-1,-1,-1]):
            self.resultado = 2

        for column in zip(self.estrutura[0],self.estrutura[1],self.estrutura[2]):
            if(column == (1,1,1)):
                self.resultado = 1
                break
            elif(column == (-1,-1,-1)):
                self.resultado = 2
                break
    
    def menu(self):
        while self.jogadas < 9:

            self.printa()
            self.pergunta()
            self.atribui()
            self.verifica()
            if(self.resultado == 1):
                print('wins player 1')
                break
            elif(self.resultado == -1):
                print('wins player 2')
                break
            if(self.jogadas == 9):
                print('Deu Velha')
                break
            self.jogadas+=1
            self.printa()
            self.pergunta()
            self.atribui()
            self.verifica()
            if(self.resultado == 1):
                print('wins player 1')
                break
            elif(self.resultado == -1):
                print('wins player 2')
                break
            if(self.jogadas == 9):
                print('Deu Velha')
                break
            self.jogadas+=1
