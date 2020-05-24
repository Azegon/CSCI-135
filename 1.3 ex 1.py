import sys

num_1 = sys.argv[0]
num_2 = sys.argv[1]
num_3 = sys.argv[2]

if num_1 == num_2:
    if num_2 == num_3:
        print('equal')
    else:
        print('not equal')
else:
    print('not equal')