from collections import deque

CUP1 = 4
CUP2 = 3
Goal = 2


def is_goal(state):
    return state[0] == Goal or state[1] == Goal

def get_next_state(state):
    x,y = state
    next_state = set()
    #Initialise the states 
    next_state.add((CUP1,y))
    next_state.add((x,CUP2))

    #emptying the cups to zero 
    next_state.add((0,y))
    next_state.add((x,0))


    pour = min(y,CUP2 - x)
    next_state.add((x+pour,y - pour))
    pour  = min(y,CUP1-x)
    next_state.add((x+pour ,y - pour))

    return next_state


def bfs():
    visited = set()
    queue = deque
    parent = {}

    start = {0,0}
    queue.append(start)
    visited.add(start)
    parent[start]  = None

    while queue:
        current = queue.popleft()
        if is_goal(current):
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path
        for next_state in  get_next_state(current):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)

    return None
            
        
