from pieces.piece import Piece


class Knight(Piece):
    def __init__(self, coordinates_x, coordinates_y, player_color):
        super(Knight, self).__init__(coordinates_x, coordinates_y, player_color)
        # Knight symbol
        self.name = "N"

    def can_move(self, board):
        return self.get_list_possible_move(board)

    def get_list_possible_move(self, board):
        list_possible_move = []
        position_1 = (self.coordinates_x + 3, self.coordinates_y)
        position_2 = (self.coordinates_x - 3, self.coordinates_y)

        for i in [-2,2,-1,1]:
            piece = board.get_piece_at(position_1[0] - abs(i), position_1[1] + i)
            if piece is None or piece.player_color != self.player_color:
                list_possible_move.append((position_1[0] - abs(i), position_1[1] + i))

        for i in [-2,2,-1,1]:
            piece = board.get_piece_at(position_2[0] + abs(i), position_2[1] + i)
            if piece is None or piece.player_color != self.player_color:
                list_possible_move.append((position_2[0] + abs(i), position_2[1] + i))

        return list_possible_move
