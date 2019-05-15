from random import shuffle
from IPython.display import clear_output

class Deck:
    defaultNums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    defaultSuits = ['Hearts','Diamonds','Spades','Clubs']
    cards = []
    #Create a constructor method for each deck - each deck should have a defined suit,numbers, and sets
    def __init__(self,deckCount=1,suits=defaultSuits,numbers=defaultNums):
        self.suits = suits
        self.numbers = numbers
        # Generate list of cards
        for deck in range(deckCount):
            for suit in suits:
                for num in numbers:
                    self.cards.append((suit,num))
    
    #Create a method to get a deck of cards    
    def getDeck(self):
        return self.deck
    
    def dealCard(self):
        return self.cards.pop()
    
    #Create method that will shuffle the deck
    def shuffleDeck(self):
        shuffle(self.cards)
        
class Player:
    #Create a constructor for the player class that will hold the hand,cards,and tally the score
    def __init__(self,hand,name):
        self.hand = hand
        self.score = 0
        self.name = name
    
    # Get total score based on the hand the user/player is given
    def getScore(self):
        self.score = 0
        for card in self.hand:
            self.score += card[1]
            
        return self.score
    
    #Create a method to display a message if the user/player busts    
    def printBust(self):
        print("You busted!")
        
    #Create a method that will show the hand of the user/player
    def printHand(self):
        print('{} hand: {}: {}'.format(self.name,self.hand,self.getScore()))

class Human(Player): #A Human should have characteristics of a player
    #Define a constructor that has the characteristics of player
    def __init__(self,cards):
        super().__init__(cards,"Player")
    
class Dealer(Player):# A Human should have characteristics of a player

    #Define a constructor that has the characteristics of player
    def __init__(self,hand):
        super().__init__(hand,"Dealer")
    
    #Define a method to give the player a hit if asked
    def hit(self,deck,human):
        human.hand.append(deck.dealCard())
    
    def hitSelf(self,deck):
        self.hand.append(deck.dealCard())

class Game:
    
    #Define a constructor that will have a dealer,human,and players(the dealer and the human)
    def __init__(self,human,dealer):
        self.human = human
        self.dealer = dealer
        
    #Define a method to display a message if the user/player wins
    def playerWins(self):
        print("You Win!")
              
    #Define a method to display a message if the user/player pushes
    def playerPushes(self):
        print("Push")
              
    #Define a method to display a message if the user/player loses    
    def playerLoses(self):
        print("Dealer Wins!")
  
# deck = Deck()
# print(deck.cards)
# deck.shuffleDeck()
# print(deck.cards)

def main():
    #Create game logic here
    gameOver = False
    
    while gameOver == False:
        #Ask the player how many decks they want to use - Then print the number of decks
        while True:
            deckCount = input("Enter deck amount: ")
            try:
                deckCount = int(deckCount)
                clear_output()
                print("Using {} deck(s)".format(deckCount))
                break
            except:
                print("Invalid input, expected integer")

        deck = Deck(deckCount=12)
        deck.shuffleDeck()
        human = Human([deck.dealCard(),deck.dealCard()])
        human.printHand()
        dealer = Dealer([deck.dealCard(),deck.dealCard()])
        game = Game(human,dealer)
        turnOver = False
        playerBust = False

        if human.getScore() == 21:
            human.printBlackJack()
            turnOver = True

        #HINT: Continue to ask player if they want a hit or if they want to end the game
        #Ask the player if they want a hit
        #If they do, add the value of the card to their game tally
        #If they stand, keep the game tally where it is - add to dealer only
        while turnOver == False:
            while True:
                ans = input("Would you like a hit? (Y/N): ")
                if ans.lower() == 'y':
                    # Hit Player
                    dealer.hit(deck,human)
                    clear_output()
                    human.printHand()
                    break
                elif ans.lower() == 'n':
                    # Player stands
                    turnOver = True
                    clear_output()
                    human.printHand()
                    break
                else:
                    print("Invalid input, expected Y or N")
            currScore = human.getScore()

            if currScore > 21:
                print("You busted!")
                turnOver = True
                playerBust = True

        #Also add to the tally of the dealer while their tally is less than 16
        #If the dealer and player tally are the same - display that result
        #If dealer wins - display that result
        #If player wins - display that result
        dealerBust = False
        dealer.printHand()
        while dealer.getScore() < 16 and playerBust == False:
            dealer.hitSelf(deck)

        if dealer.getScore() > 21:
            dealerBust = True

        playerScore = human.getScore()
        dealerScore = dealer.getScore()
        
        clear_output()
        
        if playerScore > dealerScore and playerBust == False:
            game.playerWins()
        elif playerScore < dealerScore and dealerBust == False:
            game.playerLoses()
        elif playerBust == True:
            print("You busted!")
            game.playerLoses()
        elif dealerBust == True:
            print("Dealer busted!")
            game.playerWins()
        elif playerBust == False and dealerBust == False:
            game.playerPushes()

        human.printHand()
        dealer.printHand()
        
        while True:
            again = input("Would you like to play again? (Y/N): ")

            if again.lower() == 'y':
                clear_output()
                break
            elif again.lower() == 'n':
                print("Have a good day!")
                gameOver = True
                break
            else:
                print("Invalid input, try again.")