from collections import deque
maze = [
    ["A", " ", "#", " ", "B"],
    ["#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#"]
]



def find_start(maze):
    for i ,row in enumerate(maze):
        for j  ,column in enumerate(maze):
            if column == "A":
                return (i,j)
    return None


def solve_maze_dfs(maze):
    start = find_start(maze)
    if not start:
        return None
    stack = deque()
    stack.append((start,[start]))
    visited = set()

    while stack:
        (x,y) , path = stack.pop()
        
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if maze[x][y] == "B":
            return path
        
        for dx,dy in [(-1,0,(1,0),(0,-1),(0,1))]:
            nx,ny = x + dx ,y = y+dy
            if 0 <=nx < len(maze) and 0 <= ny<len(maze[0]):
                if maze[x][ny] !="#" and (nx,ny) not in visited:
                    stack.append(((nx,ny),path + [(nx,ny)]))

    return None
solution = solve_maze_dfs(maze)
print("PATH: ", solution)





            




