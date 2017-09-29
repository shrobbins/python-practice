"""
Monte Carlo Tic-Tac-Toe Player - Sue
"""
#http://www.codeskulptor.org/#user43_8tdBp11oQI_18.py

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 200    # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    """
    Function to produce moves for machine player
    """
    while board.check_win() == None:
        empty_squares = []
        empty_squares = board.get_empty_squares()
        choose_square = random.choice(empty_squares)
        board.move(choose_square[0], choose_square[1], player)
        player = provided.switch_player(player)        


def mc_update_scores(scores, board, player):
    """
    Function to update scores
    """
    if board.check_win() == provided.PLAYERX:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == provided.PLAYERX:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == provided.PLAYERO:
                    scores[row][col] -= SCORE_OTHER
    if board.check_win() == provided.PLAYERO:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == provided.PLAYERO:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == provided.PLAYERX:
                    scores[row][col] -= SCORE_OTHER               
    

def get_best_move(board, scores):
    """
    Function to get best move for machine
    """
    max_value = 0
    blank_values = []
    blank_squares = []
    blank_squares = board.get_empty_squares()
    for index1, index2 in blank_squares:
        blank_values.append(scores[index1][index2]) 
    max_value = max(blank_values)
        
             
    return find_value(blank_values, blank_squares, max_value)   
                  


def find_value(score_list, tuple_list, max_amount ): 
    """
    Function to find value for tuple
    """
    bm_tuples = []
    for index, val in enumerate(score_list):
             for num, tup in enumerate(tuple_list):
                if index == num and val == max_amount:
                    bm_tuples.append(tup)
    if len(bm_tuples)  >  0:
        tuple_select = random.choice(bm_tuples)
    else: 
        tuple_select = bm_tuples[0]
    return tuple_select



def mc_move(board, player, trials):
    """
    Function to work out best move for machine
    """
    score_board = [[0 for dummy_row in range(board.get_dim())]
                           for dummy_col in range(board.get_dim())] 

    for dummy_item in range(NTRIALS):
        trial_board = board.clone()
        mc_trial(trial_board,player)
        mc_update_scores(score_board,trial_board,player)
        
    
    return get_best_move(board, score_board)
    

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, mc_move, NTRIALS, False)