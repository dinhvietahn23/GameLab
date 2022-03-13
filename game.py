import pygame as pg
from board import Board
# import sockets.network as network
import smart_move
import math

WIDTH = HEIGHT = 512
COLS = ROWS = 8
SQ_SIZE = 512 // 8


class Game:

    def __init__(self):
        self.board = Board()
        self.board_second = Board()

        self.player = "white"
        self.piece_choose = None

    def set_piece_choose(self, piece):
        self.piece_choose = piece

    def draw_game_state(self, screen, list_pieces):
        self.draw_board(screen)
        self.draw_pieces(screen, list_pieces)

    def draw_board(self, screen):
        colors = [pg.Color("white"), pg.Color("grey")]
        for i in range(ROWS):
            for j in range(COLS):
                color = colors[(i + j) % 2]
                pg.draw.rect(screen, color, pg.Rect(i * SQ_SIZE, j * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def draw_pieces(self, screen, list_pieces):
        for piece in list_pieces:
            screen.blit(piece.draw_piece(),
                        pg.Rect(piece.coordinates_y * SQ_SIZE, piece.coordinates_x * SQ_SIZE,
                                SQ_SIZE, SQ_SIZE))

    def draw_border_selected_piece(self, screen, x, y):
        pg.draw.rect(screen, pg.Color("yellow"), pg.Rect(x * SQ_SIZE, y * SQ_SIZE, SQ_SIZE, SQ_SIZE), 2)

    def draw_list_possible_move(self, screen, piece):
        list_move = piece.can_move(self.board)
        for move in list_move:
            pg.draw.rect(screen, pg.Color("red"), pg.Rect(move[1] * SQ_SIZE, move[0] * SQ_SIZE, SQ_SIZE, SQ_SIZE), 2)

    def start(self):
        SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
        SCREEN.fill("white")

        running = True
        pg.init()

        player_clicks = []
        selected_piece = None

        # n = network.Network()
        # p = n.getP()
        #  print(p)

        while running:
            # game = n.send("s")
            # self.board = game.board
            if self.board.player_turn == "b":
                best_move = smart_move.minimax(self.board, 3, -math.inf, math.inf, True, "b")
                print(best_move[0][0].get_information())
                print(best_move[0][1][0], best_move[0][1][1])
                self.board.move_piece_to(best_move[0][0],  best_move[0][1][0], best_move[0][1][1])

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    running = False
                elif e.type == pg.MOUSEBUTTONDOWN:
                    position = pg.mouse.get_pos()
                    x = position[0] // SQ_SIZE
                    y = position[1] // SQ_SIZE

                    if not player_clicks:
                        selected_piece = self.board.get_piece_at(y, x)
                        if selected_piece is not None:
                            player_clicks.append((x, y))
                    else:
                        if self.board.get_piece_at(y, x) is not None and \
                                self.board.get_piece_at(y, x).player_color == self.board.player_turn:
                            selected_piece = self.board.get_piece_at(y, x)
                            player_clicks.clear()
                            player_clicks.append((x, y))
                        elif player_clicks[0] != (x, y) and selected_piece is not None:
                            if (y, x) in selected_piece.can_move(self.board):
                                posCurrent = (selected_piece.coordinates_y, selected_piece.coordinates_x)
                                self.board.move_piece_to(selected_piece, y, x)
                                # posCurrent_ = (y,x)
                                # msg = str(posCurrent[0])+","+str(posCurrent[1])+","+str(posCurrent_[0])+","+str(posCurrent_[1])
                                # print(msg)
                                selected_piece = None
                                # self.board=n.send(msg).board
                                player_clicks.clear()
                elif e.type == pg.KEYDOWN:
                    if e.key == pg.K_z:
                        self.board.undo_move()

            self.draw_game_state(SCREEN, self.board.list_pieces)
            if selected_piece is not None:
                self.draw_border_selected_piece(SCREEN, selected_piece.coordinates_y, selected_piece.coordinates_x)
                if selected_piece.player_color == self.board.player_turn:
                    self.draw_list_possible_move(SCREEN, selected_piece)

            pg.display.flip()
