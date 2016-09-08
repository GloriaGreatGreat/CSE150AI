# -*- coding: utf-8 -*-
__author__ = 'Sivasubramanian Chandrasegarampillai, Walter Curnow'
__email__ = 'rchandra@uci.edu,wcurnow@uci.edu'

import heapq

from assignment2 import Player


class EvaluationPlayer(Player):
    def move(self, state):
        """Calculates the best move after 1-ply look-ahead with a simple evaluation function.

        Args:
            state (State): The current state of the board.

        Returns:
            the next move (Action)
        """

        # *You do not need to modify this method.*
        best_move = None
        max_value = -1.0
        my_color = state.to_play.color

        for action in state.actions():
            if self.is_time_up():
                break

            result_state = state.result(action)
            value = self.evaluate(result_state, my_color)
            if value > max_value:
                max_value = value
                best_move = action

        # Return the move with the highest evaluation value
        return best_move

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
        """Evaluates the state for the player with the given stone color.

        This function calculates the length of the longest ``streak'' on the board
        (of the given stone color) divided by K.  Since the longest streak you can
        achieve is K, the value returned will be in range [1 / state.K, 1.0].

        Args:
            state (State): The state instance for the current board.
            color (int): The color of the stone for which to calculate the streaks.

        Returns:
            the evaluation value (float), from 1.0 / state.K (worst) to 1.0 (win).
        """

        # TODO implement this
        #return 0.0
