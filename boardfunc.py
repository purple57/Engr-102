
import pygame
mydict={}
pieceonboard = {}
whitelist = ["a1", "a2", "b1", "b2", "c1", "c2", "d1", "d2", "e1", "e2", "f1", "f2", "g1", "g2", "h1", "h2"]
blaclist = ["a7", "a8", "b7", "b8", "c7", "c8", "d7", "d8", "e7", "e8", "f7", "f8", "g7", "g8", "h7", "h8"]
def board(sizex=50,sizey=50):
    x = 200
    y = 100
    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if i == 0:
                    mydict[f"a{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 1:
                    mydict[f"b{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 2:
                    mydict[f"c{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 3:
                    mydict[f"d{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 4:
                    mydict[f"e{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 5:
                    mydict[f"f{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 6:
                    mydict[f"g{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 7:
                    mydict[f"h{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
        else:
            for j in range(8):
                if i == 0:
                    mydict[f"a{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 1:
                    mydict[f"b{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 2:
                    mydict[f"c{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 3: 
                    mydict[f"d{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 4:
                    mydict[f"e{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 5:
                    mydict[f"f{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 6:
                    mydict[f"g{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
                elif i == 7:
                    mydict[f"h{j+1}"] = ((x+i*75)+sizex/4,(y+j*75)+sizey/4)
    return True

def beginplacement():
    for i in whitelist:
        if "2" in i:
            pieceonboard[i] = "white pawn"
        elif "a1" == i or "h1" == i:
            pieceonboard[i] = "white rook"
        elif "b1" == i or "g1" == i:
            pieceonboard[i] = "white knight"
        elif "c1" == i or "f1" == i:
            pieceonboard[i] = "white bishop"
        elif "d1" == i:
            pieceonboard[i] = "white queen"
        elif "e1"== i:
            pieceonboard[i] = "white king"
    for i in blaclist:
        if "7" in i:
            pieceonboard[i] = "black pawn"
        elif "a8" == i or "h8" == i:
            pieceonboard[i] = "black rook"
        elif "b8" == i or "g8" == i:
            pieceonboard[i] = "black knight"
        elif "c8" == i or "f8" == i:
            pieceonboard[i] = "black bishop"
        elif "d8" == i:
            pieceonboard[i] = "black queen"
        elif "e8"== i:
            pieceonboard[i] = "black king"
    return True

class Pieces():
    
    def __init__(self,post,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = post


    def draw(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #Draw pieces
