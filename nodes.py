import pygame
import math
from config import *
import numpy

Vector2D = pygame.math.Vector2

class Node:
    def __init__(self, size, row, col):
        self.size = size
        self.position = Vector2D(row, col)
        self.coordinate = Vector2D(row * size, col * size)
        self.color = WHITE
        self.neighbours = []
        self.g = 2e50
        self.h = 2e50
        self.f = 2e50
        self.parent = Vector2D(-1, -1)

    # Return methods
    def get_data(self):
        return self.position, self.color

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_wall(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == YELLOW

    # Do methods
    def reset(self):
        self.color = WHITE

    def do_closed(self):
        self.color = ORANGE

    def do_open(self):
        self.color = GREEN

    def do_wall(self):
        self.color = BLACK
    
    def do_start(self):
        self.color = YELLOW

    def do_end(self):
        self.color = VOILET
    
    def do_path(self):
        self.color = BLUE

    # 
    def draw(self):
        pygame.draw.rect(SCREEN, self.color, (self.coordinate.x, self.coordinate.y, self.size, self.size))

    def updateNodes(self, matrix):
        self.neighbours = []
        if self.position.x != 0 and not matrix[round(self.position.x-1)][round(self.position.y)].is_wall():
            self.neighbours.append(matrix[round(self.position.x-1)][round(self.position.y)]) #(x-1,y)
        if self.position.x != ROWS-1 and not matrix[round(self.position.x+1)][round(self.position.y)].is_wall():
            self.neighbours.append(matrix[round(self.position.x+1)][round(self.position.y)]) #(x+1,y)
        if self.position.y != 0 and not matrix[round(self.position.x)][round(self.position.y-1)].is_wall():
            self.neighbours.append(matrix[round(self.position.x)][round(self.position.y-1)]) #(x,y-1)
        if self.position.y != COLS-1 and not matrix[round(self.position.x)][round(self.position.y+1)].is_wall():
            self.neighbours.append(matrix[round(self.position.x)][round(self.position.y+1)]) #(x,y+1)
        if self.position.x!= ROWS-1 and not matrix[round(self.position.x+1)][round(self.position.y)].is_wall() and self.position.y != 0 and not matrix[round(self.position.x)][round(self.position.y-1)].is_wall():
            self.neighbours.append(matrix[round(self.position.x+1)][round(self.position.y-1)]) #(x+1,y-1)
        if self.position.x!= ROWS-1 and not matrix[round(self.position.x+1)][round(self.position.y)].is_wall() and self.position.y != COLS-1 and not matrix[round(self.position.x)][round(self.position.y+1)].is_wall():
            self.neighbours.append(matrix[round(self.position.x+1)][round(self.position.y+1)]) #(x+1,y+1)
        if self.position.x != 0 and not matrix[round(self.position.x-1)][round(self.position.y)].is_wall() and self.position.y != 0 and not matrix[round(self.position.x)][round(self.position.y-1)].is_wall():
            self.neighbours.append(matrix[round(self.position.x-1)][round(self.position.y-1)])#(x-1,y-1)
        if self.position.x != 0 and not matrix[round(self.position.x-1)][round(self.position.y)].is_wall() and self.position.y != COLS-1 and not matrix[round(self.position.x)][round(self.position.y+1)].is_wall():
            self.neighbours.append(matrix[round(self.position.x-1)][round(self.position.y+1)]) #(x-1,y+1)

    def __lt__(self, other):
        return False

    