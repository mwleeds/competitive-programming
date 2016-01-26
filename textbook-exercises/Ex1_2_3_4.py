#!/usr/bin/python3

# solution to Exercise 1.2.3 problem #4 from "Competitive Programming 3"

l = []
while True:
    userInput = input()
    if userInput == '': break
    l.append(int(userInput))
sortedUnique = sorted(list(set(l)))
print(sortedUnique)
