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


mydict={}
count = 1

pygame.init()
window = pygame.display.set_mode((1000,800))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.draw.rect(window,(255,255,255),(200,100,600,600))
    x = 200
    y = 100
    #Middle = half of screen - half of rect size
    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if count % 2 == 0:
                    pygame.draw.rect(window,(255,0,0),(x+i*75,y+j*75,75,75))
                else:
                    pygame.draw.rect(window,(0,100,255),(x+i*75,y+j*75,75,75))
                if i == 0:
                    mydict[f"a{j+1}"] = (x+i*75,y+i*75)
                elif i == 1:
                    mydict[f"b{j+1}"] = (x+i*75,y+i*75)
                elif i == 2:
                    mydict[f"c{j+1}"] = (x+i*75,y+i*75)
                elif i == 3:
                    mydict[f"d{j+1}"] = (x+i*75,y+i*75)
                elif i == 4:
                    mydict[f"e{j+1}"] = (x+i*75,y+i*75)
                elif i == 5:
                    mydict[f"f{j+1}"] = (x+i*75,y+i*75)
                elif i == 6:
                    mydict[f"g{j+1}"] = (x+i*75,y+i*75)
                elif i == 7:
                    mydict[f"h{j+1}"] = (x+i*75,y+i*75)
                count += 1
        else:
            for j in range(8):
                if count % 2 != 0:
                    pygame.draw.rect(window,(255,0,0),(x+i*75,y+j*75,75,75))
                else:
                    pygame.draw.rect(window,(0,100,255),(x+i*75,y+j*75,75,75))
                if i == 0:
                    mydict[f"a{j+1}"] = (x+i*75,y+i*75)
                elif i == 1:
                    mydict[f"b{j+1}"] = (x+i*75,y+i*75)
                elif i == 2:
                    mydict[f"c{j+1}"] = (x+i*75,y+i*75)
                elif i == 3:
                    mydict[f"d{j+1}"] = (x+i*75,y+i*75)
                elif i == 4:
                    mydict[f"e{j+1}"] = (x+i*75,y+i*75)
                elif i == 5:
                    mydict[f"f{j+1}"] = (x+i*75,y+i*75)
                elif i == 6:
                    mydict[f"g{j+1}"] = (x+i*75,y+i*75)
                elif i == 7:
                    mydict[f"h{j+1}"] = (x+i*75,y+i*75)
                count += 1

    pygame.display.update()    

print(mydict)
pygame.quit()
