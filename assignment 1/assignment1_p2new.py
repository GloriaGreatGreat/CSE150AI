# Yujia Li A98064697
# Ze Li A11628864
# Wei Wang A97031723

__author__ = 'yul200@ucsd.edu, zel014@ucsd.edu, wew026@ucsd.edu'

#import Queue
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

# define a Node class as a single element for every changed board
class Node(object):
	def __init__(self, x, y, board, steps, instr, q):
		self.x = x
		self.y = y
		self.board = board
		self.steps = steps
		self.instr = instr
		self.q = q
	def __eq__(self, other):
		return self.board == other.board
	def __hash__(self):
		return hash(str(self.board))

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
def make_Node(x, y, board, steps, instr,q):
	node = Node(x, y, board, steps, instr, q)
	return node

# implement problem 2 
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
	q = []
	# initial a set to store the board conditions
	visited  =  set()
	# initial the root
	root = make_Node(ini_x, ini_y, board, steps, None, q)
	check_position(root, visited)
	visited.add(root)
	# start to insert into queue
	while len(q) != 0:
		current = q.pop(0)
		# get all the elements
		x = current.get_x()
		y = current.get_y()
		steps = current.get_steps()
		board = current.get_board()
		next = make_Node(x, y, board, steps, None, q)

		if is_solved(board):
			#print(hehe)
			return ''.join(steps)
		# check after move, if the board is solved
		else:
			check_position(next, visited)
	# no more nodes in queue
	return "UNSOLVABLE"

# new function for insert legal positions into queue
def check_position(current, visited):
	#print("position", x ,y)
	x = current.get_x()
	y = current.get_y()
	steps = current.get_steps()
	instr = current.get_instr()
	board = current.get_board()
	q = current.get_q()

	if y != 0 : 
		board_checko = copy.deepcopy(board)
		board_checko[y][x] = board[y-1][x]
		yo = y-1
		board_checko[y-1][x] = 0
		step_checko = copy.deepcopy(steps)
		step_checko.append('U')
		n1 = make_Node(x, yo, board_checko, step_checko, 'U', q)
		if n1 not in visited:
			visited.add(n1)
			q.append(n1)		
	if y != len(board) - 1:
		board_checkt = copy.deepcopy(board)
		board_checkt[y][x] = board[y+1][x]
		yt = y+1
		board_checkt[y+1][x] = 0
		step_checkt = copy.deepcopy(steps)
		step_checkt.append('D')
		n2 = make_Node(x, yt, board_checkt, step_checkt, 'D', q)
		if n2 not in visited:
			visited.add(n2)
			q.append(n2)	
	if x != 0: 
		board_checks = copy.deepcopy(board)
		board_checks[y][x] = board[y][x-1]
		xt = x-1
		board_checks[y][x-1] = 0
		step_checks = copy.deepcopy(steps)
		step_checks.append('L')
		n3 = make_Node(xt, y, board_checks, step_checks, 'L', q)
		if n3 not in visited:
			visited.add(n3)
			q.append(n3)	
	if x != len(board[0]) - 1:
		board_checkf = copy.deepcopy(board)
		board_checkf[y][x] = board[y][x+1]
		xf = x+1
		board_checkf[y][x+1] = 0
		step_checkf = copy.deepcopy(steps)
		step_checkf.append('R')
		n4 = make_Node(xf, y, board_checkf, step_checkf, 'R', q)
		if n4 not in visited:
			visited.add(n4)
			q.append(n4)	

def main():
	import sys
	# transfer input into 2D-array
	board = [[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
	print(can_solved(board))

if __name__ == '__main__':
	main()