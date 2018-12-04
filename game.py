#Imports
from linked_list import LinkedList
from queue import Queue
from stack import Stack

from wave import Wave
from non_plant import Non_Plant
from plant import Plant
from card import Card

import random

#Class--Game
class Game(object):
    #Game!
    def __init__(self, file):
        with open(file, 'r') as f:
            #Cash, height, width split by a space
            self.cash, self.height, self.width = [int(x) for x in f.readline().split(' ')]
            self.waves = LinkedList()
            self.wave_num = 0
            
            for line in iter(f.readline, ''):
                self.waves.add(Wave(*[int(x) for x in line.split(' ')]))
                self.wave_num = 1
        
        #Board
        self.board = Queue()    #size? (self.width and self.height)
        self.board = [][]       #?---
        
        #
        self.game_over = False
        self.turn = 0
        self.num_nonplants = 0
        self.powerup_cards = Stack()
        
    #draw a card
    def draw(self):
        print("Cash $" + self.cash + "\nWaves: " + self.wave_num + "\n")
        s = '  '.join([str(i) for i in range(self.width - 1)])
        print('  ', s)
        
        for row in range(self.height):
            s = []
            for col in range(self.width):
                #Plant
                if self.is_plant(row, col):
                    char = 'P'
                
                #NonPlant
                elif self.is_nonplant(row, col):
                    size = self.board[row][col].size()      #?---
                    char = str(size) if size < 10 else "#"
                
                #Empty
                else:
                    char = ','
                
                s.append(char)
            
            print(row + '  ' + '  '.join(s) + '\n' + '')
        print()
        