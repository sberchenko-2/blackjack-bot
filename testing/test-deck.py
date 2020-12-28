"""
Tests the deck of the bot
"""

from src.Deck import Deck


deck = Deck(1)

assert deck.count == 52
assert deck.counts[1] == 4
assert deck.counts[6] == 4
assert deck.counts[10] == 16

assert deck.chance_of(1) == 4/52
assert deck.chance_of(5) == 4/52
assert deck.chance_of(10) == 16/52

draw = deck.draw()[0]

assert deck.count == 51
assert deck.chance_of(draw) == 3/51
assert deck.chance_of(draw + 1 if draw != 10 else draw - 1) == 4/51