import random, sys


HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():
    print('''
         Rules: Try to get as close to 21 without going over.
         Kings, Queens and Jacks are worth 10 Points
         Aces are worth 1 to 11 points
         Cards 2 through 10 are worth their face value.
         (H)it to take another card.
         (S)tand to stop taking cards.
         On your first bet, you can (D)ouble down to increase your bet 
         but must hit exactly one more time before standing. 
         In case of a tie, the bet is returned to the player.
         The dealer stops hitting at 17.  
        ''')    
    
    money = 500

    while True:
        
        if money <= 0:
            print("""
                    You're broke!
                    Good thing you weren't playing with real money
                    Thanks for playing!
                """)
            sys.exit()

        print('Money:', money)
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print('Bet:', bet)

        while True: 
            displayHands(playerHand, dealerHand, False)
            print()

            #Check if the player has bust:
            if getHandValue(playerHand) > 21:
                break
            
            #Get the player's move, either H,S or D:
            move = getMove(playerHand, money - bet)

            # Handle the players actions:

            if move == 'D':
                additionalBet = getBet(min(bet,(money-bet)))
                bet += additionalBet
                print('Bet increased to {}'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank,suit = newCard
                print('You drew a {} of {}'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

            if move in ('S', 'D'):
                break

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand,False)

                if getHandValue(dealerHand) > 21:
                    break
                input('Press Enter to continue')

        print('\n\n')

        # Show the final hands:

        displayHands(playerHand,dealerHand,True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print('Dealer busts! You win ${}'.format(bet))
            money += bet
            
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You Lost!')
            money -= bet
            
        elif playerValue > dealerValue:
            print('You won {}'.format(bet))
            money += bet

        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n') 

            
            






def getBet(maxBet):
    "Ask the player how much they want to bet for this round."
    "Keep asking until they enter a valid amount"

    while True: 
        print(f'How much do you bet? (1-{maxBet},or QUIT)')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            if bet == 'QUIT':
                print('Thanks for playing!')
            sys.exit()
        
        if not bet.isdecimal:
            continue  # If the player didn't enter a number, ask again

        bet = int(bet)

        if 1 <= bet <=maxBet:
            return bet # Player entered a valid bet 
        



def getDeck():
    """Return a list of (rank,suit) tuples for all 52 cards."""
    deck = []

    for suit in (HEARTS,DIAMONDS,SPADES,CLUBS):
        for rank in range(2,11):
            deck.append((str(rank),suit))
        for rank in ('K','Q','J','A'):
            deck.append((str(rank), suit))

    random.shuffle(deck)

    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    ''' Show the player's and delaer's cards. Hide the dealers first card if showDealerHand is False.
    '''
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER:???')
        # Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    #Show the player's card:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    '''
        Returns the value of the cards. Face cards are worth 10, aces are worth 11 and 1 (This function picks the most suitable ace value)

    '''
    value = 0
    noOfAces = 0 

    # Add the value for the non-ace cards: 

    for card in cards:
            rank = card[0] # card is a tuple like (rank, suit)
            if rank == 'A':
                noOfAces += 1
            elif rank in ('K', 'J', 'Q'): # Face cards are worth 10 points
                value += 10
            else:
                value += int(rank) # Numbered cards are worth their number.

    # Add the value for the aces:
    value += noOfAces 
    for i in range(noOfAces):
        #If another 10 can be added without busting, do so:
            if value + 10 < 21:
                value += 10

    return value

def displayCards(cards):
    """Display all the cards in the cards list"""
    rows = ['','','','',''] # The text to display on each row

    for i, card in enumerate(cards):

        rows[0] += ' ___ ' # Print the top line of the card
        if card == 'backside':
            # Print a card's back:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            # Print the card's front:
            rank,suit = card
            rows[1] += "|{} |".format(rank.ljust(2))
            rows[2] += "| {} |".format(suit)
            rows[3] += "|_{}|".format(rank.rjust(2, '_'))
    
    for row in rows:
        print(row)


def getMove(playerHand, money):
        """
        Asks the player for their move, and returns 'H' for hit, 'S' for stand, and 'D' for double down
        """
        while True: # Keep looping until the player enters a correct move
            moves = ['(H)it', '(S)tand']

            # The player can double down on their first move, which we can 
            # tell because they'll have exactly two cards:

            if len(playerHand) == 2 and money > 0:
                moves.append('(D)ouble down')

            #Get the player's move:
            movePrompt = ', '.join(moves) + '> '
            move = input(movePrompt).upper()

            if move in ('H', 'S'):
                return move #Player has entered a valid move.
            
            if move == 'D' and  '(D)ouble down' in moves:
                return move



if __name__ == '__main__':
    main()