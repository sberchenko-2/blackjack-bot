import random


class Deck:
    """
    Represents a blackjack deck.
    In this deck, cards are represented solely by value - no information about suit is contained.
        - Ace is represented by the value 1
    Furthermore, 10s, Jacks, Queens, and Kings, are all considered equivalent cards.

    Fields:
        - counts:  Dictionary mapping values to their respective counts in the deck
        - cards:   List of card values in deck
        - count:   Number of cards in deck
    """

    def __init__(self, n=3):
        """
        Initializes a new blackjack containing n normal decks.
        :param n: The number of normal decks contained in this blackjack deck. Default is 3.
        """
        count = 4*n
        self.counts = {i: count for i in range(1, 11)}
        self.counts[10] *= 4

        self.cards = [e for e in range(1, 11) for i in range(self.counts[e])]
        self.count = n*52

    def chance_of(self, card):
        """
        Returns the probability of the next draw being the inputted card.
        :param card: An integer representing the numerical value of a card - ace is 1 and max is 10
        :return: The probability of the next draw being the input - return type is float
        """
        return self.counts[card] / self.count

    def draw(self, n=1):
        """
        Draws n cards from the deck. The drawn cards are returned as a list in drawn order.
        :param n: The amount of cards to be drawn - default is 1
        :return: A list of the values of the drawn cards in drawn order.
        """
        arr = []
        for i in range(n):
            card = random.randint(0, self.count - 1)
            val = self.cards[card]
            arr.append(val)
            del self.cards[card]
            self.count -= 1
            self.counts[val] -= 1
        return arr
