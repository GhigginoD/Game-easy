class Game():    
    player = None
    estrutura=None
    resposta = ''
    resultado = 0
    jogadas = 0
    linha = 0
    coluna = 0

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
        elif self.resposta == 'n':
            self.player = 2
        else:
            print('resposta inválida')
            self.__init__()

    def printa(self):
        nova_estrutura = [[],[],[]]
        for nlinha,linha in enumerate(self.estrutura):
            for item in (linha): 
                if(item == 0):
                    nova_estrutura[nlinha].append('_')
                elif(item == 1):
                    nova_estrutura[nlinha].append('X')
                else:
                    nova_estrutura[nlinha].append('O')
        

        print('    0    1   2')
        print('0:  {} |  {} | {}'.format(nova_estrutura[0][0],nova_estrutura[0][1],nova_estrutura[0][2]))
        print('1:  {} |  {} | {}'.format(nova_estrutura[1][0],nova_estrutura[1][1],nova_estrutura[1][2]))
        print('2:  {} |  {} | {}'.format(nova_estrutura[2][0],nova_estrutura[2][1],nova_estrutura[2][2]))

    def pergunta_player1(self):
        
        self.linha = int(input('linha: '))
        self.coluna = int(input('coluna: '))    
        self.atribui_player1()
        
    def atribui_player1(self):
        self.estrutura[self.linha][self.coluna] = 1
        print(self.estrutura[self.linha][self.coluna])

    def pergunta_player2(self):
        
        self.linha = int(input('linha: '))
        self.coluna = int(input('coluna: '))    
        self.atribui_player2()
    
    def atribui_player2(self):
        self.estrutura[self.linha][self.coluna] = -1

    def verifica(self):
        for line in self.estrutura:
            if line == [1,1,1]:
                self.resultado = 1
                break
            elif line == [-1,-1,-1]:
                self.resultado = 2
                break

        diagonal1 =[self.estrutura[0][0],self.estrutura[1][1],self.estrutura[2][2]]
        diagonal2 =[self.estrutura[0][2],self.estrutura[1][1],self.estrutura[2][0]]
        
        if ((diagonal1) == [1,1,1]):
            self.resultado = 1
            
        elif  ((diagonal2) ==  [1,1,1]):
            self.resultado = 1
            
        elif((diagonal1) == [-1,-1,-1]):
            self.resultado = 2
            
        elif ((diagonal2) == [-1,-1,-1]):
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
            self.pergunta_player1()
            self.verifica()
            if(self.resultado == 1):
                self.printa()
                print('wins player 1')
                break
            elif(self.resultado == -1):
                self.printa()
                print('wins player 2')
                break
            if(self.jogadas == 9):
                self.printa()
                print('Deu Velha')
                break
            self.jogadas+=1
            self.printa()
            self.pergunta_player2()
            self.verifica()
            if(self.resultado == 1):
                print('wins player 1')
                break
            elif(self.resultado == -1):
                print('wins player 2')
                break
            if(self.jogadas == 9):
                print('Deu Velha')
            self.jogadas+=1
game = Game()
