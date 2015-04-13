from math import *
import time
import random

THINK_DUR = 1


def think(state, quip):
    time_start = time.time()
    time_stop = time_start + THINK_DUR
    print time_start
    print time_stop


    iterations = 0

    rootnode = Node(state=state)
    print state.get_moves()

    while True:
        iterations += 1

        node = rootnode
        copy_state = state.copy()
        print copy_state.get_moves()
        while node.untriedMoves == [] and node.childNodes != []:  # node is fully expanded and non-terminal
            node = node.UCTSelectChild()
            copy_state.apply_move(node.move)
            print 'loop'

        if node.untriedMoves != []:
            m = random.choice(node.untriedMoves)
            copy_state.apply_move(m)
            node = node.AddChild(m, copy_state)

        while copy_state.get_moves() != []:
            copy_state.apply_move(random.choice(copy_state.get_moves()))


        while node != None:
            node.Update(copy_state.get_score())
            node = node.parentNode

        time_now = time.time()

        if time_now > time_stop:
            print 'I gpot hrtr'
            return node.UCTSelectChild(0).move

        sample_rate = float(iterations) / (time_now - time_start)


class Node:

    def __init__(self, move=None, parent=None, state=None):
        self.move = move
        self.parentNode = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = state.get_moves()
        self.playerJustMoved = state.get_whos_turn()

    def UCTSelectChild(self):
        s = sorted(self.childNodes, key=lambda c: c.wins / c.visits + sqrt(2 * log(self.visits) / c.visits))[-1]
        return s

    def AddChild(self, m, s):
        print 'child added'
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
