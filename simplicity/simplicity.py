#!/usr/bin/python3

# Solution to the Simplicity problem from ACM Southeast 2015

def main():
    input_string = input()
    char_counts = {}
    for char in input_string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    sorted_chars = sorted(char_counts.items(), key= lambda s: s[0], reverse=True)
    num_chars = 0
    for char in sorted_chars[2:]:
        num_chars += char[1]
    print(num_chars)

if __name__=='__main__':
    main()
