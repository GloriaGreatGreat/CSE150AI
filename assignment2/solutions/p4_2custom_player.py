# -*- coding: utf-8 -*-
__author__ = 'Sivasubramanian Chandrasegarampillai, Walter Curnow'
__email__ = 'rchandra@uci.edu,wcurnow@uci.edu'
import time
from assignment2 import Player, State, Action


class Your1(Player):
    @property
    def name(self):
        """Returns the name of this agent. Try to make it unique!"""
        return '2player'

    def move(self, state):
        """Calculates the absolute best move from the given board position using magic.
        
        Args:
            state (State): The current state of the board.

        Returns:
            your next Action instance
        """
        # my_move = None
        start_time = time.time()
        # while not self.is_time_up() and self.feel_like_thinking(start_time):
        #     # Do some thinking here
        #     my_move = self.do_the_magic(state)

        # # Time's up, return your move
        # # You should only do a small amount of work here, less than one second.
        # # Otherwise a random move will be played!
        # return my_move
        while self.feel_like_thinking(start_time):
            max_depth = state.M * state.N - sum([1 for row in state.board for cell in row if cell > 0])
            current_depth = 0
            return_state = None
            trans = {}
            while(current_depth <= max_depth and self.feel_like_thinking(start_time)):
                return_state = min_max(state, current_depth, trans)
                current_depth = current_depth + 1

        # Do the magic, return the first available move!
        return return_state

    def feel_like_thinking(self, start_time):
        if time.time() - start_time <= 3:
            return True
        return False

# implement iterative depping alpha beta + heuristic function at depth limit
# improve the heuristic function
# add move ordering based on the best moves from previous iteration 
# in iterative deepening
    def do_the_magic(self, state):
        max_depth = 25
        #max_depth = state.M * state.N - sum([1 for row in state.board for cell in row if cell > 0])
        current_depth = 0
        return_state = state
        
        while(current_depth <= max_depth):
            return_state = min_max(state, current_depth)
            current_depth = current_depth + 1

        # Do the magic, return the first available move!
        return return_state

def min_max(state, current_depth, trans):
    trans.clear()
    if current_depth == 0:
        if(state.is_terminal()):
            return state.utility(player)
        return evaluate(state, state.to_play.color, state.K)
    player = state.to_play
    state_list = state.actions()
    store = []
    a = float("-infinity")
    b = float("infinity")
    for i in range(0, len(state_list)):
        store.insert(i, min_value(state.result(state_list[i]),player, a, b, trans, 
            current_depth - 1))
    val = float("-infinity")
    for i in range(0, len(store)):
        if store[i] > val: 
            val = store[i]
            index = i
    return state_list[index]

def max_value(state, player,a,b,trans, current_depth):
        # if terminal test is true, return utility
        # val <- negative infinity
        # for each child in Action do
        #       val <- max(val, min_value(child, a, b))
        #       if val >= b then return val
        #       a <- max(a, val)
        # return val
    if current_depth == 0:
        if(state.is_terminal()): return state.utility(player)
        if state in trans: return trans[state]
        return evaluate(state, state.to_play.color,state.K)   
    if state in trans:
        return trans[state]
    if(state.is_terminal()):
        #print(state.utility(state.to_play))
        return state.utility(player)
    val_return = float("-infinity")
    action_list = state.actions()
    for i in range(0, len(action_list)):
        value = min_value(state.result(action_list[i]),player, a, b, trans,
            current_depth - 1)
        if value > val_return:
            val_return = value
        if val_return >= b: return val_return
        if val_return > a: a = val_return
        trans[state.result(action_list[i])] = val_return
    return val_return
def min_value(state, player,a,b,trans, current_depth):
        # if terminal test is true, return utility
        # val <- positive infinity
        # for each child in Action do
        #       val <- min(val, max_value(child))
        # return val
    if current_depth == 0:
        if(state.is_terminal()): return state.utility(player)
        if state in trans: return trans[state]
        return evaluate(state, state.to_play.color, state.K)   
    if state in trans:
        return trans[state]
    if(state.is_terminal()):
        #print(state.utility(state.to_play))
        return state.utility(player)
    val_return = float("infinity")
    action_list = state.actions()
    for i in range(0, len(action_list)):
        value = max_value(state.result(action_list[i]),player, a, b, trans,
            current_depth - 1)
        if(value < val_return):
            val_return = value
        if val_return <= a: return val_return
        if val_return < b: b = val_return
        trans[state.result(action_list[i])] = val_return
    return val_return

