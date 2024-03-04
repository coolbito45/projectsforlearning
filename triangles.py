import numpy as np
import pygame, sys
from pygame.locals import *
from dataclasses import dataclass

@dataclass
class Triangle:
    a: tuple[float, float]
    b: tuple[float, float]
    c: tuple[float, float]
    color: tuple[int, int, int]

pygame.init()
screen = pygame.display.set_mode((800 , 600))
pygame.display.set_caption('we are some pygamers')

matrix = np.eye(3)*100

print(matrix)
# print(np.dot(matrix, (1,0,0)))

triangles = [
    Triangle(
        (0,0), (1, 1), (0, 1), (255,0,0)
    ),
    Triangle(
        (0,0), (1, 0), (1,1), (255,0,0)
    )
]
tx = 1
ty = 1

def make_translation_matrix(tx, ty):
    translation_matrix = [
        [1,0,tx],
        [0,1,ty],
        [0,0,1]
    ]
    return translation_matrix

WHITE = (255, 255, 255)

translation_matrix = [make_translation_matrix(1, 1), make_translation_matrix(1.2, 0.8)]
while True:
    for event in pygame.event.get():
        screen.fill(WHITE)

        for i, triangle in enumerate(triangles):        
            transformed_vertexi = []
            local_matrix = np.dot(matrix, translation_matrix[i])
            for point in [triangle.a, triangle.b, triangle.c]:
                new_point = [*point, 1]
                transformed_pt = np.dot(local_matrix, new_point)
                transformed_vertexi.append(transformed_pt[:-1])
            pygame.draw.polygon(screen, triangle.color, transformed_vertexi) 
        pygame.display.flip()