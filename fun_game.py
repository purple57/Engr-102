# By submitting this assignment, I agree to the following:
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
import king, queen, rook, bishop, knight, pawn, check, endgame

piece_values = {"pawn":1,"knight":3,"bishop":3,"rook":5,"queen":9,"king":0}

def filter_safe_moves(start,moves,pieces,has_moved,rook_positions,color):
    safe=[]
    for move in moves:
        new_pieces=pieces.copy()
        new_pieces[move]=new_pieces[start]
        del new_pieces[start]
        if not check.is_in_check(color,new_pieces,has_moved,rook_positions):
            safe.append(move)
    return safe

def promote_pawn(window,color,wq,wr,wb,wn,bq,br,bb,bn):
    font=pygame.font.SysFont(None,36)
    options=["queen","rook","bishop","knight"]
    images={"white":{"queen":wq,"rook":wr,"bishop":wb,"knight":wn},
            "black":{"queen":bq,"rook":br,"bishop":bb,"knight":bn}}
    window.fill((200,200,200))
    for i,opt in enumerate(options):
        text=font.render(opt.capitalize(),True,(0,0,0))
        rect=pygame.Rect(200,100+i*100,200,80)
        pygame.draw.rect(window,(150,150,150),rect)
        window.blit(text,(rect.x+20,rect.y+20))
    pygame.display.update()
    chosen=None
    while chosen is None:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: pygame.quit(); exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                for i,opt in enumerate(options):
                    rect=pygame.Rect(200,100+i*100,200,80)
                    if rect.collidepoint(pos): chosen=opt; break
    return chosen,images[color][chosen]

