"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mcribbage_cmd` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``cribbage_cmd.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``cribbage_cmd.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click

from .deck import Deck
from .player import Cribbage
from .player import Opponent
from .player import Player


@click.command()
@click.argument('names', nargs=-1)
@click.option("--peg-char", default="", help="Enter character to represent peg on board. Can only be ONE character!")
def main(names, peg_char):

    # click.echo(repr(names))
    p = Player("rick")
    o = Opponent("guy")
    deck = Deck()
    deck.deal([p, o])
    # p.get_discards()
    # o.get_discards()
    # while sum([len(p.hand), len(o.hand)]):
    #     ps = p.lay_card()
    #     os = o.lay_card()
    #     print(f"{ps=} || {os=}")
    #     if all([ps == "GO",os == "GO"]):
    #         Player.peg.reset()
    if peg_char:
        Cribbage.set_char(peg_char)
    p.score(101)
    p.score(4)
    p.score(8)
    o.score(22)
    o.score(5)
    click.secho("_" * 37, fg="yellow")
    click.echo(p.make_lines())
    click.echo(click.style(" " * 7 + "     ".join(["|"] * 5), fg="yellow"))
    click.echo(o.make_lines())
    click.secho("‾" * 37, fg="yellow")
