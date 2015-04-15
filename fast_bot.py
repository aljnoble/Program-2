from math import *
import time
import random

MAX_ROLLOUTS = 5


def think(state, quip):
    best_move = moves[0]
    best_expectation = float('-inf')
    moves = state.get_moves()

    """Trying to check who's who
    me = state.get_whos_turn()

    if me == 'red':
        print "I am red"
    else:
        print "I am blue"

    print state.get_score()['blue']
    """
    time_start = time.time()
    time_stop = time_start + THINK_DUR

    iterations = 0

    rootnode = Node(state=state)

    while True:
        iterations += 1

        node = rootnode
        copy_state = state.copy()

        # Select

        while node.untriedMoves == [] and node.childNodes != []:  # node is fully expanded and non-terminal
            node = node.UCTSelectChild()
            copy_state.apply_move(node.move)

        # Expand

        if node.untriedMoves != []:
            m = random.choice(node.untriedMoves)
            copy_state.apply_move(m)
            node = node.AddChild(m, state)

        # Rollout

        while copy_state.get_moves() != []:
            for move in moves:

                total_score = 0.0

                for r in range(ROLLOUTS):
                    if rollout_state.get_moves =[]
                    rollout_state = state.copy()
                    rollout_state.apply_move(move)

            if expectation > best_expectation:
                best_expectation = expectation
                best_move = move
                print "Picking %s with expected score %f" % (str(best_move), best_expectation)

        return best_move


class Node:
    def __init__(self, move=None, parent=None, state=None):
        self.move = move
        self.parentNode = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = state.get_moves()
        self.who = state.get_whos_turn()
        self.score = state.get_score()[self.who]

    def UCTSelectChild(self):
        s = sorted(self.childNodes, key=lambda c: (c.score) + sqrt(2 * log(self.visits) / c.visits))[-1]
        return s

    def AddChild(self, m, s):
        n = Node(move=m, parent=self, state=s)
        self.untriedMoves.remove(m)
        self.childNodes.append(n)
        return n

    def Update(self, result):
        self.visits += 1
        self.wins += result

    def __repr__(self):
        return "[M:" + str(self.move) + " W/V:" + str(self.wins) + "/" + str(self.visits) + " U:" + str(
            self.untriedMoves) + "]"

    def TreeToString(self, indent):
        s = self.IndentString(indent) + str(self)
        for c in self.childNodes:
            s += c.TreeToString(indent + 1)
        return s

    def IndentString(self, indent):
        s = "\n"
        for i in range(1, indent + 1):
            s += "| "
        return s

    def ChildrenToString(self):
        s = ""
        for c in self.childNodes:
            s += str(c) + "\n"
        return s


__author__ = 'Alec Noble and Delmy Reyes'

