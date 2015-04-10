import random


def think(state, quip):
    random_state = state.copy()
    random_move = random.choice(random_state.get_moves())

    print "Picking %s for no good reason" % (str(random_move))
    return random_move


__author__ = 'Alec Noble and Delmy Reyes'
