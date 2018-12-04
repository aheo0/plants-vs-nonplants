from organism import Organism
from plant import Plants
from non_plant import Non_Plant
from card import Card

class Wave(object):
    #Waves
    def __init__(self, wave_num, row, num):
        self.wave_num = wave_num
        self.row = row
        self.num = num