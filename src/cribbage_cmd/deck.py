from random import choice
from random import shuffle


class Card:
    def __init__(self, data):
        suit, digit = data.split("|")
        self.suit = suit
        self.digit = digit

    suits = dict(S="♠", H="♡", C="♣", D="♢")

    def __repr__(self):
        suit = self.suits[self.suit]
        return f"{self.order}{suit}"

    def __eq__(self, other):
        return f"{self.suit}|{self.digit}" == other

    @property
    def order(self):
        return self.digit if self.digit != "1" else "10"

    @property
    def value(self):
        if self.digit == "A":
            return 1
        return 10 if self.order.isalpha() else int(self.order)


class Deck:

    suits = "SHCD"
    order = "A234567891JQK"
    indices = "|0|1|2|3|4|5|6|7|8|9|10|11|12|"

    def __init__(self):
        self.cards = None
        self.cut = None
        self._build()

    def _build(self):
        self.cards = [Card(f"{s}|{v}") for s in self.suits for v in self.order]
        shuffle(self.cards)

    def cut_cards(self):
        return choice(self.cards)

    def show(self):
        for c in self.cards:
            print(c)

    def deal(self, players):
        num_players = len(players)
        num_cards = 6 if num_players < 3 else 5
        for i in range(num_cards):
            for j in range(num_players):
                players[j].get(self.cards.pop())
        if num_players == 3:
            self.cut = self.cards.pop()

    def change_dealer(self, p1, p2):
        """this could just be a function from player.py
        Won't work with 3 players"""
        p1.is_dealer = p1.is_dealer ^ 1
        p2.is_dealer = p2.is_dealer ^ 1
