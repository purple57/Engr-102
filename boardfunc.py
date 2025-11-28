import pygame
mydict={}
whitelist = ["a1", "a2", "b1", "b2", "c1", "c2", "d1", "d2", "e1", "e2", "f1", "f2", "g1", "g2", "h1", "h2"]
blaclist = ["a7", "a8", "b7", "b8", "c7", "c8", "d7", "d8", "e7", "e8", "f7", "f8", "g7", "g8", "h7", "h8"]
def board(window,sizex,sizey):
    count = 1
    x = 200
    y = 100
    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if count % 2 == 0:
                    pygame.draw.rect(window,(197,140,99),(x+i*75,y+j*75,75,75))
                else:
                    pygame.draw.rect(window,(250,236,210),(x+i*75,y+j*75,75,75))
                if i == 0:
                    mydict[f"a{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 1:
                    mydict[f"b{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 2:
                    mydict[f"c{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 3:
                    mydict[f"d{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 4:
                    mydict[f"e{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 5:
                    mydict[f"f{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 6:
                    mydict[f"g{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 7:
                    mydict[f"h{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                count += 1
        else:
            for j in range(8):
                if count % 2 != 0:
                    pygame.draw.rect(window,(197,140,99),(x+i*75,y+j*75,75,75))
                else:
                    pygame.draw.rect(window,(250,236,210),(x+i*75,y+j*75,75,75))
                if i == 0:
                    mydict[f"a{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 1:
                    mydict[f"b{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 2:
                    mydict[f"c{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 3: 
                    mydict[f"d{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 4:
                    mydict[f"e{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 5:
                    mydict[f"f{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 6:
                    mydict[f"g{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                elif i == 7:
                    mydict[f"h{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4, sizex, sizey)
                count += 1
    return True

def beginplacement(window, diction):
    for i in whitelist:
        pygame.draw.rect(window,(195,186,191),(diction[i]))
    for i in blaclist:
        pygame.draw.rect(window,(30,30,30),(diction[i]))
    return True
