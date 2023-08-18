#Blackjack game coded by Rohit Gore
#user v dealer simulation

import random

 

class Card:

    def __init__(self, suit, rank):

        self.suit = suit

        self.rank= rank

   

    def __str__(self):

        return (f"{self.rank['rank']} of {self.suit}")

 

class Deck:

    def __init__(self):

        self.cards=[]

        suits = ["hearts", "spades", "clubs", "diamonds"]

        ranks=[{"rank" : "A", "value" : 11}, {"rank" : "2", "value" : 2},{"rank" : "3", "value" : 3},{"rank" : "4", "value" : 4},{"rank" : "5", "value" : 5},{"rank" : "6", "value" : 6},{"rank" : "7", "value" : 7},{"rank" : "8", "value" : 8},{"rank" : "9", "value" : 9},{"rank" : "10", "value" : 10},{"rank" : "J", "value" : 10},{"rank" : "Q", "value" : 10},{"rank" : "K", "value" : 10}]

        for suit in suits:

            for rank in ranks:

                #print([suit, rank])

                self.cards.append(Card(suit, rank)) # crwates a full deck of cards with a suit and value, all as strings to start off

   

    def shuffle(self):

        if len(self.cards) > 1:

            random.shuffle(self.cards) # randomizes the cards #self.cards allows for the cards variable to be accessed in many other methods

   

   

    def deal(self, number): #creating a function to deal two cards, takes two from the deck and removes the two from the list of all the cards

        player_cards_dealt = []

        for x in range(number):

            if len(self.cards) > 0: #Checking to make sure there is more than 0 cards in the deck

                player_card = self.cards.pop()

                player_cards_dealt.append(player_card)

        return player_cards_dealt

   

 

class Hand:

    def __init__(self, dealer=False):

        self.cards=[]

        self.value=0

        self.dealer=dealer

 

    def add_card(self, card_list):

        self.cards.extend(card_list)

 

    def calculate_value(self):

        self.value =0

        has_Ace = False

 

        for card in self.cards:

            card_value = int(card.rank["value"])

            self.value += card_value

            if card.rank["rank"] == "A" :

                has_Ace = True

        if has_Ace and self.value > 21:

            self.value -= 10

 

    def get_value(self):

        self.calculate_value()

        return self.value

   

    def isBlackJack(self):

        return self.get_value() ==21

   

    def display(self, show_all_dealer_cards=False):

        print (f'''{"Dealer's" if self.dealer else "Your"} hand: ''')

        for index,card in enumerate(self.cards):

            if index == 0 and self.dealer and not show_all_dealer_cards and not self.isBlackJack():

                print ("hidden")

            else:

                print(card)

        if not self.dealer:

            print("Value:", self.get_value())

        print()

 

class Game:

    def play(self):

        game_number=0

        games_to_play=0

        while games_to_play == 0:

            try:

                games_to_play = int(input("How many games do you want to play? "))

            except:

                print("You must enter a number")

        while game_number < games_to_play:

            game_number += 1

            deck = Deck()

            deck.shuffle()

            player_hand = Hand()

            dealer_hand=Hand(dealer=True)

            for i in range(2):

                player_hand.add_card(deck.deal(1))

                dealer_hand.add_card(deck.deal(1))

            print()

            print("*" * 30)

            print(f"Game{game_number} of {games_to_play})")

            print("*" * 30)

            player_hand.display()

            dealer_hand.display()

       

            if self.check_winner(player_hand, dealer_hand):

                continue

            choice=""

            while player_hand.get_value() < 21 and choice not in ["s" , "stand"]:

                choice = input("Please Choose 'hit' or 'stand': ").lower()

                print()

                while choice not in ["h", "s", "hit", "stand"]:

                    choice = input("Please Choose 'Hit' or 'Stand': ").lower()

                    print()

                if choice in ["hit", "h"]:

                    player_hand.add_card(deck.deal(1))

                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):

                continue

            player_hand_value = player_hand.get_value()

            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:

                dealer_hand.add_card(deck.deal(1))

                dealer_hand_value = dealer_hand.get_value()

 

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):

                continue

            print ("Final Results")

            print ("Your Hand: ", player_hand_value)

            print("Dealer's hand: ", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

 

    def check_winner(self, player_hand, dealer_hand, game_over=False):

        if not game_over:

            if player_hand.get_value() > 21:

                print("Busted hand. Dealer Wins")

                return True

            elif dealer_hand.get_value() > 21:

                print ("Dealer Busted, You Win")

                return True

            elif dealer_hand.isBlackJack() and player_hand.isBlackJack():

                print ("Both players have a blackjack, tie")

                return True  

            elif dealer_hand.isBlackJack():

                print ("Dealer has blacjack, dealer wins")

                return