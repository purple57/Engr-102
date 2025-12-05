import pygame

mydict = {}
cols = "abcdefgh"

def board(window, x, y):
    size = 75
    font = pygame.font.SysFont(None, 24)

    for row in range(8):          # row = 0..7
        for col in range(8):      # col = 0..7
            # Flip vertical orientation: rank 1 at bottom, rank 8 at top
            rect = (x + col*size, y + (7-row)*size, size, size)
            square = f"{cols[col]}{row+1}"   # rank labels 1..8
            mydict[square] = rect

            # Standard chessboard colors
            color = (240,217,181) if (row+col)%2==0 else (181,136,99)
            pygame.draw.rect(window, color, rect)

            # --- Draw rank/file labels ---
            # Draw file letter at bottom edge (row == 0 → rank 1 at bottom)
            if row == 0:
                text = font.render(cols[col], True, (0,0,0))
                window.blit(text, (rect[0] + size//2 - text.get_width()//2,
                                   rect[1] + size - text.get_height()))

            # Draw rank number at left edge (col == 0)
            if col == 0:
                text = font.render(str(row+1), True, (0,0,0))
                window.blit(text, (rect[0] + 2, rect[1] + 2))

def beginplacement(window, mydict):
    # Optional: debug overlay of square names
    font = pygame.font.SysFont(None, 18)
    for square, rect in mydict.items():
        text = font.render(square, True, (50,50,50))
        window.blit(text, (rect[0]+2, rect[1]+2))
