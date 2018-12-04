from organsim import Organism

class Plants(Organism):
    #Plants
    cost = 35
    
    def __init__(self):
        super(Plants, self).__init__()
    
    #Attacks nonplants
    def attack(self, nonplant):
        nonplant.take_damage(self.dmg + self.powerup)
    
    #Apply powerup
    def apply_powerup(self, card):
        self.power += card
        
    #Weakens powerup
    def weaken_powerup(self):
        self.power /= 2
    
    