from pieces.piece import Piece
from pieces.bishop import Bishop
from pieces.rook import Rook


class Queen(Piece):
    def __init__(self, coordinates_x, coordinates_y, player_color):
        super(Queen, self).__init__(coordinates_x,coordinates_y,player_color)
        # Queen symbol
        self.name = "Q"

    def can_move(self, board):
        bishop_component = Bishop(self.coordinates_x,self.coordinates_y,self.player_color)
        rook_component = Rook(self.coordinates_x, self.coordinates_y, self.player_color)
        list_move_bishop = bishop_component.can_move(board)
        list_move_rook = rook_component.can_move(board)
        list_move_bishop.extend(list_move_rook)
        return list_move_bishop


