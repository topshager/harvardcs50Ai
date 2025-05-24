"""
✅ 6. Water Jug Problem (State Space BFS)
You have:

A 4-liter jug

A 3-liter jug

You must measure exactly 2 liters using these operations:

Fill, Empty, Pour

Return a sequence of states showing how to get 2 liters in one jug.

📌 This is state-space search, like AI search problems.
"""
from collections import deque

JUG4 =4
JUG3 = 3
Goal = 2

# define base case

def is_goal(state):
    return state[0] == Goal or state[1] == Goal

def get_next_state(state):
    x,y  =  state
    next_state = set()
    #FILLING THE JUGS 
    next_state.add((JUG4,y))
    next_state.add((x,JUG3))

    # SETTING THE STATE TO Zero
    next_state.add((0,y))
    next_state.add((x,0))

    pour = min(y,JUG4 - x)
    next_state.add((x + pour,y - pour))

    pour  = min(y,JUG3-x)
    next_state.add((x+pour ,y - pour))

    return next_state


def bfs():
    visited = set()
    queue = deque()
    parent = {}

    start ={0,0}
    queue.append(start)
    visited.add(start)
    parent[start] = None

    while queue:
        current = queue.popleft()
        if is_goal(current):
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path
        for next_state in get_next_state(current):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)

    return None

solution = bfs()
if solution:
    print("✅ Solution path:")
    for state in solution:
        print(state)
else:
    print("❌ No solution found.")


