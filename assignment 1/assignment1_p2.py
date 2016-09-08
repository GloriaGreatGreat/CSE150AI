# import heapq

# class PriorityQueue(object):
# 	def __init__(self):
# 		self.heap = []
# 		self.count = 0
# 		self.max_length = 0

# 	def insert(self, item, priority):
# 		heapq.heappush(self.heap, (priority, self.count, item))
# 		self.count += 1
# 		self.max_length = max(self.max_length, len(self))

__author__ = 'yul200@ucsd.edu'

import copy

# print True if the inital board is solved; or False if not solved
def is_solved(board):
	if board[0][0] != 0:
		return False
	else:
		for i in range(len(board)):
			for j in range(len(board[i])):
				if j == len(board[0]) - 1:
					if i < len(board)-1:
						if board[i][j] > board[i+1][0]:
							return False
				elif j < len(board[0]) - 1:
					if board [i][j] > board [i][j+1]:
						return False
	return True

class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop(len(self.items)-1)

	def empty(self):
		return self.items == []

# define a Node class as a single element for every changed board
class Node(object):
	def __init__(self, x, y, board, steps, instr, s, level):
		self.x = x
		self.y = y
		self.board = board
		self.steps = steps
		self.instr = instr
		self.s = s
		self.level = level
	# def __eq__(self, other):
	# 	return self.board == other.board
	# def __hash__(self):
	# 	return hash(str(self.board))

	def get_x(self):
		return self.x
	def get_y(self):
		return self.y
	def get_steps(self):
		return self.steps
	def get_instr(self):
		return self.instr
	def get_board(self):
		return self.board
	def get_s(self):
		return self.s
	def get_level(self):
		return self.level

def make_Node(x, y, board, steps, instr, s, level):
	node = Node(x, y, copy.deepcopy(board), copy.deepcopy(steps), instr, s, level)
	return node

# new function for insert legal positions into stack
def check_position(current):
	#print("position", x ,y)
	x = current.get_x()
	y = current.get_y()
	# visited[y][x] = True
	steps = current.get_steps()
	instr = current.get_instr()
	board = current.get_board()
	level = current.get_level()
	s = current.get_s()

	if level < 5:
		if y != 0:
			if len(steps) == 0:
				s.push(make_Node(x, y, board, steps, 'U', s, level+1))
			elif steps[-1] != 'D': 
			#print("U")
				s.push(make_Node(x, y, board, steps, 'U', s, level+1))		
		if y != len(board) - 1:
			#print("D")
			if len(steps) == 0:
				s.push(make_Node(x, y, board, steps, 'D', s, level+1))
			elif steps[-1] != 'U': 
			#print("U")
				s.push(make_Node(x, y, board, steps, 'D', s, level+1))	
		if x != 0: 
			if len(steps) == 0:
				s.push(make_Node(x, y, board, steps, 'L', s, level+1))
			elif steps[-1] != 'R': 
			#print("U")
				s.push(make_Node(x, y, board, steps, 'L', s, level+1))	
		if x != len(board[0]) - 1:
			#print("R")
			if len(steps) == 0:
				s.push(make_Node(x, y, board, steps, 'R', s, level+1))
			elif steps[-1] != 'L': 
			#print("U")
				s.push(make_Node(x, y, board, steps, 'R', s, level+1))	
# implement problem 3
# print steps, UP for "U", DOWN for "D", LEFT for "L", RIGHT for "R"
# if it is not solvable, print UNSOLVABLE, or solvable more than 5 steps
def can_solved(board):
	# search the location of zero
	# corner case: there is no zero on the board
	if is_solved(board):
		return "ALREADY_SOLVED"
	# initial x and y
	for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 0:
					ini_x = j
					ini_y = i
	# initialize a list recording steps made
	steps = list();
	# initial a queue to store Nodes
	s = Stack()
	# initial a set to store the board conditions
	# visited  =  set()
	# initial the root
	root = make_Node(ini_x, ini_y, board, steps, None, s, 0)

	check_position(root)

	# visited.add(root)
	# start to insert into queue
	
	while s.empty() == False:
		#print(board)
		# get the next node
		current = s.pop()
		# get all the elements
		x = current.get_x()
		y = current.get_y()
		# visited[y][x] = True
		steps = current.get_steps()
		instr = current.get_instr()
		board = current.get_board()
		level = current.get_level()

		#print(board)
		if instr == 'U':
			board[y][x] = board[y-1][x]
			y = y-1
			#print(y-1)
			#print(x)
			#print(board[y-1][x])
			steps.append('U')
		elif instr == 'D':
			board[y][x] = board[y+1][x]
			y = y+1
			steps.append('D')
		elif instr == 'L':
			board[y][x] = board[y][x-1]
			x = x-1
			steps.append('L')
		elif instr == 'R':
			board[y][x] = board[y][x+1]
			x = x+1
			steps.append('R')
		board[y][x] = 0

		next = make_Node(x, y, board, steps, None, s, level)

		# if next not in visited:
		# 	visited.add(next)
		if is_solved(board):
			return ''.join(steps)
		# check after move, if the board is solved
		else:
			check_position(next)
	# no more nodes in queue
	return "UNSOLVABLE"


def main():
	import sys
	# transfer input into 2D-array
	board = [[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
	print(can_solved(board))

if __name__ == '__main__':
	main()