#!/usr/bin/python3

# A simple algorithm for finding the greatest common divisor of two numbers
# Usage: $ python3 gcd.py <a> <b>

from sys import argv

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

if __name__=='__main__':
    print(gcd(int(argv[1]), int(argv[2])))

