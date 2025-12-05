# queen.py
def get_legal_moves(start, pieces):
    """Return a list of legal squares for the queen, with blocking rules."""
    cols = "abcdefgh"
    start_col, start_row = start[0], int(start[1])
    moves = []

    directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    for dc, dr in directions:
        nc = cols.index(start_col)
        nr = start_row
        while True:
            nc += dc
            nr += dr
            if not (0 <= nc < 8 and 1 <= nr <= 8):
                break
            sq = f"{cols[nc]}{nr}"
            if sq in pieces:
                # Can capture opponent but stop afterwards
                if pieces[sq][1] != pieces[start][1]:
                    moves.append(sq)
                break
            moves.append(sq)

    return moves


