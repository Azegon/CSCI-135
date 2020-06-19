import ZombieSimWorldPhase3

class World:
    def __init__(self, sim_world):
        self.sim_world = sim_world


a = int(input('Enter Patient Zero Height: '))
b = int(input('Enter Patient Zero Width: '))
immunityRate = float(input('Enter Immunity Rate: '))

worldinit = World(ZombieSimWorld.createWorld())
ZombieSimWorld.populate(worldinit.sim_world,immunityRate)
ZombieSimWorld.infect(worldinit.sim_world, a, b)
ZombieSimWorld.outputWorld(worldinit.sim_world)
ZombieSimWorld.outputWorldStats(worldinit.sim_world)
