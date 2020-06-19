import random
class Character:
    def __init__(self, immunity, infected):
        self.immunity = immunity
        self.infected = infected


class World:
    def __init__(self, sim_world):
        self.sim_world = sim_world


def createWorld():
    ZombieSimWorld = []
    for y in range(10):
        xaxis = []
        for x in range(10):
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
                ZombieSimWorld[x][y] = Character(True, False)
            else:
                ZombieSimWorld[x][y] = Character(False, False)
    return

def infect(a, x, y):
    d = 1  # distance from x, y
    a[x-1][y-1] = Character(False,True) # infect Patient Zero

    outputWorld(a)

    while d <= len(a):
        for i in range(x - d, x + d):
            if i >= 0 and i < len(a):  # don't go out of array bounds
                for j in range(y - d, y + d):
                    if j >= 0 and j < len(a):  # don't go out of bounds
                        a[i-1][j-1] = Character(False, True)  # does not check for immunity, just turns everyone into zombies
        print(d)
        outputWorld(a)
        d = d + 1

def outputWorld(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j].immunity == True:
                print('I', end=' ')
            elif a[i][j].infected == True:
                print('Z', end=' ')
            else:
                print('.', end=' ')
        print()
    print()

def outputWorldStats(ZombieSimWorld):

   return

def main():
    print('Zombie World')
    if __name__ == '__main__':
        main()
