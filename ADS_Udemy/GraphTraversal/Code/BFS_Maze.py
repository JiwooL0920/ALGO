# Design an algorithm with BFS that is able to find the shortest path from a given
# source to a given destination. The maze is represented by a two dimensional list
# [
#    [S, 1, 1, 1, 1],
#    [0, 1, 1, 1, 1],
#    [0, 0, 0, 0, 1],
#    [1, 0, 1, 1, 1],
#    [0, 0, 0, 1, D]
# ]
# The (0,0) is the source and (4,4) is the destination. 0 represents walls/obstacles
# and 1 is the valid cells we an include in the solution


#                (x, y+1)
#   (x-1, y)      (x,y)      (x+1, y)
#                (x, y-1)

from collections import deque

class MazeSolver:
	def __init__(self, matrix):
		self.matrix = matrix
		# D(0,1), U(0,-1), L(-1,0), R(1,0)
		self.move_x = [1, 0, 0, -1] # one step to the left
		self.move_y = [0, -1, 1, 0] # one step to the right
		self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
		self.min_distance = float('inf')

	def is_valid(self, row, col):
		# outside the table horizontally
		if row < 0 or row >= len(self.matrix):
			return False

		# outside the table vertically
		if col < 0 or col >= len(self.matrix):
			return False

		# obstacle (wall)
		if self.matrix[row][col] == 0:
			return False

		# already visited the given cell
		if self.visited[row][col]:
			return False

		return True

	# BFS
	#                             4             4
	def search(self, i, j, destination_x, destination_y):
		self.visited[i][j] = True
		queue = deque() # O(1)
		# i = x coordinate
		# j = y coordinate
		queue.append((i, j, 0)) # 0 because in the first iteration the min distance is 0

		while queue:
			# we take the first item we have inserted
			(i, j, dist) = queue.popleft()

			# if we have reached the destination - break
			if i == destination_x and j == destination_y:
				self.min_distance = dist
				break

			# we are at the location (i,j), have to make a given move
			# L, U, R, D - consider moves one by one
			for move in range(len(self.move_x)): # range(4)
				# we calculate the position after the move
				next_x = i + self.move_x[move]
				next_y = j + self.move_y[move]

				# is it possible to make the move to cell with coordinates (next_x, next_y)?
				if self.is_valid(next_x, next_y):
					# we make the given move (BFS)
					self.visited[next_x][next_y] = True
					# we append the move to the queue
					queue.append((next_x, next_y, dist+1))


	def show_result(self):
		if self.min_distance != float('inf'):
			print("The shortest path from source to destination: ", self.min_distance)
		else:
			print("No feasible solution - the destination can not be reached!")

if __name__ == '__main__':
	m = [
		[1, 1, 1, 1, 1],
		[0, 0, 0, 0, 1],
		[1, 1, 1, 1, 1],
		[1, 0, 0, 0, 0],
		[1, 1, 1, 1, 1]
	]

	maze_solver = MazeSolver(m)
	maze_solver.search(0,0,4,4) # bottom-rightmost cell
	maze_solver.show_result()