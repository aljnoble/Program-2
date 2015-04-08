def think(state, quip):
    best_action = None
    max_gains = 0

    for move in state.get_moves():
        curr_move = state.apply_move(move)
        curr_score = state.get_score()

        if best_action is None:
            best_action = curr_move
            max_gains = curr_score

        elif max_gains < curr_score:
            best_action = curr_move
            max_gains = curr_score

        else:
            pass

        # TODO: This is doing the exact same thing as uniform_bot, maybe I'm missing a key concept here.
        state.apply_move(best_action)


__author__ = 'Alec Noble and Delmy Reyes'
