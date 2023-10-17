import random


class game:


    def __init__(self) :
        self.moves = ['Rock','Paper','Scissor']
        self.computerMove = None
        self.PlayerMove = None


    def get_playerMove(self):
        self.PlayerMove = input('Enter your move >>>')

    def get_computerMove(self):
        self.computerMove = random.choice(self.moves)

    def check_win(self):
        return self.PlayerMove.lower() == self.computerMove.lower()
    
    

if __name__  == '__main__':

    rps = game()
    rps.get_playerMove()
    rps.get_computerMove()

    if rps.check_win:
       print('You Win!')
    else:
       print('You Lose!')