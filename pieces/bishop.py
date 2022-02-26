from pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, coordinates_x, coordinates_y, player_color="W"):
        super(Bishop, self).__init__(coordinates_x, coordinates_y, player_color)
        # Bishop symbol
        self.name = "B"
        self.direction = {
            "East": False,
            "West": False,
            "South": False,
            "North": False
        }

    def can_move(self, board):
        list_possible_move = []
        present_position = (self.coordinates_x, self.coordinates_y)

        self.direction = {
            "East": False,
            "West": False,
            "South": False,
            "North": False
        }

        for i in range(1, 9):
            if self.direction["East"] is False:
                if board.get_piece_at(present_position[0] + i, present_position[1] + i) is None:
                    list_possible_move.append((present_position[0] + i, present_position[1] + i))
                else:
                    if board.get_piece_at(present_position[0] + i,
                                          present_position[1] + i).player_color != board.player_turn:
                        list_possible_move.append((present_position[0] + i, present_position[1] + i))
                    self.direction["East"] = True

            if self.direction["West"] is False:
                if board.get_piece_at(present_position[0] - i, present_position[1] - i) is None:
                    list_possible_move.append((present_position[0] - i, present_position[1] - i))
                else:
                    if board.get_piece_at(present_position[0] - i,
                                          present_position[1] - i).player_color != board.player_turn:
                        list_possible_move.append((present_position[0] - i, present_position[1] - i))
                    self.direction["West"] = True

            if self.direction["South"] is False:
                if board.get_piece_at(present_position[0] - i, present_position[1] + i) is None:
                    list_possible_move.append((present_position[0] - i, present_position[1] + i))
                else:
                    if board.get_piece_at(present_position[0] - i,
                                          present_position[1] + i).player_color != board.player_turn:
                        list_possible_move.append((present_position[0] - i, present_position[1] + i))
                    self.direction["South"] = True

            if self.direction["North"] is False:
                if board.get_piece_at(present_position[0] + i, present_position[1] - i) is None:
                    list_possible_move.append((present_position[0] + i, present_position[1] - i))
                else:
                    if board.get_piece_at(present_position[0] + i,
                                          present_position[1] - i).player_color != board.player_turn:
                        list_possible_move.append((present_position[0] + i, present_position[1] - i))
                    self.direction["North"] = True

        return list_possible_move
