#!/usr/bin/python3
for a in range(ord('a'), ord("z") + 1):
    if a == ord('e') or a == ord("q"):
        continue
    print("{:c}".format(a), end="")
