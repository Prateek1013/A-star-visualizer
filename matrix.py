from config import *
import numpy
import pygame 
import math
from nodes import *
import random
    
def make_matrix():
    matrix = []
    for i in range(ROWS):
        matrix.append([])
        for j in range(COLS):
            mynode = Node(NODE_SIZE, i, j)
            matrix[i].append(mynode)
    return matrix

def draw_lines():
    for i in range(ROWS+1):
        pygame.draw.line(SCREEN, BLACK, (0, NODE_SIZE * i), (WIDTH, NODE_SIZE * i))
    for i in range(COLS):
        pygame.draw.line(SCREEN, BLACK, (i * NODE_SIZE, 0), (i * NODE_SIZE, HEIGHT))
    pygame.draw.line(SCREEN, BLACK, (BUTTONWIDTH, HEIGHT), (BUTTONWIDTH, HEIGHT + BUTTONHEIGHT))
    pygame.draw.line(SCREEN, BLACK, (2 * BUTTONWIDTH, HEIGHT), (2 * BUTTONWIDTH, HEIGHT + BUTTONHEIGHT))
    pygame.draw.line(SCREEN, BLACK, (7 * BUTTONWIDTH/2, HEIGHT), (7 * BUTTONWIDTH / 2, HEIGHT + BUTTONHEIGHT))
    pygame.draw.line(SCREEN, BLACK, (9 * BUTTONWIDTH/2, HEIGHT), (9 * BUTTONWIDTH / 2, HEIGHT + BUTTONHEIGHT))

def draw_nodes(matrix):
    SCREEN.fill(WHITE)
    for row in matrix:
        for node in row:
            node.draw()

def update_neighbours(matrix):
    for row in matrix:
        for node in row:
            node.updateNodes(matrix)

def reset_nodes(matrix):
    for row in matrix:
        for node in row:
            node.reset()         

def randomMatrixGenerator(matrix):
    randomNumbers = []
    for i in range(ROWS):
        randomNumbers.append([])
        for j in range(COLS):
            randomNumbers[i].append(random.randint(0,10))
    for i in range(ROWS):
        for j in range(COLS):
            if randomNumbers[i][j] >= 7:
                matrix[i][j].do_wall()
            else:
                matrix[i][j].reset()



    

    