def evaluate(state, color,K):
    chase_list = []

    count = 0
    for i in range(0, len(state.board)):
        for j in range(0, len(state.board[0])):
            if state.board[i][j] == color:
                count = count + 1
                chase_list.append(chase(i, j, state, color,K))
    chase_list.sort()
    #print(chase_list[len(chase_list)-1])
    #print(state.K)
    if count == 0: return 0
    return round(chase_list[len(chase_list)-1],1)/ round(state.K, 1)

def chase(i, j, state, color,K):
    return_list = []
    #left, chase right
    if j == 0 or j > 0 and state.board[i][j-1] != color:
        count = 0
        jj = j
        while jj < len(state.board[0]) and state.board[i][jj] == color:
            count = count + 1
            jj = jj + 1
        if count == K: return K
        if jj < len(state.board[0]) and state.board[i][jj] == 0 : return_list.append(count)
        else : return_list.append(-1)
    #right, chase left
    if j == len(state.board[0]) - 1 or j < len(state.board[0]) - 1 and state.board[i][j+1] != color:
        count = 0
        jj = j
        while jj >= 0 and state.board[i][jj] == color:
            count = count + 1
            jj = jj - 1
        if count == K: return K
        if jj >=0 and state.board[i][jj] == 0 : return_list.append(count)
        else : return_list.append(-1)
    #up, chase down
    if i == 0 or i > 0 and state.board[i-1][j] != color:
        count = 0
        ii = i
        while ii < len(state.board) and state.board[ii][j] == color:
            count = count + 1
            ii = ii + 1
        if count == K: return K
        if ii < len(state.board) and state.board[ii][j] == 0 : return_list.append(count)
        else : return_list.append(-1)
    #down, chase up
    if i == len(state.board) - 1 or i < len(state.board) - 1 and state.board[i+1][j] != color:
        count = 0
        ii = i
        while ii >= 0 and state.board[ii][j] == color:
            count = count + 1
            ii = ii - 1
        if count == K: return K
        if ii >= 0 and state.board[ii][j] == 0 : return_list.append(count)
        else : return_list.append(-1)
    #left-up, chase right-down
    if i == 0 or j == 0 or i>0 and j>0 and state.board[i-1][j-1] != color:
        count = 0
        ii = i
        jj = j
        while jj < len(state.board[0]) and ii < len(state.board) and state.board[ii][jj] == color:
            count = count + 1
            ii = ii + 1
            jj = jj + 1
        if count == K: return K
        if jj < len(state.board[0]) and ii < len(state.board) and state.board[ii][jj] == 0 : return_list.append(count)
        else : return_list.append(-1)
    #right-down, chase left-up
    if j  == len(state.board[0]) - 1 or i == len(state.board) - 1 or j < len(state.board[0]) - 1 and i < len(state.board) - 1 and state.board[i+1][j+1] != color:
        count = 0
        ii = i
        jj = j
        while ii >= 0 and jj >= 0 and state.board[ii][jj] == color:
            count = count + 1
            ii = ii - 1
            jj = jj - 1
        if count == K: return K
        if ii >= 0 and jj >= 0 and state.board[ii][jj] == 0 : return_list.append(count)
        else : return_list.append(-1)
    #right-up, chase left-down
    if i == 0 or j == len(state.board[0]) - 1 or i>0 and j < len(state.board[0]) - 1 and state.board[i-1][j+1] != color:
        count = 0
        ii = i
        jj = j
        while jj >= 0 and ii < len(state.board) and state.board[ii][jj] == color:
            count = count + 1
            ii = ii + 1
            jj = jj - 1
        if count == K: return K
        if jj >= 0 and ii < len(state.board) and state.board[ii][jj] == 0 : return_list.append(count)
        else : return_list.append(-1)
    #left-down, chase right-up
    if j == 0 or i == len(state.board) - 1 or j>0 and i < len(state.board) - 1 and state.board[i+1][j-1] != color:
        count = 0
        ii = i
        jj = j
        while ii >= 0 and jj < len(state.board[0]) and state.board[ii][jj] == color:
            count = count + 1
            ii = ii - 1
            jj = jj + 1
        if count == K: return K
        if ii >= 0 and jj < len(state.board[0]) and state.board[ii][jj] == 0 : return_list.append(count)
        else : return_list.append(-1)
    if len(return_list) != 0: 
        return_list.sort()
        return return_list[len(return_list)-1]
    return 0

