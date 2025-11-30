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
    count = 1
    
    boardfunc.board()
    boardfunc.beginplacement()
    pygame.init()
    
    window = pygame.display.set_mode((1000,800))
    
    blpawn_img = pygame.image.load("C:\\Users\\Manning\\Downloads\\blackpawn.png").convert_alpha()
    blpawn1 = boardfunc.Pieces((Fuckaround.mydict["a7"]), blpawn_img)
    
    clicking = True

    running = True

    pygame.draw.rect(window,(50,50,50),(0,0,1000,800))


    while running:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicking = not clicking
                
        for i in Fuckaround.mydict:
            if "a" in i or "c" in i or "e" in i or "g" in i:
                if count%2 == 0:
                    pygame.draw.rect(window, (197,140,99), (Fuckaround.mydict[i][0]-50/4, Fuckaround.mydict[i][1]-50/4, 75, 75))
                else:
                    pygame.draw.rect(window, (250,236,210), (Fuckaround.mydict[i][0]-50/4, Fuckaround.mydict[i][1]-50/4, 75, 75))
                count += 1
            elif "b" in i or "d" in i or "f" in i or "h" in i:
                if count%2 != 0:
                    pygame.draw.rect(window, (197,140,99), (Fuckaround.mydict[i][0]-50/4, Fuckaround.mydict[i][1]-50/4, 75, 75))
                else:
                    pygame.draw.rect(window, (250,236,210), (Fuckaround.mydict[i][0]-50/4, Fuckaround.mydict[i][1]-50/4, 75, 75))
                count += 1
    
        blpawn1.draw(window)
                    
        if clicking:
            pygame.draw.rect(window,(195,186,191), placementsquare)
            print("clicked")
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
