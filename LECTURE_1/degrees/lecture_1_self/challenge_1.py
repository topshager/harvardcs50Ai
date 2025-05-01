from collections import deque
maze = [
    ["A", " ", "#", " ", "B"],
    ["#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#"]
]
#DEFINITION OF MAZE



def find_start(maze):#finding the start of the maxe 
    for i ,row in enumerate(maze):#going through rows in maze using enumerate to keep track of  i 
        for j  ,column in enumerate(maze):# going through columns in maze using enumerate 
            if column == "A":# once you find goal state  
                return (i,j) #return (i,j)
    return None


def solve_maze_dfs(maze):
    start = find_start(maze)# this is inital state
    if not start:
        return None
    
    stack = deque() #stack  
    stack.append((start,[start])) # append inital state  into stack 
    visited = set() #visited is a set 

    while stack: #while stack has values 
        (x,y) , path = stack.pop()  # popping these values into stack 
        
        if (x,y) in visited: # if x,y in visited  continue without doing enything 
            continue

        visited.add((x,y)) # if not in visited add to visited 
        if maze[x][y] == "B":
            return path # end state 
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x + dx ,y = y+dy
            if 0 <=nx < len(maze) and 0 <= ny<len(maze[0]):
                if maze[x][ny] !="#" and (nx,ny) not in visited:
                    stack.append(((nx,ny),path + [(nx,ny)]))

    return None
solution = solve_maze_dfs(maze)
print("PATH: ", solution)





            




