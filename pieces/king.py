from pieces.piece import Piece


class King(Piece):
    def __init__(self, coordinates_x, coordinates_y, player_color):
        super(King, self).__init__(coordinates_x, coordinates_y, player_color)
        # King symbol
        self.name = "K"

    def can_move(self, board):
        list_possible_move = []
        present_position = (self.coordinates_x, self.coordinates_y)
        for i in [present_position[1] - 1, present_position[1], present_position[1] + 1]:
            for j in [present_position[0] - 1, present_position[0], present_position[0] + 1]:
                piece = board.get_piece_at(j, i)
                if piece is None or piece.player_color != self.player_color:
                    list_possible_move.append((j, i))
        if self.is_first_move is True:
            rook_right = board.get_piece_at(self.coordinates_x, self.coordinates_y + 3)
            rook_left = board.get_piece_at(self.coordinates_x, self.coordinates_y - 4)
            if rook_right is not None and rook_right.is_first_move is True:
                if (self.coordinates_x, self.coordinates_y + 1) in list_possible_move and \
                        board.get_piece_at(self.coordinates_x, self.coordinates_y + 2) is None:
                    list_possible_move.append((self.coordinates_x, self.coordinates_y + 2))
            if rook_left is not None and rook_left.is_first_move is True:
                if (self.coordinates_x, self.coordinates_y - 1) in list_possible_move and \
                        board.get_piece_at(self.coordinates_x, self.coordinates_y - 2) is None:
                    list_possible_move.append((self.coordinates_x, self.coordinates_y - 2))
        return list_possible_move

    def get_rook_already_use_in_corners(self, board):
        list_rook = {
            "rook_left": None,
            "rook_right": None
        }
        rook_right = board.get_piece_at(self.coordinates_x, self.coordinates_y + 3)
        rook_left = board.get_piece_at(self.coordinates_x, self.coordinates_y - 4)
        if rook_right is not None and rook_right.is_first_move is True:
            list_rook["rook_right"] = rook_right
        if rook_left is not None and rook_left.is_first_move is True:
            list_rook["rook_left"] = rook_left
