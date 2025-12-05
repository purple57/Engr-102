# king.py
def get_legal_moves(start, pieces, has_moved, rook_positions, for_check=False):
    """
    Return a list of legal squares for the king.
    - Normal moves: simulate each candidate; include only moves where the king is NOT in check after the move.
    - Castling: strictly enforced (cannot castle out of, through, or into check).
    - for_check=True: used by check detection; returns adjacent king moves without castling to avoid recursion.
    """
    cols = "abcdefgh"
    start_col, start_row = start[0], int(start[1])
    moves = []

    # Adjacent king moves (candidates)
    for dc in [-1, 0, 1]:
        for dr in [-1, 0, 1]:
            if dc == 0 and dr == 0:
                continue
            nc = cols.index(start_col) + dc
            nr = start_row + dr
            if 0 <= nc < 8 and 1 <= nr <= 8:
                sq = f"{cols[nc]}{nr}"
                # Can move if empty or occupied by enemy
                if sq not in pieces or pieces[sq][1] != pieces[start][1]:
                    moves.append(sq)

    # If we're generating moves for threat mapping, skip safety filtering and castling
    if for_check:
        return moves

    # Import here to avoid circular imports at module load time
    from check import is_in_check

    color = pieces[start][1]
    king_key = f"{color}_king"

    # Filter candidates: only keep moves where king is NOT in check after moving
    safe_moves = []
    for dest in moves:
        new_pieces = dict(pieces)
        # Move king on a shallow copy
        new_pieces[dest] = new_pieces[start]
        del new_pieces[start]
        if not is_in_check(color, new_pieces, has_moved, rook_positions):
            safe_moves.append(dest)

    # --- Castling ---
    # King must not have moved and must not currently be in check
    if king_key in has_moved and not has_moved[king_key]:
        if not is_in_check(color, pieces, has_moved, rook_positions):
            # Try both rooks on this color
            for rook_square in rook_positions[color]:
                # Rook must exist and not have moved
                if rook_square in pieces and pieces[rook_square][0] == "rook" and pieces[rook_square][1] == color:
                    if rook_square in has_moved and not has_moved[rook_square]:
                        king_col = cols.index(start_col)
                        rook_col = cols.index(rook_square[0])
                        step = 1 if rook_col > king_col else -1

                        # Squares between king and rook must be empty
                        path_clear = True
                        for c in range(king_col + step, rook_col, step):
                            sq = f"{cols[c]}{start_row}"
                            if sq in pieces:
                                path_clear = False
                                break
                        if not path_clear:
                            continue

                        # Simulate king standing on the intermediate square (passing through) and destination
                        intermediate_col = king_col + step
                        dest_col = king_col + 2 * step
                        intermediate_sq = f"{cols[intermediate_col]}{start_row}"
                        dest_sq = f"{cols[dest_col]}{start_row}"

                        # Simulate intermediate
                        temp_pieces = dict(pieces)
                        temp_pieces[intermediate_sq] = temp_pieces[start]
                        del temp_pieces[start]
                        if is_in_check(color, temp_pieces, has_moved, rook_positions):
                            continue

                        # Simulate destination
                        temp2_pieces = dict(pieces)
                        temp2_pieces[dest_sq] = temp2_pieces[start]
                        del temp2_pieces[start]
                        if is_in_check(color, temp2_pieces, has_moved, rook_positions):
                            continue

                        # If both simulations are safe, castling is legal
                        safe_moves.append(dest_sq)

    return safe_moves
