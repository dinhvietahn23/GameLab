from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, coordinates_x, coordinates_y, player_color):
        super(Pawn, self).__init__(coordinates_x, coordinates_y, player_color)
        self.name = "P"

    def can_move(self, board):
        return self.get_list_possible_move(board)

    def get_list_possible_move(self, board):
        ONE = -1
        TWO = -2
        if self.player_color == "b":
            ONE = 1
            TWO = 2
        list_possible_move = []
        present_position = (self.coordinates_x, self.coordinates_y)

        if self.is_first_move:
            if board.get_piece_at(present_position[0] + TWO, present_position[1]) is None and \
                    board.get_piece_at(present_position[0] + ONE, present_position[1]) is None:
                list_possible_move.append((present_position[0] + TWO, present_position[1]))
        for i in [-1, 0, 1]:
            if i == 0:
                if board.get_piece_at(present_position[0] + ONE, present_position[1] + i) is None:
                    list_possible_move.append((present_position[0] + ONE, present_position[1] + i))
            else:
                piece = board.get_piece_at(present_position[0] + ONE, present_position[1] + i)
                if piece is not None and piece.player_color != self.player_color:
                    list_possible_move.append((present_position[0] + ONE, present_position[1] + i))

        return list_possible_move
