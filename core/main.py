    
class Game():
    
    def __init__(self):
        __player = self.__create_player()
        __structure = self.create_constructor()
    def __create_player(self):
        self.__player = str(input('Deseja ser o player 1?[y/n] '))
        
        if self.__player == 'y':
            self.__player = 1
        else:
            self.__player = 2
        return self.__player
    def create_constructor(self):
        
        self.__structure = [
            ['0','1','2'],
            ['3','4','5'],
            ['6','7','8'],
        ]
        return self.__structure
