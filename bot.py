import random


class Deck:
    """
    Represents a blackjack deck.
    In this deck, cards are represented solely by value - no information about suit is contained.
    Furthermore, 10s, Jacks, Queens, and Kings, are all considered equivalent cards.
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
        return self.cards[card] / self.count

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

def main():
    deck = Deck()

    count_init = deck.count
    draw = deck.draw(2)
    count_final = deck.count
    counts = (deck.counts[draw[0]], deck.counts[draw[1]])

    print(f"""
Init count: {count_init}
Final count: {count_final}
Draw: {draw}
Counts: {counts}
""")


if __name__ == '__main__':
    main()
