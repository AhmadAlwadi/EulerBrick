# This program is supposed to find Eulers Bricks. More info: https://en.wikipedia.org/wiki/Euler_brick

import math

def isint(n):
    return (n%1==0)

def findBricks(i, j):
    bricks=[]
    for a in range(1, j):
        aSquared=a**2
        for b in range(i, j):
            bSquared=b**2
            firstDiagonal=math.sqrt(aSquared+bSquared)
            if not isint(firstDiagonal):
                continue
            for c in range(b, j):
                cSquared=c**2
                secondDiagonal=math.sqrt(aSquared+cSquared)
                if not isint(secondDiagonal):
                    continue
                thirdDiagonal=math.sqrt(bSquared+cSquared)
                if not isint(thirdDiagonal):
                    continue

                brick=[a, b, c]
                bricks.append(brick)
    return bricks


# Change the number in the bracket to change the lower and upper bounds of the bricks respectively, this gives the edges in the form of (a, b, c) 
print(findBricks(1, 1000))