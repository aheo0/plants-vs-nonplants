class Organism(object):
    #All organisms
    def __init__(self):
        self.hp = 35
        self.dmg = 10
    
    #Loses health
    def take_damage(self, damage):
        self.hp -= damage
    
        