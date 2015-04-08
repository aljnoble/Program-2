import random


def think(state, quip):
    moves = state.get_moves()
    print moves
    random_move = random.choice(moves)
    print random_move
    print random_move[0], random_move[1]

    """ I have no idea why the below code freaks out about iterating over 'NoneType' when
    it is neither iterating or of type None."""
    # TODO: Fix this. It should be the last bit for the easy bot.

    state.apply_move(random_move)

__author__ = 'Alec Noble and Delmy Reyes'
