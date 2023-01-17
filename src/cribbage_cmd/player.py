from collections import namedtuple
from itertools import combinations

import click

from cribbage_cmd.deck import Deck

Hand = namedtuple("Hand", "index cards count fifteens flush pairs runs")


class Cribbage:
    def __init__(self):
        self.hand = []
        self.go = 0

    @property
    def last(self):
        return self.hand[0] if self.hand else None

    @property
    def score(self):
        return sum([c.value for c in self.hand])

    def point(self, card):
        self.hand.append(card)

    def reset(self):
        self.hand = []


class Contestant:

    # peg = Cribbage()

    def __init__(self, name=None, hand=None):
        self.name = name
        self.hand = hand if hand else []
        self.score = 0
        # istantiating with a name makes the first dealer
        self.is_dealer = False if not name else True
        Contestant.peg = Cribbage()

    def check_points(self, card):
        print(f"{self.peg.hand=}")
        if card.digit == self.peg.last.digit:
            self.score += 2
        if self.peg.score + card.value in (15, 31):
            # print(f"{card=}")
            self.score += 2
        # print(f"{self.score=}")

    def play_card(self, card=None):
        if not card:
            playable = [c for c in self.hand if (c.value + self.peg.score) <= 31]
            card = playable.pop()
        else:
            playable = (card.value + self.peg.score) <= 31
        if self.peg.score < 31 and playable:
            self.check_points(card)
            self.peg.point(card)
        else:
            if self.peg.go:
                # print(f"{self.hand=}")
                # print(f"{self.peg.score=}")
                self.peg.reset()
                self.score += 1  # this would be the last person
                return "GONE"
                # need to know the last person to have played a card for
                # point
            else:
                self.peg.go = self.peg.go ^ 1
                return "GO"

    def _faces(self):
        return [c.digit for c in self.hand]

    def _values(self):
        return [c.value for c in self.hand]

    def _suits(self):
        return [c.suit for c in self.hand]

    def _get_indices(self, cards):
        """Get indexes of the hand, filter out duplicates. Organize the list
        of strings in order to match against self.indices"""
        strx = [str(Deck.order.index(card)) for card in self._faces()]
        dups = [x for x in strx if strx.count(x) > 1]
        return sorted(list(set(strx)), key=int), dups

    def _iter_indices(self, hand, idx):
        """get a string to check against for the indexes that are found in
        self.indices. Return a window of size `idx`"""
        for i in range(len(hand) - idx + 1):
            yield f"|{'|'.join(hand[i : i + idx])}|"

    def _find_pairs(self):
        """Find the number of cards that match each other"""
        return sum([2 for x, y in combinations(self._faces(), 2) if x == y])

    def _find_runs(self):
        # print(f"{cards=}")
        indices, dups = self._get_indices(self.hand)
        if "|".join(indices) in Deck.indices and len(indices) == 5:
            return len(indices)
        windows = []
        for x in (4, 3):
            for jam in self._iter_indices(indices, x):
                if jam in Deck.indices:
                    # print(f"{jam=}")
                    windows.append(jam)
        win_size = max([len(w[1:-1].split("|")) for w in windows]) if windows else 0
        # print(f"{dups=}")
        if win_size == 4:
            return 8 if dups else 4
        elif dups:
            return sum([3 for win in windows for dup in dups if f"|{dup}|" in win])
        elif windows:
            return 3
        return 0

    def _find_fifteen(self):
        nums = (2, 3, 4, 5) if len(self.hand) == 5 else (2, 3, 4)
        count = 0
        for g in nums:
            count += sum([2 for grp in combinations(self._values(), g) if sum(grp) == 15])
        return count

    def add_cut(self, card):
        self.hand.append(card)

    @property
    def cards(self):
        return "|  ".join([str(card) for card in self.hand])

    def _count_hand(self):
        # faces = [c.digit for c in self.hand]
        # values = [c.value for c in self.hand]
        runs = self._find_runs()
        pairs = self._find_pairs()
        fif = self._find_fifteen()
        with_cut = len(self.hand) == 5
        if with_cut:
            cut = self.hand.pop()
        suits = [c.suit == self.hand[0].suit for c in self.hand]
        flush = len(self.hand) if all(suits) else 0
        if with_cut:
            self.hand.append(cut)
            if flush and cut.suit == self.hand[0].suit:
                flush += 1
        return fif, flush, pairs, runs


