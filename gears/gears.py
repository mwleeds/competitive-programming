#!/usr/bin/python3

# Attempt to solve the Gears problem from the 
# 2015 ACM-ICPC Southeast USA Regional Programming Contest Divison 1.

__author__='mwleeds'

from math import pow

class Gear:

    def __init__(self, x, y, r):
        self.x = x # x coordinate
        self.y = y # y coordinate
        self.r = r # radius
        self.rotation = 0 # 1 = clockwise, -1 = counter-clockwise
        self.adjacent = [] # list of adjacent gears
        self.last = False # denotes the last/target gear
        self.visited = False # whether the gear has been traversed in the graph

    def __str__(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + str(self.r)


def main():
    # get input and build a list of gears
    n = int(input().strip())
    gears = []
    for i in range(n):
        nextline = input().split(' ')
        newGear = Gear(int(nextline[0]), int(nextline[1]), int(nextline[2]))
        gears.append(newGear)
    # update each gear's adjacency list
    gearsCopy = gears.copy()
    for (i, gear) in enumerate(gearsCopy):
        for (j, otherGear) in enumerate(gearsCopy):
            if i != j and adjacent(gear, otherGear):
                gears[i].adjacent.append(gears[j])
    # mark the last gear
    gears[len(gears) - 1].last = True
    # arbitrarily set the rotation of the source gear
    gears[0].rotation = 1
    # traverse the 'graph' of gears breadth-first and determine if they can rotate
    if len(gears[0].adjacent) == 0:
        print('0')
        return
    result = check_adjacent(gears[0])
    if isinstance(result, bool) and result == True:
        lastGear = gears[len(gears) - 1]
        a = lastGear.rotation * lastGear.r
        b = gears[0].r
        divisor = gcd(a,b)
        a = a // divisor
        b = b // divisor
        print(str(a) + ' ' + str(b))
    else:
        print(result)

def check_adjacent(gear):
    gear.visited = True
    # do breadth first
    reachedLast = False
    for adjGear in gear.adjacent:
        if adjGear.rotation == gear.rotation or set(adjGear.adjacent) & set(gear.adjacent):
            return -1 # meaning the gears can't move
        else:
            adjGear.rotation = (-1 * gear.rotation)
            if adjGear.last:
                reachedLast = True
    if reachedLast:
        return True
    # now recurse for depth
    reachedLast = False
    for adjGear in gear.adjacent:
        if not adjGear.visited:
            result = check_adjacent(adjGear)
            if isinstance(result, int) and result == -1:
                return -1
            if isinstance(result, bool) and result == True:
                reachedLast = True
    if reachedLast:
        return True
    return 0 # meaning there's no path to the last gear
            
def adjacent(gear1, gear2):
    sum_of_radii_squared = pow(gear1.r + gear2.r, 2)
    distance_squared = pow(gear2.x - gear1.x, 2) + pow(gear2.y - gear1.y, 2)
    return (sum_of_radii_squared == distance_squared)

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

if __name__=='__main__':
    main()
