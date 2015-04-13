import random


def think(state, quip):
    moves = state.get_moves()

    best_move = moves[0]
    best_expectation = float('-inf')

    me = state.get_whos_turn()

    def outcome(score):
        if me == 'red':
            return score['red'] - score['blue']
        else:
            return score['blue'] - score['red']

    for move in moves:

        total_score = 0.0
        random_state = state.copy()
        random_move = random.choice(random_state.get_moves())
        random_state.apply_move(random_move)
        total_score += outcome(random_state.get_score())

        if total_score > best_expectation:
            best_expectation = total_score
            best_move = random_move

    print "Picking %s with expected score %f" % (str(best_move), best_expectation)
    return best_move

__author__ = 'Alec Noble'
