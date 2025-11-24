#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
# Names: Ismael Ortega
# Manning Phan
# Caitlyn Brown
# Anita Kumar
# Section: 504 & 404
# Assignment: Chess game - Chapter 13 Lab
# Date: 11/20/25

import numpy as np
import pygame

pygame.init()
W, H = 600, 600
screen = pygame.display.set_mode((900, 900))
#pygame.draw(0, 0, W, H)

square = pygame.Rect(0, 0, 50, 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0,0,0), square)


    
    





boardsize = [["R","Kn","B","K","Q","B","Kn","R"],
             ["P","P","P","P","P","P","P","P"],
             ["","","","","","","",""],
             ["","","","","","","",""],
             ["","","","","","","",""],
             ["","","","","","","",""],
             ["P","P","P","P","P","P","P","P"],
             ["R","Kn","B","K","Q","B","Kn","R"]]
