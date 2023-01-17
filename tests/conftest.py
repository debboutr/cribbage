from unittest.mock import patch

import click
import pytest

from cribbage_cmd.deck import Card
from cribbage_cmd.deck import Deck
from cribbage_cmd.player import Opponent
from cribbage_cmd.player import Player


@pytest.fixture(params=(), ids=())
def data():
    return "H|A"


@pytest.fixture
def card():
    Card


@pytest.fixture
def prompt_player():
    with patch.object(click, "prompt", lambda x: "4"):
        player = Player()
        yield player


@pytest.fixture
def discard_player():
    with patch.object(click, "prompt", lambda x: "42"):
        player = Player(
            hand=[
                Card("S|A"),
                Card("S|K"),
                Card("S|Q"),
                Card("S|J"),
                Card("S|1"),
                Card("S|9"),
            ]
        )
        yield player


@pytest.fixture
def discard_opponent():
    return Opponent(
        hand=[
            Card("S|4"),
            Card("S|5"),
            Card("S|6"),
            Card("S|6"),
            Card("S|1"),
            Card("S|9"),
        ]
    )


@pytest.fixture
def player():
    return Player("one")


@pytest.fixture
def dealer():
    return Opponent("dealer")


@pytest.fixture
def deck():
    return Deck()


@pytest.fixture
def ace():
    return Card("S|A")


@pytest.fixture
def king():
    return Card("S|K")


@pytest.fixture
def queen():
    return Card("S|Q")


@pytest.fixture
def jack():
    return Card("S|J")


@pytest.fixture
def ten():
    return Card("S|1")
