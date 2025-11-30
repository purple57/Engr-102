import pygame
mydict={}
pieceonboard = {}
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
                count += 1
        else:
            for j in range(8):
                if count % 2 != 0:
                    pygame.draw.rect(window,(197,140,99),(x+i*75,y+j*75,75,75))
                else:
                    pygame.draw.rect(window,(250,236,210),(x+i*75,y+j*75,75,75))
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
                count += 1
    return True

def beginplacement(window, diction):
    chesspiece = []
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
    
    def click(self,window):
        pos = pygame.mouse.get_pos()
        #print(pos)

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                print("Add")
        #Draw pieces

def main():
    pygame.init()
    window = pygame.display.set_mode((1000,800))
    
    blpawn_img = pygame.image.load("C:\\Users\\Manning\\Downloads\\blackpawn.png").convert_alpha()

    running = True
    while running:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            pygame.draw.rect(window,(50,50,50),(0,0,1000,800))

            board(window,50,50)
            beginplacement(window, mydict)
            #Middle = half of screen - half of rect size

            #Draw then use click and if statement and draw where you can move
            #Use click to add value to y or x and use click twice to make it false
            blpawn1 = Pieces((mydict["a7"]), blpawn_img)
            blpawn2 = Pieces((mydict["b7"]), blpawn_img)
            blpawn3 = Pieces((mydict["c7"]), blpawn_img)
            blpawn4 = Pieces((mydict["d7"]), blpawn_img)
            blpawn5 = Pieces((mydict["e7"]), blpawn_img)
            blpawn6 = Pieces((mydict["f7"]), blpawn_img)
            blpawn7 = Pieces((mydict["g7"]), blpawn_img)
            blpawn8 = Pieces((mydict["h7"]), blpawn_img)
            blpawn1.draw(window)
            if blpawn1.rect.collidepoint(pos):
                print("hover")
            blpawn2.draw(window)
            blpawn3.draw(window)
            blpawn4.draw(window)
            blpawn5.draw(window)
            blpawn6.draw(window)
            blpawn7.draw(window)
            blpawn8.draw(window)
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("clicked")
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
