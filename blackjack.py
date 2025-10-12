import random, sys

suits = ["♣", "♥", "♠", "♦"]
values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

class Game():

        def __init__(self, money: int, money=500) -> None:

                self.money = money

        def get_hands() -> None:

                self.dealer_hand = Deck().take_card()
                self.dealer_hand.take_card()
                self.player_hand = Deck().take_card()
                self.player_hand.take_card()
                
        def do_action() -> None:

                valid_actions = ["h", "k", "d", "s", "q"]
                    print('''
Actions:

T - Take card
K - Keep hand
D - Double the bet and take a card
S - Split the deck in two and Double Down
Q - Quit
'''

                while True:
                        player_action = input("> ").lowercase().strip()
       	                if player_action in valid_actions:
	                        return player_action
       	                print("Invalid action")

                match player_action:
                        case "h":
                                self.player_hand.take_card()
                        case "k":
                                pass
                        case "d":
                                self.player_hand.take_card()
                                self.player_hand.take_card()
                                self.bet *= 2
                        case "s":
                                pass
                        case "q":
                                print("Farewell!")
                                sys.exit()
                                
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

        def check_game() -> None:

                if:
                        self.buffer += self.bet
                elif:
                        self.buffer -= self.bet
                else:
                        print("Drawn")

class Deck():

        def __init__(self) -> None:
                pass
        
        def create_deck() -> None:
                
                self.deck = []
                while len(self.deck) < 2:
                        self.deck.append((create_card()))
                
        def take_card() -> None:
                
                return self.deck.append(Card(random.choice(values), random.choice(suits)))

        def flip_card(card_index: int) -> None:
                
                self.hand[card_index].flipp_card()
                
        def sum_hand() -> int:

                sum = 0
                for i in self.deck:
                        value = i.return_value()

                        if value in "A":
                                sum += 1        
                        elif i in ["K", "Q", "J"]:
                                sum += 10
                        else:
                                sum += int(value)
                return sum
                        
        def render_deck() -> None:

                render_deck = []
                for i in self.hand():
                        render_deck.append(i.render_card())

                line_printed = 0
                while line_printed < 4:
                        print(" ".join(render_deck[line_printed] for card_line in render_deck))
                        line_printed += 1
                        
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
                
                if not self.flipped == True:
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
                                is_blank = False
                                for i in card[1]:
                                        if is_blank == True and i == "#":
                                                card.replace(card[1][i], " ")
                                        elif i == "#":
                                                card.replace(card[1][i], self.value)
                                                is_blank = True
                                for i in card[3]:
                                        if is_blank == True and i == "#":
                                                card.replace(card[3][i], "_")
                                                is_blank = False
                                        elif i == "#":
                                                card.replace(card[3][i], self.value)
                        for i in card[2]:
                                if i == "#": card[2][i] = self.suit
                        return card
                else:
                        return card
                                        
def main() -> None:

        money = 500

        while True:
                game = Game(money)
                buffer_money = self.money
                while buffer_money > 0:
                        current_deck = game.get_hands()
                        current_bet = get_bet(self.buffer_money)
                
                        while current_state != False:
                                game.do_action()
                                game.render_game()

                                current_state, winner = game.check_game(current_buffer)

                        if winner == "player":
                                buffer_money += current_bet
                                if winner == "dealer":
                                        buffer_money -= current_bet   
                                else:
                                        print("It is a draw!")
                valid_entries = ["c", "m", "q"]
                print('''
Want to continue playing?

C - Continue
M - Continue and change money
Q - Quit
                ''')

                while True:
                        entry = input("> ")
                        if entry.lowercase().strip() not in valid_entries:
                                break
                        print("Invalid entry")
                match entry:
                        case "c":
                                pass
                        case "m":
                                money =

def get_money() -> int:

        try:
                while True:
                        return int(input("> "))
        except ValueError:
                print("Invalid entry")
                        
        
def get_bet(current_money: int) -> int:

        try:
                while True:
                        print("How much you want to bet? (Q to quit)")
                        wanted_bet = input("> ")
                        
                        if wanted_bet.lowercase().strip() == "q":
                                print("Farewell!")
                                sys.exit()

                        if 0 < int(wanted_bet) <= current_money:
                                return int(wanted_bet)
                        print("Invalid bet")
        except ValueError:
                print("Invalid entry")
        
if __name__ == "__main__":
        main()
