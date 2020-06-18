import random

def createWorld(x,y):
    ZombieSimWorld = []
    for y in range(5):
        xaxis = []
        for x in range(5):
            xaxis.append('')
        ZombieSimWorld.append(xaxis)
    return ZombieSimWorld

def isimmune(immunityRate):
    random.seed()
    chance = immunityRate*100
    randonum = random.randrange(100)
    if randonum < chance:
        retbool = True
    else:
        retbool = False
    return retbool

def populate(ZombieSimWorld, immunityRate):
    for x in range(len(ZombieSimWorld)):
        for y in range(len(ZombieSimWorld[x])):
            immune = isimmune(immunityRate)
            if immune == True:
                ZombieSimWorld[x][y] = 'i'
            else:
                ZombieSimWorld[x][y] = '.'
    return

def infect(a, x, y):
    d = 1  # distance from x, y
    a[x-1][y-1] = 'Z'  # infect Patient Zero

    outputWorld(a)

    while d <= len(a):
        for i in range(x - d, x + d):
            if i >= 0 and i < len(a):  # don't go out of array bounds
                for j in range(y - d, y + d):
                    if j >= 0 and j < len(a):  # don't go out of bounds
                        a[i][j] = 'Z'  # does not check for immunity, just turns everyone into zombies
        print(d)
        outputWorld(a)
        d = d + 1

def outputWorld(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
    print()

def outputWorldStats(ZombieSimWorld):

   return

def main():
    print('Zombie World')
    if __name__ == '__main__':
        main()
