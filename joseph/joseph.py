#!/usr/bin/python3

# Solution to a variant of the 'Joseph' problem, UVa #305

def works(k, m):
    n = 2*k # number of people in the circle
    pos = 0 # current position
    while n > k: # loop will break when only good guys remain
        kill = (pos + m) % n # next to be killed
        if kill == 0: kill = n # 1-index not 0-index
        if kill <= k: return False # a good guy was killed
        n -= 1 # the circle is smaller now
        pos = kill - 1 # index based on the new circle size
    return True

# pre-computed values for m. k = index + 1
solutions = [2, 7, 5, 30, 169, 441, 1872, 7632, 1740, 93313, 459901, 1358657, 2504881]

def main():
    """ Only run this once
    for k in range(1,14):
        m = k + 1
        while not works(k, m):
            m += 1
        solutions.append(m)
    """
    k = int(input())
    while k != 0:
        print(solutions[k - 1])
        k = int(input())
    return

if __name__=='__main__':
    main()

