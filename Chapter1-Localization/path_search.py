# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    open = []
    check = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]  # initialize a check list used for indicate whether 
    # the corresponding grid is expanded, if yes, then ingnore that possiblity
    y = init[0]
    x = init[1]
    g = 0
    check[y][x] = 1 # the start grid is checked
    found = False # used for indicate we find a path successfully
    no_solution = False # used for indicate whether there exist a solution
    open.append([g, y, x])
    
    while (not found) and (not no_solution):
        if len(open) == 0:
            no_solution = True
            print "fail, no validate path exist"
        else:
            open.sort()
            open.reverse()
            next = open.pop()  # retrieve the last element, here the last element is the item with the smallest g value
            if next[1] == goal[0] and next[2] == goal[1]:
                found = True
                print next  # print what we want
            else:
                for i in range(len(delta)):
                    y2 = next[1] + delta[i][0]
                    x2 = next[2] + delta[i][1]
                    if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid) and grid[y2][x2] == 0 and check[y2][x2] == 0:
                        # the above condition include: 1) coordinate in a valid range
                        # 2) the new expanded grid is obstacle-free
                        # 3) the grid is not checked
                        g2 = next[0] + cost
                        open.append([g2, y2, x2])
                        check[y2][x2] = 1 # grid checked

                        print open[-1]
                        
        
    
    # ----------------------------------------

search(grid,init,goal,cost)
