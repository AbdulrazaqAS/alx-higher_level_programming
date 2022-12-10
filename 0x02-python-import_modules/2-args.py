#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    ac = len(argv)
    if ac > 1:
        if ac == 2:
            print('1 argument:')
        else:
            print(ac - 1, 'arguments:')
        for ag in range(1, ac):
            print('{}: {}'.format(ag, argv[ag]))
    else:
        print('0 arguments.')
