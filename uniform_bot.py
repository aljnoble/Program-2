def think(state, quip):
    moves = {}
    for move in state.get_moves():
        moves = [move, state.get_moves(move)]
    state.apply_move(moves.choice())

__author__ = 'Alec Noble and Delmy Reyes'
