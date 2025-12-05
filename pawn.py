# pawn.py
def get_legal_moves(square, pieces, color, en_passant_target=None):
    """
    Generate legal pawn moves including en passant.
    square: current square (e.g. "e5")
    pieces: dict of board state
    color: "white" or "black"
    en_passant_target: square string (e.g. "d6") if en passant is possible, else None
    """
    moves = []
    file = square[0]
    rank = int(square[1])

    direction = 1 if color == "white" else -1
    start_rank = 2 if color == "white" else 7
    promotion_rank = 8 if color == "white" else 1

    # --- Forward move ---
    forward_square = f"{file}{rank + direction}"
    if forward_square not in pieces:
        moves.append(forward_square)
        # Double move from starting rank
        if rank == start_rank:
            double_square = f"{file}{rank + 2*direction}"
            if double_square not in pieces:
                moves.append(double_square)

    # --- Captures ---
    for df in [-1, 1]:
        capture_file = chr(ord(file) + df)
        if "a" <= capture_file <= "h":
            capture_square = f"{capture_file}{rank + direction}"
            if capture_square in pieces and pieces[capture_square][1] != color:
                moves.append(capture_square)

    # --- En passant ---
    if en_passant_target:
        target_file = en_passant_target[0]
        target_rank = int(en_passant_target[1])
        if abs(ord(file) - ord(target_file)) == 1 and target_rank == rank + direction:
            # White pawns must be on rank 5, black pawns on rank 4
            if (color == "white" and rank == 5) or (color == "black" and rank == 4):
                moves.append(en_passant_target)

    # --- Promotion handling ---
    # (Promotion is handled in fun_game.py when a pawn reaches promotion_rank)

    return moves



