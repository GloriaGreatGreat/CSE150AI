# Yujia Li A98064697
# Ze Li A11628864
# Wei Wang A97031723

__author__ = 'yul200@ucsd.edu, zel014@ucsd.edu, wew026@ucsd.edu'

import copy
import heapq
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
# define a class priority queue to implement data structure
class PriorityQueue(object):
	def __init__(self):
		self.heap = []
		self.count = 0

	def insert(self, item, priority):
		heapq.heappush(self.heap, (priority, self.count, item))
		self.count += 1
		
	def get(self):
		(_,_, current) = heapq.heappop(self.heap)
		return current

	def empty(self):
		return (len(self.heap)) == 0

# define a Node class as a single element for every changed board
class Node(object):
	def __init__(self, x, y, board, steps, instr, q):
		self.x = x
		self.y = y
		self.board = board
		self.steps = steps
		self.instr = instr
		self.q = q

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
	def get_q(self):
		return self.q

	def __eq__(self, other):
		return self.board == other.board
	def __hash__(self):
		return hash(str(self.board))

def make_Node(x, y, board, steps, instr, q):
	node = Node(x, y, copy.deepcopy(board), copy.deepcopy(steps), instr, q)
	return node

# new function for insert legal positions into queue
def check_position(current):
	x = current.get_x()
	y = current.get_y()
	steps = current.get_steps()
	instr = current.get_instr()
	board = current.get_board()
	q = current.get_q()
	if y != 0 : 
		if len(steps) == 0 or len(steps) != 0 and steps[-1] != 'D':
			q.insert(make_Node(x, y, board, steps, 'U', q), x+y-1+len(steps))	
	if y != len(board) - 1:
		if len(steps) == 0 or len(steps) != 0 and steps[-1] != 'U':
			q.insert(make_Node(x, y, board, steps, 'D', q), x+y+1+len(steps))	
	if x != 0:
		if len(steps) == 0 or len(steps) != 0 and steps[-1] != 'R':
			q.insert(make_Node(x, y, board, steps, 'L', q), x+y-1+len(steps))
	if x != len(board[0]) - 1:
		if len(steps) == 0 or len(steps) != 0 and steps[-1] != 'L':
			q.insert(make_Node(x, y, board, steps, 'R', q), x+y+1+len(steps))

# implement problem 5
# print steps, UP for "U", DOWN for "D", LEFT for "L", RIGHT for "R"
# if it is not solvable, print UNSOLVABLE
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
	q = PriorityQueue()
	# initial a set to store the board conditions
	visited  =  set()
	# initial the root
	root = make_Node(ini_x, ini_y, board, steps, None, q)
	check_position(root)
	visited.add(root)
	# start to insert into queue
	while q.empty() == False:
		# get the next node
		current = q.get()
		# get all the elements
		x = current.get_x()
		y = current.get_y()
		steps = current.get_steps()
		instr = current.get_instr()
		board = current.get_board()
		if instr == 'U':
			board[y][x] = board[y-1][x]
			y = y-1
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
		next = make_Node(x, y, board, steps, None, q)
		if is_solved(board):
			return ''.join(steps)
		# check after move, if the board is solved
		elif next not in visited:
			visited.add(next)
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