import ZombieSimWorld

x =int(input('Enter Map Height: '))
y = int(input('Enter Map Width: '))
a = int(input('Enter Patient Zero Height: '))
b = int(input('Enter Patient Zero Width: '))
immunityRate = float(input('Enter Immunity Rate: '))

sim_world = ZombieSimWorld.createWorld(x, y)
ZombieSimWorld.populate(sim_world,immunityRate)
ZombieSimWorld.infect(sim_world, a, b)
ZombieSimWorld.outputWorld(sim_world)
ZombieSimWorld.outputWorldStats(sim_world)
