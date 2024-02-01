#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ag = len(sys.argv)
    sum = 0
    if ag > 1:
        for ac in range(1, ag):
            sum += int(sys.argv[ac])
        print(sum)
    else:
        print(0)
