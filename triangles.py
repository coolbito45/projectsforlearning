import numpy as np
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('we are some pygamers')

matrix = np.eye(3)*100

print(matrix)
# print(np.dot(matrix, (1,0,0)))

triangles = [
    [ (0,0), (1, 1), (0, 1)],
    [(0,0), (1, 0), (1,1)]
]
tx = 0
ty = float(input('how d out oiweafn twtoasnfdiorm '))

def make_translation_matrix(tx, ty):
    translation_matrix = [
        [1,0,tx],
        [0,1,ty],
        [0,0,1]
    ]
    return translation_matrix

translation_matrix = make_translation_matrix(tx, ty)
matrix = np.dot(matrix, translation_matrix)
while True:
    for event in pygame.event.get():
        screen.fill((0, 0, 0))


        for triangle in triangles:        
            transformed_vertexi = []
            for point in triangle:
                new_point = [*point, 1]
                transformed_pt = np.dot(matrix, new_point)
                transformed_vertexi.append(transformed_pt[:-1])
            pygame.draw.polygon(screen, (255,255,255), transformed_vertexi)

 
        # pygame.draw.polygon(screen, (255, 255, 255), [ (0,0), (1, 100), (0, 100)])
        # # wer areaw  gonna mak ea  cube

        pygame.display.flip()