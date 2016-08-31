# Modify the code below so that the function sense, which
# takes p and Z as inputs, will output the NON-normalized
# probability distribution, q, after multiplying the entries
# in p by pHit or pMiss according to the color in the
# corresponding cell in world.

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    #
    # ADD YOUR CODE HERE
    q = []
    for i in range(len(p)):
        hit = (world[i] == Z)
        q.append(p[i] * (pHit * hit + pMiss * (1 - hit)))  # unnormalized
        # here use a little trick, you can write it in a more clear style
        # by using if ... else ... switch.
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s     # normalizes the output for the function sense. \
        # This means that the entries in q should sum to one.
    return q
print "quiz for sense function, input red, output is normalized: "
print sense(p, Z)


# next
# Try using your code with a measurement of 'green' and
# make sure the resulting probability distribution is correct.

# to fulfill this quiz, just change the mesurement Z to "green" color
p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
Z = 'green'
pHit = 0.6
pMiss = 0.2

print "another quiz, use green color as input to test our senese function, result is: "
print sense(p, Z)


# next test
# Modify the code so that it updates the probability twice
# and gives the posterior distribution after both
# measurements are incorporated. Make sure that your code
# allows for any sequence of measurement of any length.

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2


for i in range(len(measurements)):
    p = sense(p, measurements[i])
print "test for multiple measurements: "
print p
