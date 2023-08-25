import random 

class NumberGuessingGame:

    def __init__(self,low,high) :
        self.low = low
        self.high = high
        self.secret_number = random.randint(low,high)
        self.attempts = 0


    def play(self):
         
        while True:
            
            guess = int(input(f'Guess:'))

            if guess < self.secret_number:
                print("Too low!Try again.")

            elif guess > self.secret_number:
                print("Too high!Try again.")

            else:
                print(f"Congratulations!You guessed the numnber{self.secret_number}")
                break



def main():
    low = 1
    high = 100
    game = NumberGuessingGame(low,high)
    print("Welcome!")
    print(f"Guess a number between {low} and {high}.")
    game.play()


if __name__ == '__main__':
    main()


