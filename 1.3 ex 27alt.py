import sys

width = sys.argv[0]

for x in range(1, width+2, 2):
    num_ask = x+(x-1)
    space_gap = ((width+(width-1))-num_ask)/2
    for y in range(int(space_gap)):
        print(end=' ')
    for z in range(x):
        print('*',end=' ')
    print()