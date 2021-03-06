from p2_game import Game, State
from collections import defaultdict

import uct_bot as blue_bot
import greedy_bot as red_bot

BOTS = {'red': red_bot, 'blue': blue_bot}

rounds = 100
wins = defaultdict(lambda: 0)

for i in range(rounds):

    print
    ""
    print
    "Round %d, fight!" % i

    game = Game(4)
    state = State(game)

    def make_quipper(who):
        def quip(what):
            print
            who, ">>", what

        return quip

    while not state.is_terminal():
        move = BOTS[state.whos_turn].think(state.copy(), make_quipper(state.whos_turn))
        state.apply_move(move)

    final_score = state.get_score()
    winner = max(['red', 'blue'], key=final_score.get)
    print
    "The %s bot wins this round! (%s)" % (winner, str(final_score))
    wins[winner] += 1

print
""
print
"Final win counts:", dict(wins)

