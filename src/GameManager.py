from src.Deck import Deck
import json

class GameManager:
    """
    Manages a game of blackjack
    """

    def __init__(self):
        """
        Initializes the GameManager according to config.json
        """
        config = json.loads(open('config.json').read())

        self.deck = Deck(config['num_decks'])
        self.bot_cash = config['start_cash']
        self.max_bet = config['max_bet']

    def run_game(self):
        while self.bot_cash != 0 and self.deck.count >= 4:
            dlr_cards = self.deck.draw(2)
            bot_cards = self.deck.draw(2)




def main():
    manager = GameManager()
    manager.run_game()


if __name__ == '__main__':
    main()
