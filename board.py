import pieces.king
import pieces.bishop
import pieces.pawn
import pieces.rook
import pieces.knight
import pieces.queen


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
        if piece.player_color == self.player_turn:
            if self.get_piece_at(x, y) is not None:
                self.remove_piece_at(x, y)

            if isinstance(piece, pieces.king.King):
                print(x, y)
                if piece.is_first_move:
                    if y == 6:
                        p = self.get_piece_at(x, y + 1)
                        p.coordinates_y = y - 1
                    elif y == 2:
                        p = self.get_piece_at(x, y - 2)
                        p.coordinates_y = y + 1

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
