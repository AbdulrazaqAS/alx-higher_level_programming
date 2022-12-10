#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4 as hid
    names = dir(hid)
    for n in names:
        if n[0] != '_':
            print(n)
