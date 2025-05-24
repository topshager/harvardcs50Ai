"""
1. 🔀 Sliding Puzzle Solver (8-puzzle)
Implement an AI agent that, given any initial configuration of the 8-puzzle, returns the shortest sequence of moves to reach the goal configuration using A* search with admissible heuristics.

"""
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]