# -*- coding: utf-8 -*-
__author__ = 'Sivasubramanian Chandrasegarampillai, Walter Curnow'
__email__ = 'rchandra@uci.edu,wcurnow@uci.edu'
import time
from assignment2 import Player, State, Action

# Yujia Li A98064697
# Ze Li A11628864
# Wei Wang A97031723

__author__ = 'yul200@ucsd.edu, zel014@ucsd.edu, wew026@ucsd.edu'

class YourCustomPlayer(Player):
    @property
    def name(self):
        """Returns the name of this agent. Try to make it unique!"""
        return 'whatever'

    def move(self, state):
        """Calculates the absolute best move from the given board position using magic.
        
        Args:
            state (State): The current state of the board.

        Returns:
            your next Action instance
        """
        max_depth = state.M * state.N - sum([1 for row in state.board for cell in row if cell > 0])
        current_depth = 0
        return_state = None
        trans = {}
        while(current_depth <= max_depth):
            return_state = self.min_max(state, current_depth, trans)
            current_depth = current_depth + 1
        return return_state

    def feel_like_thinking(self, start_time):
        if time.time() - start_time <= 1:
            return True
        return False

    # implement iterative depping alpha beta + heuristic function at depth limit
    # improve the heuristic function
    # add move ordering based on the best moves from previous iteration 
    # in iterative deepening
    def do_the_magic(self, state):
        """we did not use this function at this time"""

    def min_max(self, state, current_depth, trans):
        trans.clear()
        if current_depth == 0:
            if(state.is_terminal()):
                return state.utility(player)
            return self.evaluate(state, state.to_play.color)
        player = state.to_play
        state_list = state.actions()
        store = []
        a = float("-infinity")
        b = float("infinity")
        for i in range(0, len(state_list)):
            store.insert(i, self.min_value(state.result(state_list[i]),player, a, b, trans, 
                current_depth - 1))
        val = float("-infinity")
        for i in range(0, len(store)):
            if store[i] > val: 
                val = store[i]
                index = i
        return state_list[index]

    def max_value(self, state, player,a,b,trans, current_depth):
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
            return self.evaluate(state, state.to_play.color)   
        if state in trans:
            return trans[state]
        if(state.is_terminal()):
            return state.utility(player)
        val_return = float("-infinity")
        action_list = state.actions()
        for i in range(0, len(action_list)):
            value = self.min_value(state.result(action_list[i]),player, a, b, trans,
                current_depth - 1)
            if value > val_return:
                val_return = value
            if val_return >= b: return val_return
            if val_return > a: a = val_return
            trans[state.result(action_list[i])] = val_return
        return val_return
    def min_value(self, state, player,a,b,trans, current_depth):
            # if terminal test is true, return utility
            # val <- positive infinity
            # for each child in Action do
            #       val <- min(val, max_value(child))
            # return val
        if current_depth == 0:
            if(state.is_terminal()): return state.utility(player)
            if state in trans: return trans[state]
            return self.evaluate(state, state.to_play.color)   
        if state in trans:
            return trans[state]
        if(state.is_terminal()):
            return state.utility(player)
        val_return = float("infinity")
        action_list = state.actions()
        for i in range(0, len(action_list)):
            value = self.max_value(state.result(action_list[i]),player, a, b, trans,
                current_depth - 1)
            if(value < val_return):
                val_return = value
            if val_return <= a: return val_return
            if val_return < b: b = val_return
            trans[state.result(action_list[i])] = val_return
        return val_return

    def evaluate(self, state, color):
        chase_list = []
        for i in range(0, len(state.board)):
            for j in range(0, len(state.board[0])):
                if state.board[i][j] == color:
                    chase_list.append(self.chase(i, j, state, color))
        chase_list.sort()
        #print(chase_list[len(chase_list)-1])
        #print(state.K)
        return round(chase_list[len(chase_list)-1],1)/ round(state.K, 1)

    def chase(self, i, j, state, color):
        return_list = []
        #left, chase right
        if j == 0 or j > 0 and state.board[i][j-1] != color:
            count = 0
            jj = j
            while jj < len(state.board[0]) and state.board[i][jj] == color:
                count = count + 1
                jj = jj + 1
            return_list.append(count)
        #right, chase left
        if j == len(state.board[0]) - 1 or j < len(state.board[0]) - 1 and state.board[i][j+1] != color:
            count = 0
            jj = j
            while jj >= 0 and state.board[i][jj] == color:
                count = count + 1
                jj = jj - 1
            return_list.append(count)
        #up, chase down
        if i == 0 or i > 0 and state.board[i-1][j] != color:
            count = 0
            ii = i
            while ii < len(state.board) and state.board[ii][j] == color:
                count = count + 1
                ii = ii + 1
            return_list.append(count)
        #down, chase up
        if i == len(state.board) - 1 or i < len(state.board) - 1 and state.board[i+1][j] != color:
            count = 0
            ii = i
            while ii >= 0 and state.board[ii][j] == color:
                count = count + 1
                ii = ii - 1
            return_list.append(count)
        #left-up, chase right-down
        if i == 0 or j == 0 or i>0 and j>0 and state.board[i-1][j-1] != color:
            count = 0
            ii = i
            jj = j
            while jj < len(state.board[0]) and ii < len(state.board) and state.board[ii][jj] == color:
                count = count + 1
                ii = ii + 1
                jj = jj + 1
            return_list.append(count) 
        #right-down, chase left-up
        if j  == len(state.board[0]) - 1 or i == len(state.board) - 1 or j < len(state.board[0]) - 1 and i < len(state.board) - 1 and state.board[i+1][j+1] != color:
            count = 0
            ii = i
            jj = j
            while ii >= 0 and jj >= 0 and state.board[ii][jj] == color:
                count = count + 1
                ii = ii - 1
                jj = jj - 1
            return_list.append(count)
        #right-up, chase left-down
        if i == 0 or j == len(state.board[0]) - 1 or i>0 and j < len(state.board[0]) - 1 and state.board[i-1][j+1] != color:
            count = 0
            ii = i
            jj = j
            while jj >= 0 and ii < len(state.board) and state.board[ii][jj] == color:
                count = count + 1
                ii = ii + 1
                jj = jj - 1
            return_list.append(count)
        #left-down, chase right-up
        if j == 0 or i == len(state.board) - 1 or j>0 and i < len(state.board) - 1 and state.board[i+1][j-1] != color:
            count = 0
            ii = i
            jj = j
            while ii >= 0 and jj < len(state.board[0]) and state.board[ii][jj] == color:
                count = count + 1
                ii = ii - 1
                jj = jj + 1
            return_list.append(count)
        return_list.sort()
        return return_list[len(return_list)-1]

