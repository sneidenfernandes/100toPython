import random
from matka import matka
from tqdm.autonotebook import tqdm # For displaying progress bars while running simulations 


class game():

  
    def __init__(self):

        self.betting_range = [x for x in range(100)]       # Defines a bettting which translates all possible outcomes that can 
        self.odds = 90
        self.win = 0
        self.loss = 0
        self.sims = None
        self.rpu = None

    def simulate(self,n):

        Matka = matka()
        self.sims = n
    

        for _ in tqdm(range(n)):

            bet = random.choice(self.betting_range)         # Places a bet on a random number from the betting range.
            Matka.draw_patti('morning')
            Matka.draw_patti('evening')
            Matka.get_jodi()

            if Matka.jodi == bet: 
                self.win += 1
            else:
                self.loss += 1
        
        self.return_per_unit()
            

  
    
    def return_per_unit(self):                              # Calculates return per unit of currency that has been bet

        winnings = self.win * self.odds
        losses = self.loss 
        amount_bet = self.sims

        self.rpu = (winnings-losses)/amount_bet

        
        

      
    def results(self):                                      # Displays results
        print(f"""
               Wins:{self.win}
               Losses:{self.loss}
               Win rate:{self.win/self.sims}
               Return Per Unit Amount Bet: {self.rpu}
            """)







if __name__ == '__main__':

    kalyan = game()             # Initializing 'game' object
    kalyan.simulate(1000000)    # Setting the number of simulations
    kalyan.results()            # Displaying the Results
