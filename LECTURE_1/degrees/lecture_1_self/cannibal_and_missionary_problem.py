from collections import deque
"""
🔢 1. Missionaries and Cannibals Problem
Goal: Move 3 missionaries and 3 cannibals across a river using a boat that can carry 2 people, without ever having cannibals outnumber missionaries on either side.§§
"""

M_left = 0
C_left = 0
boat_side = {"l","r"}


def crossing(m,c,side):

    