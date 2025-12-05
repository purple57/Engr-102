import king
import queen
import rook
import bishop
import knight
import pawn
import check

def filter_safe_moves(start, moves, pieces, has_moved, rook_positions, color):
    """Return only moves that do not leave the king in check."""
    safe_moves = []
    for move in moves:
        new_pieces = pieces.copy()
        new_pieces[move] = new_pieces[start]
        del new_pieces[start]
        if not check.is_in_check(color, new_pieces, has_moved, rook_positions):
            safe_moves.append(move)
    return safe_moves

def is_checkmate_or_stalemate(color, pieces, has_moved, rook_positions):
    """
    Determine if the given color is checkmated or stalemated.
    Returns:
        "checkmate" if the king is in check and no legal moves exist,
        "stalemate" if the king is not in check and no legal moves exist,
        None if there are still legal moves.
    """
    in_check = check.is_in_check(color, pieces, has_moved, rook_positions)

    # Loop through all pieces of this color
    for sq, (ptype, pcolor, _) in pieces.items():
        if pcolor == color:
            if ptype == "king":
                moves = king.get_legal_moves(sq, pieces, has_moved, rook_positions)
            elif ptype == "queen":
                moves = queen.get_legal_moves(sq, pieces)
            elif ptype == "rook":
                moves = rook.get_legal_moves(sq, pieces)
            elif ptype == "bishop":
                moves = bishop.get_legal_moves(sq, pieces)
            elif ptype == "knight":
                moves = knight.get_legal_moves(sq, pieces)
            elif ptype == "pawn":
                moves = pawn.get_legal_moves(sq, pieces, pcolor)
            else:
                moves = []

            safe_moves = filter_safe_moves(sq, moves, pieces, has_moved, rook_positions, pcolor)
            if safe_moves:
                return None  # At least one legal move exists

    # No legal moves found
    if in_check:
        return "checkmate"
    else:
        return "stalemate"


