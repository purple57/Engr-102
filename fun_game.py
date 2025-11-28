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
import pygame
import boardfunc

def main():
    pygame.init()
    window = pygame.display.set_mode((1000,800))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        pygame.draw.rect(window,(50,50,50),(0,0,1000,800))

        boardfunc.board(window,50,50)
        boardfunc.beginplacement(window, boardfunc.mydict)
        #Middle = half of screen - half of rect size


        pygame.display.update()    

    pygame.quit()

if __name__ == "__main__":
    main()
    print(boardfunc.mydict)
