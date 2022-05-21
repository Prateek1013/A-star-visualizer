import pygame
from config import *
import random
import math
from Astar import *
import queue
from nodes import *
import matrix
from UI import *

pygame.init()
pygame.mixer.init()

mymatrix = matrix.make_matrix()
KEYS = pygame.key.get_pressed()
MOUSEPOS = pygame.mouse.get_pos()
FONT = pygame.font.SysFont('Corbel',35) 
RESETTEXT = FONT.render('Reset' , True , BLACK) 
QUITTEXT = FONT.render('Quit' , True , BLACK) 
RANDOMTEXT = FONT.render('Random' , True , BLACK) 
SELFTEXT = FONT.render('Self' , True , BLACK)

class Game:
    def __init__(self):
        self.screen = SCREEN
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self._running = True
        self.algo = False
        self.start_node = None
        self.end_node = None
        self.selfAlgo = False

    def new(self):
        self.run()

    def run(self):
        self._playing = True
        while self._playing:
            self.events()
            if self.algo:
                mygame.run_algo()  
            self.update()
            self.draw() 
            self.clock.tick(FPS)
        

    def update(self):      
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self._playing == True:
                    self._playing = False
                self._running = False
            if event.type == pygame.KEYDOWN:
                if KEYS[pygame.K_RETURN]:
                    if not self.start_node or not self.end_node:
                        continue
                    else:
                        self.algo = True
            if not self.algo:
                if pygame.mouse.get_pressed()[0]:
                    if is_matrixButton(pygame.mouse.get_pos()):
                        node = mymatrix[pygame.mouse.get_pos()[0] // NODE_SIZE][pygame.mouse.get_pos()[1] // NODE_SIZE]
                        if not self.start_node:
                            self.start_node = node    
                            self.start_node.do_start()
                        elif not self.end_node and node != self.start_node:
                            self.end_node = node
                            self.end_node.do_end()
                        elif node != self.start_node and node != self.end_node:
                            node.do_wall()
                    if is_resetButton(pygame.mouse.get_pos()):
                        matrix.reset_nodes(mymatrix)
                        self.start_node = None
                        self.end_node = None
                        self.algo = False
                    if is_quitButton(pygame.mouse.get_pos()):
                        if self._playing == True:
                            self._playing = False
                        self._running = False
                    if is_randomButton(pygame.mouse.get_pos()):
                        matrix.reset_nodes(mymatrix)
                        self.start_node = None
                        self.end_node = None
                        self.algo = False
                        matrix.randomMatrixGenerator(mymatrix)
                    if is_selfButton(pygame.mouse.get_pos()):
                        self.selfAlgo = True
                if pygame.mouse.get_pressed()[2]:
                    if is_matrixButton(pygame.mouse.get_pos()):
                        node = mymatrix[pygame.mouse.get_pos()[0] // NODE_SIZE][pygame.mouse.get_pos()[1] // NODE_SIZE]
                        if node == self.start_node:
                            self.start_node = None
                        elif node == self.end_node:
                            self.end_node = None
                        node.reset()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    self.algo = True
                



    def draw(self):   
        matrix.draw_nodes(mymatrix)      
        drawResetButton()
        drawQuitButton()
        drawRandomButton()
        drawSelfButton()
        matrix.draw_lines()
        SCREEN.blit(RESETTEXT, (BUTTONWIDTH/5, HEIGHT+BUTTONHEIGHT/5)) 
        SCREEN.blit(QUITTEXT, (6*BUTTONWIDTH/5, HEIGHT+BUTTONHEIGHT/5)) 
        SCREEN.blit(RANDOMTEXT, (11*BUTTONWIDTH/5, HEIGHT+BUTTONHEIGHT/5)) 
        SCREEN.blit(SELFTEXT, (37*BUTTONWIDTH/10, HEIGHT+BUTTONHEIGHT/5))
        pygame.display.flip()

    def run_algo(self):
        matrix.update_neighbours(mymatrix)
        Algorithm(mymatrix, self.start_node, self.end_node)
        self.algo = False

    def show_start_screen(self):
        pass

    def show_end_screen(self):
        pass


mygame = Game()
mygame.show_start_screen()



while mygame._running:
    mygame.new()     
    mygame.show_end_screen()

pygame.quit()