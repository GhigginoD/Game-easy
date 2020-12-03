    
class Game():
    
    def __init__(self):
        __player = self.__create_player()
    
    def __create_player(self):
        self.__player = str(input('Deseja ser o player 1?[y/n] '))
        
        if self.__player == 'y':
            self.__player = 1
        else:
            self.__player = 2
        return self.__player
