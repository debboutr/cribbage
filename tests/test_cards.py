import pytest

from cribbage_cmd.deck import Card


@pytest.mark.parametrize(
    "data, expected",
    [("S|A", 1), ("S|K", 10), ("S|Q", 10), ("S|J", 10), ("S|1", 10), ("S|9", 9)],
)
def test_card_value(data, expected):
    assert Card(data).value == expected


def test_card_equal():
    """find if pair"""
    assert not Card("S|4") == Card("D|4")
    assert Card("S|4") == Card("S|4")


def test_deck_deals_correct(player, dealer, deck):
    deck.deal([player, dealer])
    assert len(player.hand) == 6
    assert len(dealer.hand) == 6


def test_player_count(player):
    player.hand = [
        Card("S|K"),
        Card("S|Q"),
        Card("D|J"),
        Card("S|J"),
    ]
    count = player.count_cards()
    assert count == 8


def test_pegging_count(player, dealer):
    player.peg.point(Card("S|K"))
    assert player.peg.score == 10
    assert dealer.peg.score == 10
    dealer.peg.point(Card("S|5"))
    assert player.peg.score == 15
    assert dealer.peg.score == 15
    player.peg.point(Card("S|2"))
    assert player.peg.score == 17
    assert dealer.peg.score == 17


def test_running_score_fail(player, dealer):
    player.play_card(Card("S|7"))
    assert dealer.peg.score == 7
    dealer.play_card(Card("S|K"))
    assert player.peg.score == 17
    player.play_card(Card("D|K"))
    assert dealer.peg.score == 27
    ret = dealer.play_card(Card("D|K"))
    assert dealer.peg.go == 1
    assert ret == "GO"
    assert player.peg.score == 27
    # card = player.lay_card()
    ret = player.play_card(Card("D|K"))
    assert player.peg.score == 0
    assert ret == "GONE"


def test_player_prompt_returns_valid_card(prompt_player, deck):
    deck.deal([prompt_player])
    card = prompt_player.lay_card()
    assert type(card) == Card
    assert prompt_player.peg.score == card.value


def test_player_discard(discard_player):
    cards = discard_player.get_discards()
    for card in cards:
        assert type(card) == Card
        assert card not in discard_player.hand
    assert len(discard_player.hand) == 4


def test_opponent_discard(discard_opponent):
    cards = discard_opponent.get_discards()
    for card in cards:
        assert type(card) == Card
        assert card not in discard_opponent.hand
    assert len(discard_opponent.hand) == 4
    print(cards)
    print(discard_opponent.cards)
