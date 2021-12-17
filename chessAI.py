import random

PIECE_SCORE = {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "P": 1}
CHECKMATE = 1000  # Highest score.
STALEMATE = 0  # Better than losing, but not as good as checkmate.
DEPTH = 3   # How deep we want to go into the game moves.

def find_random_move(valid_moves):
    """Return a random move from the list of valid moves."""
    return random.choice(valid_moves)


#def find_best_move(gs, valid_moves):
    """Find the best move based only on material using a greedy approach."""
    """turn_multiplier = 1 if gs.white_to_move else -1
    opponent_min_max_score = CHECKMATE  # The minimum of all the maximum scores that the opponent has.
    best_player_move = None
    random.shuffle(valid_moves)
    for player_move in valid_moves:
        gs.make_move(player_move, promoted_pawn='Q')
        opponent_moves = gs.get_valid_moves()
        if gs.stalemate:
            opponent_max_score = STALEMATE
        elif gs.checkmate:
            opponent_max_score = -CHECKMATE
        else:
            opponent_max_score = -CHECKMATE
            for opponent_move in opponent_moves:
                gs.make_move(opponent_move, promoted_pawn='Q')
                gs.get_valid_moves()   # We need to generate all valid moves to see if there's a checkmate.
                if gs.checkmate:
                    score = CHECKMATE
                elif gs.stalemate:
                    score = STALEMATE
                else:
                    score = -turn_multiplier * score_material(gs.board)
                if score > opponent_max_score:
                    opponent_max_score = score
                gs.undo_move()
        if opponent_max_score < opponent_min_max_score:
            opponent_min_max_score = opponent_max_score
            best_player_move = player_move
        gs.undo_move()
    return best_player_move"""


def find_best_move(gs, valid_moves):
    """This function will make the first recursive call for the negamax algorithm."""
    global next_move
    next_move = None
    random.shuffle(valid_moves)
    find_move_nega_max_alpha_beta(gs, valid_moves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.white_to_move else -1)
    return next_move

#def find_move_min_max(gs, valid_moves, depth, white_to_move):
    """global next_move
    if depth == 0:
        return score_material(gs.board)
    
    if white_to_move:   # We want to maximize the score. 
        max_score = -CHECKMATE
        for move in valid_moves:
            gs.make_move(move)
            next_moves = gs.get_valid_moves()
            score = find_move_min_max(gs, next_moves, depth-1, False)
            if score > max_score:
                max_score = score
                if depth == DEPTH:
                    next_move = move
            gs.undo_move()
        return max_score

    else:   # We want to minimize the score.
        min_score = CHECKMATE
        for move in valid_moves:
            gs.make_move(move)
            next_moves = gs.get_valid_moves()
            score = find_move_min_max(gs, next_moves, depth-1, True)
            if score < min_score:
                min_score = score
                if depth == DEPTH:
                    next_move = move
            gs.undo_move()
        return min_score"""


#def find_move_nega_max(gs, valid_moves, depth, turn_multiplier):
    """We will look for max score, then multipli it by -1 when it's black's turn."""
    """global next_move
    if depth == 0:
        return turn_multiplier * score_board(gs)
    max_score = -CHECKMATE
    for move in valid_moves:
        gs.make_move(move)
        next_moves = gs.get_valid_moves()
        score = -find_move_nega_max(gs, next_moves, depth-1, -turn_multiplier)   # Will negate opponent's max score.
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move
        gs.undo_move()
    return max_score"""


def find_move_nega_max_alpha_beta(gs, valid_moves, depth, alpha, beta, turn_multiplier):
    """We will look for max score, then multipli it by -1 when it's black's turn."""
    global next_move
    if depth == 0:
        return turn_multiplier * score_board(gs)
    
    # move ordering - implement late.

    max_score = -CHECKMATE
    for move in valid_moves:
        gs.make_move(move)
        next_moves = gs.get_valid_moves()
        score = -find_move_nega_max_alpha_beta(gs, next_moves, depth-1, -beta, -alpha,  -turn_multiplier)   # Will negate opponent's max score.
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move
        gs.undo_move()
        if max_score > alpha:   # Pruning. Neglecting unnecessary position calculations.
            alpha = max_score
        if alpha >= beta:   # We reached the best possible score. no need to calculate further more.
            break
    return max_score


    
def score_board(gs):
    """Positive score is better for white while negative score is better for black."""
    if gs.checkmate:
        if gs.white_to_move:
            return -CHECKMATE   # Black wins.
        else:
            return CHECKMATE   # White wins.
    elif gs.stalemate:
        return STALEMATE

    score = 0
    for row in gs.board:
        for square in row:
            if square[0] == 'w':
                # For white to win the score need to be a positive value.
                # Meaning that white is trying to maximize the score.
                score += PIECE_SCORE[square[1]]
            elif square[0] == 'b':
                # Black is trying to minimize the score.
                score -= PIECE_SCORE[square[1]]
    return score

#def score_material(board):
    """Score the board based on material alone not considering the position."""
    """score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                # For white to win the score need to be a positive value.
                # Meaning that white is trying to maximize the score.
                score += PIECE_SCORE[square[1]]
            elif square[0] == 'b':
                # Black is trying to minimize the score.
                score -= PIECE_SCORE[square[1]]
    return score"""
