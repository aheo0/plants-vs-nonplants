from organism import Organism
from plant import Plants

class Non_Plant(Organism):
    #Non-plants (aka Zombies)
    worth = 20
    
    def __init__(self):
        super(Non_Plant, self).__init__()
        self.hp = 80
        self.dmg = 5
    
    #Attacks plant
    def attack(self, plant):
        plant.take_damage(dmg)
        
    