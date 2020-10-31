class Player:
    def __init__(self, name, sex, vocation, level, world, residence, lastLogin):
        self.name = name
        self.sex = sex
        self.Vocation = vocation
        self.level = level
        self.world = world
        self.residence = residence
        self.lastLogin = lastLogin
        self.deaths = {}
     
    def __len__(self):
        return len(self.deaths)

    #def add_death(self, level):
        #self.deaths.append(level)

class OnlinePlayer:
    def __init__(self, name, level, vocation):
        self.name = name
        self.level = int(level)
        self.vocation = vocation