from organism import Organism
from plant import Plants
from non_plant import Non_Plant

class Card(object):
    #Card
    cost = 5
    
    def __init__(self, power):
        self.power = power