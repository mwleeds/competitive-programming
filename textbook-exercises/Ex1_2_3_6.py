#!/usr/bin/python3

# solution to Exercise 1.2.3 problem #6 from "Competitive Programming 3"

l = []

def main():
    while True:
        s = input()
        if s == '': break
        l.append(int(s))
    v = int(input())
    print('Index: ' + str(binary_search(v, 0, len(l) - 1)))

def binary_search(value, left, right):
    if left > right: return -1
    mid = int((left + right) / 2)
    if l[mid] < value: return binary_search(value, mid + 1, right)
    if l[mid] > value: return binary_search(value, left, mid - 1)
    return mid

if __name__=='__main__':
    main()
