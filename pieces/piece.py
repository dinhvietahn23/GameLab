import pygame as pg


class Piece:
    def __init__(self, coordinates_x, coordinates_y, player_color):
        self.coordinates_x = coordinates_x
        self.coordinates_y = coordinates_y
        self.player_color = player_color
        self.name = ""
        self.is_first_move = True
        self.have_moved = False


    def get_information(self):
        return f"Piece: {self.player_color}{self.name} - pos: ({self.coordinates_x}, {self.coordinates_y}) "

    def draw_piece(self):
        return pg.transform.scale(pg.image.load("images/" + self.player_color + self.name + ".png"), (64, 64))

    def can_move(self, board):
        return True
