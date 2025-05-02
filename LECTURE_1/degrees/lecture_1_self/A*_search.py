import heapq

grid = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]
start = (0, 0)
goal = (3, 3)



def heuristic(a,b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid,start,goal):
    rows,cols = len(grid),len(grid[0])
    open_set = []
    heapq.heappush(open_set,(0 + heuristic(start,goal)),0,start,[start])

    visited = set()

    while open_set:
        f,g,current,path = heapq.heappop(open_set)

        if current == goal:
            return path
        
        if current in visited:
            continue
        visited.add(current)

        x,y = current
        for dx ,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x +dx,y + dy
            next_node = (nx,ny)

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if next_node not in visited:
                    new_g = g + 1
                    new_F = new_g + heuristic(next_node,goal)
                    heapq.heappush(open_set,(new_F,new_g,next_node,path + [next_node]))

    return None

path = a_star(grid,start,goal)
print("path",path)












    





        
                