def main():
    pygame.init()
    window=pygame.display.set_mode((1000,800))
    font=pygame.font.SysFont(None,36)

    # --- UI assets ---
    homepage=pygame.image.load("home page.png").convert_alpha()
    insturctions=pygame.image.load("insturctions.png").convert_alpha()
    startbutton=pygame.image.load("start button.png").convert_alpha()
    inbutton=pygame.image.load("instructions button.png").convert_alpha()
    outbutton=pygame.image.load("back button.png").convert_alpha()
    start_rect=pygame.Rect(688,673,262,77)
    instructions_rect=pygame.Rect(376,673,262,77)
    back_rect=pygame.Rect(738,723,262,77)

    # --- Piece images ---
    def scale(img): return pygame.transform.scale(img,(75,75))
    white_king=scale(pygame.image.load("white_king.png"))
    white_queen=scale(pygame.image.load("white_queen.png"))
    black_king=scale(pygame.image.load("black_king.png"))
    black_queen=scale(pygame.image.load("black_queen.png"))
    white_rook=scale(pygame.image.load("white_rook.png"))
    black_rook=scale(pygame.image.load("black_rook.png"))
    white_bishop=scale(pygame.image.load("white_bishop.png"))
    black_bishop=scale(pygame.image.load("black_bishop.png"))
    white_knight=scale(pygame.image.load("white_knight.png"))
    black_knight=scale(pygame.image.load("black_knight.png"))
    white_pawn=scale(pygame.image.load("white_pawn.png"))
    black_pawn=scale(pygame.image.load("black_pawn.png"))

    # --- Game state ---
    pieces={
        "a1":("rook","white",white_rook),"b1":("knight","white",white_knight),
        "c1":("bishop","white",white_bishop),"d1":("queen","white",white_queen),
        "e1":("king","white",white_king),"f1":("bishop","white",white_bishop),
        "g1":("knight","white",white_knight),"h1":("rook","white",white_rook),
        **{f"{c}2":("pawn","white",white_pawn) for c in "abcdefgh"},
        "a8":("rook","black",black_rook),"b8":("knight","black",black_knight),
        "c8":("bishop","black",black_bishop),"d8":("queen","black",black_queen),
        "e8":("king","black",black_king),"f8":("bishop","black",black_bishop),
        "g8":("knight","black",black_knight),"h8":("rook","black",black_rook),
        **{f"{c}7":("pawn","black",black_pawn) for c in "abcdefgh"},
    }
    has_moved={"white_king":False,"black_king":False,"a1":False,"h1":False,"a8":False,"h8":False}
    rook_positions={"white":["a1","h1"],"black":["a8","h8"]}
    selected_piece=None; legal_moves=[]; game_over=False
    current_turn="white"; white_score=0; black_score=0
    winner_text=""; en_passant_target=None
    page=0

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: running=False; break

            if page==0 and event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if start_rect.collidepoint(pos): page=2
                elif instructions_rect.collidepoint(pos): page=1

            elif page==1 and event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if back_rect.collidepoint(pos): page=0

            elif page==2 and not game_over and event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                for square,rect in boardfunc.mydict.items():
                    x,y,w,h=rect
                    if x<=pos[0]<=x+w and y<=pos[1]<=y+h:
                        if selected_piece is None:
                            if square in pieces:
                                piece_type,color,image=pieces[square]
                                if color!=current_turn: continue
                                selected_piece=square
                                if piece_type=="king": moves=king.get_legal_moves(square,pieces,has_moved,rook_positions)
                                elif piece_type=="queen": moves=queen.get_legal_moves(square,pieces)
                                elif piece_type=="rook": moves=rook.get_legal_moves(square,pieces)
                                elif piece_type=="bishop": moves=bishop.get_legal_moves(square,pieces)
                                elif piece_type=="knight": moves=knight.get_legal_moves(square,pieces)
                                elif piece_type=="pawn": moves=pawn.get_legal_moves(square,pieces,color,en_passant_target)
                                else: moves=[]
                                legal_moves=filter_safe_moves(square,moves,pieces,has_moved,rook_positions,color)
                        else:
                            piece_type,color,image=pieces[selected_piece]
                            if square in legal_moves:
                                # En passant capture
                                if piece_type=="pawn" and square==en_passant_target:
                                    captured_file=square[0]
                                    captured_rank=str(int(square[1])+(-1 if color=="white" else 1))
                                    captured_square=f"{captured_file}{captured_rank}"
                                    if captured_square in pieces:
                                        captured_type,captured_color,_=pieces[captured_square]
                                        if captured_color!=color:
                                            if color=="white": white_score+=piece_values[captured_type]
                                            else: black_score+=piece_values[captured_type]
                                            del pieces[captured_square]

                                # Normal capture
                                elif square in pieces:
                                    captured_type,captured_color,_=pieces[square]
                                    if captured_color!=color:
                                        if color=="white": white_score+=piece_values[captured_type]
                                        else: black_score+=piece_values[captured_type]

                                # Castling
                                if piece_type=="king" and abs(ord(square[0])-ord(selected_piece[0]))==2:
                                    if square[0]=="g":
                                        rook_start="h1" if color=="white" else "h8"
                                        rook_end="f1" if color=="white" else "f8"
                                    else:
                                        rook_start="a1" if color=="white" else "a8"
                                        rook_end="d1" if color=="white" else "d8"
                                    pieces[rook_end]=pieces[rook_start]; del pieces[rook_start]
                                    has_moved[rook_start]=True

                                # Move piece
                                pieces[square]=(piece_type,color,image)
                                del pieces[selected_piece]

                                # Promotion
                                if piece_type=="pawn":
                                    if (color=="white" and square[1]=="8") or (color=="black" and square[1]=="1"):
                                        chosen,img=promote_pawn(window,color,
                                            white_queen,white_rook,white_bishop,white_knight,
                                            black_queen,black_rook,black_bishop,black_knight)
                                        pieces[square] = (chosen, color, img)
                                        print(f"{color.capitalize()} pawn promoted to {chosen} at {square}!")

                                # --- Update movement flags ---
                                if piece_type == "king":
                                    has_moved[f"{color}_king"] = True
                                elif selected_piece in has_moved:
                                    has_moved[selected_piece] = True

                                # --- Update en passant target ---
                                if piece_type == "pawn":
                                    start_rank = int(selected_piece[1])
                                    end_rank = int(square[1])
                                    if abs(end_rank - start_rank) == 2:
                                        file = square[0]
                                        mid_rank = (start_rank + end_rank) // 2
                                        en_passant_target = f"{file}{mid_rank}"
                                    else:
                                        en_passant_target = None
                                else:
                                    en_passant_target = None

                                # --- Check for opponent in check/mate ---
                                opponent = "black" if color == "white" else "white"
                                if check.is_in_check(opponent, pieces, has_moved, rook_positions):
                                    print(f"{opponent.capitalize()} king is in CHECK!")

                                result = endgame.is_checkmate_or_stalemate(opponent, pieces, has_moved, rook_positions)
                                if result == "checkmate":
                                    print(f"{opponent.capitalize()} is CHECKMATED! {color.capitalize()} wins!")
                                    winner_text = f"{color.capitalize()} wins!"
                                    game_over = True
                                elif result == "stalemate":
                                    print("Stalemate! No winner.")
                                    winner_text = "Stalemate! No winner."
                                    game_over = True

                                if not game_over:
                                    current_turn = opponent
                                    print(f"It is now {current_turn}'s turn.")
                            else:
                                print(f"Invalid move for {piece_type}")
                            selected_piece = None
                            legal_moves = []

        # --- Drawing ---
        pygame.draw.rect(window,(50,50,50),(0,0,1000,800))

        if page == 0:
            window.blit(homepage,(0,0))
            window.blit(startbutton,start_rect.topleft)
            window.blit(inbutton,instructions_rect.topleft)

        elif page == 1:
            window.blit(insturctions,(0,0))
            window.blit(outbutton,back_rect.topleft)

        elif page == 2:
            boardfunc.board(window,50,50)
            boardfunc.beginplacement(window, boardfunc.mydict)

            if selected_piece:
                rect = boardfunc.mydict[selected_piece]
                pygame.draw.rect(window, (255, 255, 0), rect, 4)

            for square, (ptype, color, piece) in pieces.items():
                rect = boardfunc.mydict[square]
                window.blit(piece, (rect[0] + (rect[2]-75)//2, rect[1] + (rect[3]-75)//2))
                if ptype == "king":
                    if check.is_in_check(color, pieces, has_moved, rook_positions):
                        pygame.draw.rect(window, (255,0,0), rect, 4)

            if not game_over:
                for move in legal_moves:
                    rect = boardfunc.mydict[move]
                    center = (rect[0] + rect[2]//2, rect[1] + rect[3]//2)
                    pygame.draw.circle(window, (0,200,0), center, 15)

            score_text = font.render(f"White: {white_score}   Black: {black_score}", True, (255,255,255))
            window.blit(score_text, (750, 50))

            if game_over and winner_text:
                text_surface = font.render(winner_text, True, (255, 255, 0))
                window.blit(text_surface, (400, 20))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    print(boardfunc.mydict)
