import math


def evaluate(board, max_color):
    if max_color == "w":
        return board.get_white_score() - board.get_black_score()
    return board.get_black_score() - board.get_white_score()


def minimax(board, depth, alpha, beta, max_player, max_color):
    if depth == 0:
        return None, evaluate(board, max_color)
    moves = board.get_all_possible_move()
    best_move = moves[0]

    if max_player:
        max_eval = - math.inf
        for move in moves:
            if move[0].player_color != max_color:
                continue
            board.move_piece_to(move[0], move[1][0], move[1][1])
            current_val = minimax(board, depth - 1, alpha, beta, False, max_color)[1]
            board.undo_move()
            if current_val > max_eval:
                max_eval = current_val
                best_move = move
            alpha = max(current_val, alpha)
            if beta <= alpha:
                break
        return best_move, max_eval

    else:
        min_eval = math.inf
        for move in moves:
            if move[0].player_color == max_color:
                continue
            board.move_piece_to(move[0], move[1][0], move[1][1])
            current_val = minimax(board, depth - 1, alpha, beta, True, max_color)[1]
            board.undo_move()
            if current_val < min_eval:
                min_eval = current_val
                best_move = move
            beta = min(current_val, beta)
            if beta <= alpha:
                break
        return best_move, min_eval
