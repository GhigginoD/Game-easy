class Game():    
    def create_estrutura(self):
        self.estrutura = [[0,0,0],[0,0,0],[0,0,0]]

    def create_player(self):
        self.resposta = str(input('deseja ser o player 1? [s/n]'))
        if self.resposta == 's':
            self.player = 1
        else:
            self.player = 2

