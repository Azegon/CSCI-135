import sys

height = sys.argv[0]
width = sys.argv[1]

for x in range(height):
    if x %2 == 0:
        for y in range(width):
            print('*', end = ' ')
        if x != height - 1:
            print()
    else:
        for y in range(width):
            print(' ', end = '*')
        if x != height - 1:
            print()