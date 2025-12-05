# rook.py
def get_legal_moves(start, pieces):
    """
    Generate rook moves (straight lines).
    """
    cols = "abcdefgh"
    col, row = start[0], int(start[1])
    moves = []

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for dc, dr in directions:
        nc, nr = cols.index(col), row
        while True:
            nc += dc
            nr += dr
            if not (0 <= nc < 8 and 1 <= nr <= 8):
                break
            sq = f"{cols[nc]}{nr}"
            if sq in pieces:
                if pieces[sq][1] != pieces[start][1]:
                    moves.append(sq)
                break
            moves.append(sq)

    return moves
