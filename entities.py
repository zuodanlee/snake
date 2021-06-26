from math import floor
import random

from main import *

def round_to_multiple(num, base):
    return base * floor(num/base)

class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "R"
        self.body = [(x, y, block_size, block_size)]

    def get_rect(self):
        return (self.x, self.y, block_size, block_size)

    def turn(self, direction):
        if (self.direction == "L" and direction != "R") or \
            (self.direction == "R" and direction != "L") or \
            (self.direction == "U" and direction != "D") or \
            (self.direction == "D" and direction != "U"):
            self.direction = direction

    def move(self, apple):
        if self.direction == "L":
            self.x -= block_size
        elif self.direction == "R":
            self.x += block_size
        elif self.direction == "U":
            self.y -= block_size
        elif self.direction == "D":
            self.y += block_size
        
        if self.get_rect() == apple.get_pos():
            self.eat(apple)
        else:
            self.body.pop()

        self.body.insert(0, (self.x, self.y, block_size, block_size))
    
    def eat(self, apple):
        apple.respawn()

class Apple():
    def __init__(self):
        self.x = round_to_multiple(random.randint(0, width), block_size)
        self.y = round_to_multiple(random.randint(0, height), block_size)

    def get_pos(self):
        return (self.x, self.y, block_size, block_size)

    def respawn(self):
        self.__init__()