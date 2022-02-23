class Solution(object):
	# def isValidSudoku(self, board):
	# 	"""
	# 	:type board: List[List[str]]
	# 	:rtype: bool
	# 	"""
	#
	# 	row = {val:[] for val in [0,1,2,3,4,5,6,7,8]}
	# 	col =  {val:[] for val in [0,1,2,3,4,5,6,7,8]}
	# 	# box = [[[] for _ in range(3)] for _ in range(3)]
	# 	box = set()
	#
	#
	# 	for i in range(9):
	# 		for j in range(9):
	# 			if board[i][j] != ".":
	# 				n = int(board[i][j])
	# 				if (n in row[i]) or (n in col[j]) or (n in box): #(n in box[i//3][j//3])
	# 					return False
	# 				else:
	# 					row[i].append(n)
	# 					col[j].append(n)
	# 					box
	# 					# box[i//3][j//3].append(n)
	# 	print(box)
	#
	# 	return True

	# def isValidSudoku(self, board):
	# 	"""
	# 	:type board: List[List[str]]
	# 	:rtype: bool
	# 	"""
	#
	# 	row = {val:[] for val in [0,1,2,3,4,5,6,7,8]}
	# 	col =  {val:[] for val in [0,1,2,3,4,5,6,7,8]}
	# 	box = [[] for i in range(8)]
	# 	print(box)
	#
	# 	for i in range(9):
	# 		for j in range(9):
	# 			if board[i][j] != ".":
	# 				n = int(board[i][j])
	# 				if (n in row[i]) or (n in col[j]) or (n in box) :
	# 					print("false")
	# 					return False
	# 				else:
	# 					row[i].append(n)
	# 					col[j].append(n)
	#
	# 	# figure out an algorithm that returns the box number given i and j
	#
	# 	# below is brute force
	# 	box = []
	# 	for i in range(0,9,3):
	# 		for j in range(0,9,3):
	# 			if board[i][j] != ".":
	# 				n1 = int(board[i][j])
	# 				n2 = int(board[i+1][j+1])
	# 				n3 = int(board[i+2][j+1])
	#
	#
	#
	# 	print("true")
	# 	return True

	class Solution(object):
		def isValidSudoku(self, board):
			"""
			:type board: List[List[str]]
			:rtype: bool
			"""

			row = {val: [] for val in [0, 1, 2, 3, 4, 5, 6, 7, 8]}
			col = {val: [] for val in [0, 1, 2, 3, 4, 5, 6, 7, 8]}
			box = set()

			for i in range(9):
				for j in range(9):
					if board[i][j] != ".":
						n = int(board[i][j])
						if (n in row[i]) or (n in col[j]) or (n in box):
							return False
						else:
							row[i].append(n)
							col[j].append(n)
							box.add(str(n) + ":" + str(i / 3) + "," + str(j / 3))

			return True


	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		big = set()
		for i in range(0, 9):
			for j in range(0, 9):
				if board[i][j] != '.':
					cur = board[i][j]
					if (i, cur) in big or (cur, j) in big or (i / 3, j / 3, cur) in big:
						print("false")
						return False
					big.add((i, cur))
					big.add((cur, j))
					big.add((i / 3, j / 3, cur))
		print("true")
		return True


	def jin(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		# board = [[],[],[]...[]]
		# each row # board[0][0] ~[0][8]
		length = len(board)
		list = []
		# Checks each row for repitition
		for i in range(length):
			for j in range(length):
				if board[i][j] != ".":
					list.append(int(board[i][j]))
			if sum(set(list)) != sum(list):
				return False
			list = []

		# Checks each column for repitition
		list = []
		for i in range(length):
			for j in range(length):
				if board[j][i] != ".":
					list.append(int(board[j][i]))
			if sum(set(list)) != sum(list):
				return False
			list = []
		# Checks for sub squares

		for k in range(0, 7, 3):
			list = []
			for i in range(k, k + 3, 1):
				for j in range(0, 3, 1):
					if board[i][j] != ".":
						list.append(int(board[i][j]))
			if sum(set(list)) != sum(list):
				return False

			list = []
			for i in range(k, k + 3, 1):
				for j in range(3, 6, 1):
					if board[i][j] != ".":
						list.append(int(board[i][j]))
			if sum(set(list)) != sum(list):
				return False

			list = []
			for i in range(k, k + 3, 1):
				for j in range(6, 9, 1):
					if board[i][j] != ".":
						list.append(int(board[i][j]))
			if sum(set(list)) != sum(list):
				return False
		return True




def jin2(self, board):
	dict = {}
	length = len(board)
	for i in range(length):
		for j in range(length):
			if board[i][j] != ".":
				if board[i][j] not in dict:
					dict[board[i][j]] = []
					dict[board[i][j]].append([i, j])
				else:
					dict[board[i][j]].append([i, j])

	for key in dict:
		list = dict[key]
		length = len(list)

		list2 = []
		for i in range(length):
			list2.append(list[i][1] + 1)
		if sum(set(list2)) != sum(list2):
			return False

		list2 = []
		for i in range(length):
			list2.append(list[i][0] + 1)
		if sum(set(list2)) != sum(list2):
			return False

		sub_square_list = []  # 1 to 9
		for i in range(length):
			row = list[i][0]
			column = list[i][1]
			if (0 <= row and row < 3) and (0 <= column and column < 3):
				sub_square_list.append(1)
			elif (0 <= row and row < 3) and (3 <= column and column < 6):
				sub_square_list.append(2)
			elif (0 <= row and row < 3) and (6 <= column and column < 9):
				sub_square_list.append(3)
			elif (3 <= row and row < 6) and (0 <= column and column < 3):
				sub_square_list.append(4)
			elif (3 <= row and row < 6) and (3 <= column and column < 6):
				sub_square_list.append(5)
			elif (3 <= row and row < 6) and (6 <= column and column < 9):
				sub_square_list.append(6)
			elif (6 <= row and row < 9) and (0 <= column and column < 3):
				sub_square_list.append(7)
			elif (6 <= row and row < 9) and (3 <= column and column < 6):
				sub_square_list.append(8)
			elif (6 <= row and row < 9) and (6 <= column and column < 9):
				sub_square_list.append(9)
		if sum(set(sub_square_list)) != sum(sub_square_list):
			return False
	return True





sol = Solution()
board = [["5","3",".",".","7",".",".",".","."]
		,["6",".",".","1","9","5",".",".","."]
		,[".","9","8",".",".",".",".","6","."]
		,["8",".",".",".","6",".",".",".","3"]
		,["4",".",".","8",".","3",".",".","1"]
		,["7",".",".",".","2",".",".",".","6"]
		,[".","6",".",".",".",".","2","8","."]
		,[".",".",".","4","1","9",".",".","5"]
		,[".",".",".",".","8",".",".","7","9"]]
# sol.isValidSudoku(board)

board2 = [["8","3",".",".","7",".",".",".","."]
		,["6",".",".","1","9","5",".",".","."]
		,[".","9","8",".",".",".",".","6","."]
		,["8",".",".",".","6",".",".",".","3"]
		,["4",".",".","8",".","3",".",".","1"]
		,["7",".",".",".","2",".",".",".","6"]
		,[".","6",".",".",".",".","2","8","."]
		,[".",".",".","4","1","9",".",".","5"]
		,[".",".",".",".","8",".",".","7","9"]]

# sol.isValidSudoku(board2)


board3 = [[".",".",".",".","5",".",".","1","."],
		  [".","4",".","3",".",".",".",".","."],  #i = 1, j = 3 --> box2            i/3 j/3 --> box2
		  [".",".",".",".",".","3",".",".","1"],  #i = 2, j = 5  --> box2 			box 3 --> box 3
		  ["8",".",".",".",".",".",".","2","."],
		  [".",".","2",".","7",".",".",".","."],
		  [".","1","5",".",".",".",".",".","."],
		  [".",".",".",".",".","2",".",".","."],
		  [".","2",".","9",".",".",".",".","."],
		  [".",".","4",".",".",".",".",".","."]]
sol.isValidSudoku(board3)