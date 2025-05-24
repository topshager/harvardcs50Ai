"""
✅ 3. Knight's Shortest Path (Chessboard BFS)
Given a chessboard and a starting square, find the shortest number of moves a knight needs to reach a target square.

Input: start = (0,0), end = (7,7)
Output: 6 (minimum knight moves)
"""

from collections import deque




def Shortest_path(start,end):
    moves = [
        (2,1),(1,2),(-1,2),(-2,1),(-2,-2),(-1,-2),(-2,-1),(1,-2),(2,-1)
    ]

    queue  = deque()
    visited = set()


    queue.append((start,[start]))

    while queue:

        (x,y),path =  queue.popleft()
        
        if (x,y) in visited:
            continue
        visited.add((x,y))
        

        if (x,y) == end:
            return len(path)-1

        for dx,dy in moves:
            nx,ny = x + dx ,y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                queue.append(((nx,ny),path + [(nx,ny)]))

    return -1




start = (0,0)
end = (7,7)
print(Shortest_path(start, end))  
        
     
    