class Player(Contestant):
    def get_discards(self):
        click.echo(self.cards)
        click.echo('' + '    '.join([str(i + 1) for i in range(len(self.hand))]))
        value = click.prompt("Enter 2 numbers for cards you want to give away")
        if len(value) != 2:
            click.echo("Select two cards please!")
            value = self.get_discards()
        if not value.isnumeric():
            click.echo("Please select by number.")
        discarded = []
        for idx in sorted(value, reverse=True):
            discarded.append(self.hand.pop(int(idx) - 1))
        return discarded

    def lay_card(self):
        """this will be in player only...
        The dealer will have a similar method.
        Both will use play_card.
        """
        options = list(range(len(self.hand) + 1))
        click.echo(f"{self.peg.score=}")
        click.echo(f"HAND: {self.cards}")
        click.echo('IDXS: ' + '    '.join([str(i + 1) for i in range(len(self.hand))]))
        ret = click.prompt("what you wanna do?")
        if not ret.isnumeric():
            click.echo("You must enter a number!")
            self.lay_card()
        ret = int(ret)
        click.echo(f"{self.hand=}")
        if ret not in options or ret == 0:
            click.echo(f"Please enter one of the following numbers {', '.join(map(str, options))}")
            return self.lay_card()
        click.echo(f"{ret=}")
        card = self.hand.pop(ret - 1)
        click.echo(self.cards)
        self.peg.point(card)
        return card


class Opponent(Contestant):
    def lay_card(self):
        playable = [c for c in self.hand if (c.value + self.peg.score) <= 31]
        if not playable:
            return "GO"
        card = playable.pop()
        self.check_points(card)
        self.peg.point(card)
        return card

    # def play_card(self, card=None):
    #     if not card:
    #         card = playable.pop()
    #     else:
    #         playable = (card.value + self.peg.score) <= 31
    #     if self.peg.score < 31 and playable:
    #         self.peg.point(card)
    #     else:
    #         if self.peg.go:
    #             # print(f"{self.hand=}")
    #             # print(f"{self.peg.score=}")
    #             self.peg.reset()
    #             self.score += 1  # this would be the last person
    #             return "GONE"
    #             # need to know the last person to have played a card for
    #             # point
    #         else:
    #             self.peg.go = self.peg.go ^ 1
    #             return "GO"

    def get_discards(self):
        return self.find_highest()

    def find_highest(self):
        """Takes a hand (list of 6 Cards) and finds the one with the highest
        points
        """
        # print(f"{self.hand=}")
        hold = list(self.hand)
        combs = list(combinations(self.hand, 4))
        hands = []
        for i, comb in enumerate(combs):
            self.hand = list(comb)  # will need to think about this for dealer
            out = self._count_hand()
            count = sum([*out])
            hand = Hand(i, list(comb), count, *out)
            hands.append(hand)
        hands = sorted(hands, key=lambda h: h.count, reverse=True)
        high_hand = hands[0].count
        highest = [c for c in hands if c.count == high_hand]
        # print(f"{highest=}")
        for count in highest:
            # if pairs, look for adjacent card values
            # print(f"{count=}")
            # print(f"{count.runs=}")
            pass
        # print(f"{count.cards=}")
        # print(f"{count.count=}")
        discarded = [card for card in hold if card not in count.cards]
        self.hand = count.cards
        # print(f"{self.hand=}")
        # print(f"{discarded=}")
        return discarded  # send back the last one for now
