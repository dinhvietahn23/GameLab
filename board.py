import pieces.king
import pieces.bishop
import pieces.pawn
import pieces.rook
import pieces.knight
import pieces.queen


class Move:
    def __init__(self, start_x, start_y, end_x, end_y, piece_move, piece_remove):
        self.piece_move = piece_move
        self.piece_remove = piece_remove
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y


class Board:
    def __init__(self):
        self.board_game = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.list_pieces = ()
        self.add_pieces()
        self.player_turn = 'w'
        self.flag_check = True
        self.move_history = []
        self.weight_piece = {
            "P": 10,
            "R": 50,
            "N": 30,
            "B": 30,
            "Q": 100,
            "K": 900
        }

    def add_pieces(self):
        for i in range(8):
            for j in range(8):
                symbol = self.board_game[i][j]
                if symbol == "--":
                    continue
                if symbol[1] == "R":
                    self.list_pieces = self.list_pieces + (pieces.rook.Rook(i, j, symbol[0]),)
                elif symbol[1] == "N":
                    self.list_pieces = self.list_pieces + (pieces.knight.Knight(i, j, symbol[0]),)
                elif symbol[1] == "B":
                    self.list_pieces = self.list_pieces + (pieces.bishop.Bishop(i, j, symbol[0]),)
                elif symbol[1] == "Q":
                    self.list_pieces = self.list_pieces + (pieces.queen.Queen(i, j, symbol[0]),)
                elif symbol[1] == "K":
                    self.list_pieces = self.list_pieces + (pieces.king.King(i, j, symbol[0]),)
                elif symbol[1] == "P":
                    self.list_pieces = self.list_pieces + (pieces.pawn.Pawn(i, j, symbol[0]),)

    def get_piece_at(self, x, y):
        if self.valid_position(x, y) is False:
            return None
        for p in self.list_pieces:
            if p.coordinates_x == x and p.coordinates_y == y:
                return p
        return None

    def valid_position(self, x, y):
        return True if 0 <= x <= 7 and 0 <= y <= 7 else False

    def remove_piece_at(self, x, y):
        tuple_to_list = list(self.list_pieces)
        tuple_to_list.remove(self.get_piece_at(x, y))
        self.list_pieces = tuple(tuple_to_list)

    def move_piece_to(self, piece, x, y):
        # if piece.player_color == self.player_turn:
        piece_remove = None
        if self.get_piece_at(x, y) is not None:
            piece_remove = self.get_piece_at(x, y)
            self.remove_piece_at(x, y)
        self.move_history.append((Move(piece.coordinates_x, piece.coordinates_y, x, y, piece, piece_remove)))
        if isinstance(piece, pieces.king.King):
            if piece.is_first_move:
                if y == 6:
                    p = self.get_piece_at(x, y + 1)
                    p.coordinates_y = y - 1
                elif y == 2:
                    p = self.get_piece_at(x, y - 2)
                    p.coordinates_y = y + 1
        elif isinstance(piece, pieces.pawn.Pawn):
            if x - piece.init_coordinates_x == 6 or x - piece.init_coordinates_x == -6:
                self.remove_piece_at(piece.coordinates_x, piece.coordinates_y)
                self.list_pieces = self.list_pieces + (pieces.queen.Queen(x, y, self.player_turn),)

        piece.coordinates_y = y
        piece.coordinates_x = x
        if piece.is_first_move is True:
            piece.is_first_move = False
        self.switch_turn()

    def switch_turn(self):
        self.player_turn = "b" if self.player_turn == "w" else "w"

    def print_position_all_piece(self):
        for p in self.list_pieces:
            print(p.get_information())

    def undo_move(self):
        if len(self.move_history) != 0:
            move = self.move_history.pop()
            piece_move = move.piece_move
            piece_remove = move.piece_remove
            if isinstance(piece_move, pieces.pawn.Pawn):
                piece_move.is_first_move = True if (piece_move.player_color == "w" and move.start_x == 6) \
                                                   or (piece_move.player_color == "b" and move.start_x == 1) else False
            if piece_remove is not None:
                self.list_pieces = self.list_pieces + (piece_remove,)
            piece_move.coordinates_y = move.start_y
            piece_move.coordinates_x = move.start_x
            self.switch_turn()

    def get_all_possible_move_of(self, player_turn):
        score = 0
        list_possible_move = []
        for p in self.list_pieces:
            if p.player_color != player_turn:
                continue
            list_possible_move.extend(p.can_move(self))
            score += self.weight_piece[p.name]
        return list_possible_move, score

    def get_all_possible_move(self):
        list_possible_move = []
        for p in self.list_pieces:
            list_move = p.can_move(self)
            for move in list_move:
                if move[0] < 0 or move[1] < 0:
                    continue
                list_possible_move.append((p, move))
        return list_possible_move

    def get_white_score(self):
        return self.get_all_possible_move_of("w")[1]

    def get_black_score(self):
        return self.get_all_possible_move_of("b")[1]
