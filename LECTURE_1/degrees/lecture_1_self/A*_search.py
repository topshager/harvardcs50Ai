grid = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]
start = (0, 0)
goal = (3, 3)



def Man_distance(grid ,start ,goal):

    for x in enumerate(grid):
         for rows in enumerate(grid):
            h = (x[0] - goal[0]),(rows[1]-goal[1])
            

        
                