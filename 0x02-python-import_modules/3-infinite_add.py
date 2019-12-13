#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = 0
    length = len(argv)
    for i in range(1, length):
        num += int(argv[i])
    print(num)
