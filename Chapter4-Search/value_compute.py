# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[goal[0]][goal[1]] = 1
    value = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    check_num = 1
    x = goal[0]
    y = goal[1]
    g = 0
    open = [[x,y]]
    explor = [[x,y]]
    solution = True
    while check_num != (len(grid) * len(grid[0])) and solution:
        g += cost  # in one shot exploration, all explored gird should have the same cost value
        open = explor
        explor = []
        while open != []:
            next = open.pop()
            x = next[0]
            y = next[1]
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]) and closed[x2][y2] == 0:
                    if grid[x2][y2] == 1:
                        # obstacle
                        value[x2][y2] = 99
                        closed[x2][y2] = 1
                        check_num += 1
                        #explor.append([x2, y2])
                    else:
                        value[x2][y2] = g
                        closed[x2][y2] = 1
                        check_num += 1
                        explor.append([x2, y2])
        if explor == []:
            solution = False
            print 'no solution exist, explore failed'
            for i in range(len(value)):
                for j in range(len(value[0])):
                    if value[i][j] == -1:
                        value[i][j] = 99

    # ----------------------------------------
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value

# test
value = compute_value(grid,goal,cost)
for i in range(len(value)):
    print value[i]

