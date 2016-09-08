# -*- coding: utf-8 -*-
__author__ = 'Sivasubramanian Chandrasegarampillai, Walter Curnow'
__email__ = 'rchandra@uci.edu,wcurnow@uci.edu'

# Yujia Li A98064697
# Ze Li A11628864
# Wei Wang A97031723

__author__ = 'yul200@ucsd.edu, zel014@ucsd.edu, wew026@ucsd.edu'

from assignment2 import Player, State, Action

class MinimaxPlayer(Player):
    def move(self, state):
        """Calculates the best move from the given board using the minimax algorithm.

        Args:
            state (State): The current state of the board.

        Returns:
            the next move (Action)
        """
        player = state.to_play
        state_list = state.actions()
        store = []
        for i in range(0, len(state_list)):
        	store.insert(i, self.min_value(state.result(state_list[i]),player))
        val = float("-infinity")
        for i in range(0, len(store)):
        	if store[i] > val: 
        		val = store[i]
        		index = i
        return state_list[index]

    def max_value(self,state, player):
        	# if terminal test is true, return utility
        	# val <- negative infinity
        	# for each child in Action do
        	# 		val <- max(val, min_value(child))
        	# return val
        if(state.is_terminal()):
        	return state.utility(player)
        val_return = float("-infinity")
        action_list = state.actions()
        for i in range(0, len(action_list)):
        	value = self.min_value(state.result(action_list[i]),player)
        	if value > val_return:
        		val_return = value
        return val_return
    def min_value(self,state, player):
        	# if terminal test is true, return utility
        	# val <- positive infinity
        	# for each child in Action do
        	# 		val <- min(val, max_value(child))
        	# return val
        if(state.is_terminal()):
        	#print(state.utility(state.to_play))
        	return state.utility(player)
        val_return = float("infinity")
        action_list = state.actions()
        for i in range(0, len(action_list)):
        	value = self.max_value(state.result(action_list[i]),player)
        	if(value < val_return):
        		val_return = value
        return val_return
