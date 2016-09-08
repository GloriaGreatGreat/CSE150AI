# Yujia Li A98064697
# Ze Li A11628864
# Wei Wang A97031723

__author__ = 'yul200@ucsd.edu, zel014@ucsd.edu, wew026@ucsd.edu'

# check if the board is already solved or not
# return True if it is, or return False otherwise
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

def main():
	import sys
	# transfer input into 2D-array
	board = [[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
	print(is_solved(board))

if __name__ == '__main__':
	main()