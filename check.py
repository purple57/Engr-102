# check.py
import king
import queen
import rook
import bishop
import knight
import pawn

def is_in_check(color, pieces, has_moved, rook_positions):
    """Return True if the king of given color is in check."""
    # Find king square
    king_square = None
    for sq, (ptype, pcolor, _) in pieces.items():
        if ptype == "king" and pcolor == color:
            king_square = sq
            break
    if not king_square:
        return False

    # Check all opponent moves
    for sq, (ptype, pcolor, _) in pieces.items():
        if pcolor != color:
            if ptype == "queen":
                moves = queen.get_legal_moves(sq, pieces)
            elif ptype == "rook":
                moves = rook.get_legal_moves(sq, pieces)
            elif ptype == "bishop":
                moves = bishop.get_legal_moves(sq, pieces)
            elif ptype == "knight":
                moves = knight.get_legal_moves(sq, pieces)
            elif ptype == "pawn":
                moves = pawn.get_legal_moves(sq, pieces, pcolor)
            elif ptype == "king":
                # Use for_check=True: adjacent king threats only, no castling
                moves = king.get_legal_moves(
                    sq, pieces, has_moved, rook_positions, for_check=True
                )
            else:
                moves = []

            if king_square in moves:
                return True

    return False
