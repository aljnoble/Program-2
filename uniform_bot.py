import random


def think(state, quip):

    moves = state.get_moves()
    print moves
    state = state.apply_move(random.choice(moves))
    print state
    return state

__author__ = 'Alec Noble and Delmy Reyes'
