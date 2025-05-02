from collections import deque
maze =[
["A","0"," "," "," "],
[" ","0","0","0","0"],
[" ","0"," "," ","0"],
[" ","0"," "," ","B"]
]


start = (0,0)
goal = (3,4)


def DFS(start,goal,maze):

    stack = deque()
    visited = set()

    if not maze:
        return None
    
    stack.append((start,[start]))
    while stack:
        (x,y),path = stack.pop()

        if (x,y) in visited:
            continue

        visited.add((x,y))

        if maze[x][y] == "B":
            return path
        

        for dx,dy in[(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x + dx,y + dy
            if 0 <=nx <len(maze) and 0 <= ny <len(maze[0]):
                if maze[nx][ny] != " " and (nx,ny)  not in visited:
                    stack.append((nx,ny),path +[(nx+ ny)]) 
    return  None


def BFS(start ,goal,maze):

    queque = deque()
    visited = set()
    
    if not maze:
        return None
    queque.append((start,[start]))
    while queque:
        (x,y),path = queque.pop(-1)

        if (x,y) in visited:
            continue

        visited.add((x,y))

        if maze[i][y] == "B":
            return path 
        

        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny  = x + dx,y +dy
            if 0 <= nx <len(maze) and 0 <= ny <len(maze[0]):
                if maze[x][y] != " " and (nx,ny) not in visited:
                    queque.append((nx,ny),path + [(nx + ny)])

    return None

        


    

