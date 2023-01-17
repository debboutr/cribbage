# from collections import namedtuple
# from itertools import combinations
# from random import choice
# from random import shuffle

# import click

# def play_card(self, card, count):
#     if count + card.value > 31:
#         ...
#     possible = [c for c in self.hand if c.value + count <= 31]
#     if possible:
#         return "try again"
#     else:
#         return "GO"


# @click.command()
# def play_cribbage_game():

# if __name__ == "__main__":
#     play_cribbage_game()

# # blah = [Card("D|A"), Card("D|K"), Card("D|A"), Card("D|J"), Card("H|5"), Card("S|3")]
# blah2 = [Card("D|A"), Card("D|K"), Card("D|Q"), Card("D|J")]
# blah3 = [Card("D|A"), Card("D|K"), Card("D|Q"), Card("D|J")]

# dealer = Dealer("dealer")
# player = Player("rick")
# while dealer.score < 121 and player.score < 121:
#     deck = Deck()
#     deck.deal([dealer, player])
#     # player = Player("rick", hand=blah)
#     # dealer = Dealer("dealer", hand=blah)
#     # print(f"{player.hand=}")
#     cards = player.cards()
#     # click.echo(cards)
#     # click.echo('' + '    '.join([str(i) for i in range(len(player.hand))]))
#     # one, two = get_value()
#     one, two = "45"
#     one, two = sorted([int(one), int(two)])
#     player_discarded = [player.hand.pop(two), player.hand.pop(int(one))]
#     cut_card = choice(deck.cards)
#     cut_card = Card("D|Q")
#     # print(f"{player.hand=}")
#     player.add_cut(cut_card)
#     p_count = player.count_cards()

#     dealer_discarded = dealer.find_highest()
#     dealer.add_cut(cut_card)
#     dealer_count = dealer.count_cards()

#     crib = dealer_discarded + player_discarded + [cut_card]
#     cribbage = Player("crib",hand=crib)
#     crib_count = cribbage.count_cards()

#     player.hand.pop() # remove cut card
#     dealer.hand.pop() # remove cut card
#     dealer.hand.pop() # remove cut card
#     dealer.hand.append(Card("D|J")) # remove cut card
#     player = Player("rick", hand=blah2)
#     dealer = Dealer("dealer", hand=blah3)
#     # print(f"{sum([len(player.hand),len(dealer.hand)])=}")
#     # peggin_cards(player, dealer)
#     while sum([len(player.hand),len(dealer.hand)]):
#         peg_a_hand([player, dealer])
#     print("out")

# switch the deal, now the dealer always gets the crib
# but we don't need to subclass
# player, dealer = dealer, player

# Player has a method which either:
# * returns a card
# * if still cards in their hand -> GO
# * if no cards in their hand -> ??? None?

# conditions for each card lay:
#   * run_count < 31
#   * player holds cards that can be played to make 31 or less
#   * else GO

# strategy to hold running cards:
#     * can a pair be made?
#     * can a run be made?
#     * can a flush be made?

# click.echo(player.cards() + f" = {p_count} points!")
# click.echo(dealer.cards() + f" = {dealer_count} points!")
# while running_count < 31:

# print(f"{dealer.score=}")
# dealer.score = 747
# print(f"{dealer.score=}")


# d = Deck()
# # d.show()
# p1 = Player("rick")
# p2 = Player("dad")
# players = []
# # d.deal(players)
# a = Card("D|A")
# b = Card("S|K")
# c = Card("S|A")
# d = Card("C|J")
# e = Card("D|5")
# f = Card("S|3")
# hand = [a, b, c, d, e, f]
# hand_c = [a, b, c, d, e]
# print(f"{p1.hand=}")
# print(f"{p1.count_cards()=}")
# print(f"{p1.find_highest()=}")
# TODOS:
# this dumped the 4 & 6 into crib, should probably keep the straight
# self.hand=[4♢, 3♣, Q♣, 6♠, J♣, 5♣]
