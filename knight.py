# knight.py
def get_legal_moves(start, pieces):
    """
    Generate knight moves (L-shapes).
    """
    cols = "abcdefgh"
    col, row = start[0], int(start[1])
    moves = []

    jumps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    for dc, dr in jumps:
        nc = cols.index(col) + dc
        nr = row + dr
        if 0 <= nc < 8 and 1 <= nr <= 8:
            sq = f"{cols[nc]}{nr}"
            if sq not in pieces or pieces[sq][1] != pieces[start][1]:
                moves.append(sq)

    return moves

