# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and 
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite 
# correct).
# -----------

from copy import deepcopy
import pylab as pl

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print '['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']'

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)
    error = tolerance 
    while error >= tolerance:
        error = 0
        for i in range(1, len(path) - 1):
            for j in range(len(path[0])):
                aux = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j])\
                + weight_smooth *(newpath[(i-1)%len(path)][j] + newpath[(i+1)%len(path)][j] - 2.0 * newpath[i][j])
                error += abs(aux - newpath[i][j])
                
    
    return newpath # Leave this line for the grader!

printpaths(path,smooth(path))

# plot scatters . old VS. newpath
newpath = smooth(path)
x =[]
y = []
x_new = []
y_new =[]
for i in range(len(path)):
    x.append(path[i][0])
    y.append(path[i][1])
    x_new.append(newpath[i][0])
    y_new.append(newpath[i][1])

pl.plot(x, y)
pl.plot(x_new, y_new, 'r')
pl.xlim(min(x) -1, max(x) + 1)# set axis limits
pl.ylim(min(y) -1, max(y) + 1)
pl.show()
