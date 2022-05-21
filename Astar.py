import pygame
import math
import numpy
import matrix
from queue import PriorityQueue

def hFunction(Vector2D_1, Vector2D_2):
    return abs(Vector2D_1.x - Vector2D_2.x) + abs(Vector2D_1.y - Vector2D_2.y)

def constructPath(cameFrom, current, _matrix):
    print("constructing the path")
    while current in cameFrom:
        current = cameFrom[current]
        current.do_path()
        matrix.draw_nodes(_matrix)
        matrix.draw_lines()


def Algorithm(_matrix, start_node, end_node):
    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start_node))
    cameFrom = {}
    gScore = {node: float("inf") for rows in _matrix for node in rows}
    gScore[start_node] = 0
    fScore = {node: float("inf") for rows in _matrix for node in rows}
    fScore[start_node] = hFunction(start_node.position, end_node.position)
    
    openSetHash = {start_node}

    while not openSet.empty():
        current = openSet.get()[2]
        openSetHash.remove(current)
        if current == end_node:
            constructPath(cameFrom, current, _matrix)
            end_node.do_end()
            start_node.do_start()
            return True
        for neighbour in current.neighbours:
            tempGscore = gScore[current] + 1

            if tempGscore < gScore[neighbour]:
                cameFrom[neighbour] = current
                gScore[neighbour] = tempGscore
                fScore[neighbour] = tempGscore + hFunction(neighbour.position, end_node.position)
                if neighbour not in openSetHash:
                    count += 1
                    openSetHash.add(neighbour)
                    openSet.put((fScore[neighbour], count, neighbour))
                    neighbour.do_open()
        if current != start_node:
            current.do_closed()

        matrix.draw_nodes(_matrix)
        matrix.draw_lines()
        pygame.display.update()
            

    return False