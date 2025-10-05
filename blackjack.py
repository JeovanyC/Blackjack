import random

suits = ["♣", "♥", "♠", "♦"]
values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

class Game():

        def __init__(self, money: 500) -> None:


        self.dealer_hand = Deck
                
        def do_action(player_hand: list) -> int:

                valid_actions = ["h", "k", "d", "s", "q"]
                print()

                while True:
                        player_action = input("> ").lowercase().strip()
       	                if player_action in valid_actions:
	                        return player_action
       	        print("Invalid action")
                
        def render_game() -> None:

                print("Dealer hand:")
                print()
                print(render_hand(dealer_hand, True))
                print()
                print(f"The total sum of dealer cards is: {sum_hand(dealer_hand))}")

                print()
    
                print("Your hand:")
                print()

                
                
                print(f"The total sum of your cards  is: {sum_hand(player_hand))}")
                print()

class Deck():

        def __init__(self) -> None:
                pass
        
        def create_deck() -> None:
                
                self.deck = []
                while len(self.deck) < 2:
                        self.deck.append((create_card()))
                
        def create_card() -> None:
                
                return Card(random.choice(values), random.choice(suits))

        def flip_card(card_index: int) -> None:
                
                self.hand[card_index].flipp_card()
                
        def sum_hand() -> int:

                sum = 0
                for i in self.deck:
                        value = i.return_value()

                        if value in "A":
                                value += 1        
                        elif i in ["K", "Q", "J"]:
                                value += 10
                        else:
                                value += int(value)
                return sum
                        
        def render_deck() -> None:

                render_deck = []
                for i in self.hand():
                        render_deck.append(i.render_card())

                line_printed = 0
                while line_printed < 4:
                        print(" ".join(render_deck[line_printed] for card_line in render_deck))
                        line_printed += 1

        def clear_deck()
                        
class Card():

        card_hashmap = [
                " ___ ",
                "|## |",
                "| # |",
                "|_##|",                
        ]


        def __init__(self, value: int, suit: str, flipped: bool, flipped=True) -> None:

                self.value = value
                self.suit = suit
                self.flipped = flipped
                
        def return_value() -> int:

                return self.value

        def return_suit() -> str:

                return self.suit

        def flipp_card() -> None:

                if self.flipped == True:
                        self.flipped = False
                else:
                        self.flipped = True
                
        def render_card() -> list:

                card = card_hashmap
                
                if not self.flipped == true:
                        if len(self.value) == 2:
                                temp_value = self.value
                                for i in card[1]:
                                        if i == "#":
                                                card.replace(card[1][i], temp_value[0])
                                                temp_value.replace(temp_value[0], "")
                                temp_value = self.value
                                for i in card[3]:
                                        if i == "#":
                                                card.replace(card[3][i], temp_value[0])
                                                temp_value.replace(temp_value[0], "")
                        else:
                                temp_value = self.value
                                is_blank = False
                                for i in card[1]:
                                        if is_blank == True and i == "#":
                                                card.replace(card[1][i], " ")
                                                is_blank = True
                                        elif i == "#":
                                                card.replace(card[1][i], temp_value[0])
                                                temp_value.replace()
                                temp_value = self.value
                                for i in card[3]:
                                        if is_blank == True and i == "#":
                                                card.replace(card[3][i], "_")
                                                is_blank = False
                                        elif i == "#":
                                                card.replace(card[3][i], temp_value[0])
                                                temp_value.replace(value[0], "")
                        for i in card[2]:
                                if i == "#": card[2][i] = self.suit
                        return card
                else:
                        return card
                                        
def main() -> None:

    player_hand = [take_card()]
    dealer_hand = [take_card()]

    money = 500

    print('''
Actions:

Hit (H) -> take card
Stand (K) -> keep hand
Double down (D) -> take card and double the bet
Split (S) -> if you have two same cards, split in two and double down
Surrender (Q)
'''
    while money <= 0:
        print("Take action: ")
       	action = do_action(player_hand)
	print_game(dealer_hand, player_hand)
	check_hands(dealer_hand, player_hand)
			
def check_hands(dealer_hand: tuple, player_hand: tuple) -> None:

    for 

    if player_hand > dealer_hand:
    if player_hand > 21:
    if dealer_hand > 21:

def take_card() -> int:
	
    return {random.choice(cards), random.choice(suit)}
