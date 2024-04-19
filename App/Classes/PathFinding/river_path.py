from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

class PathFinder:
	def __init__(self, matrix, diagonal_movement = False):
		self.matrix = matrix
		self.grid = Grid(matrix = matrix)

		if diagonal_movement:
			self.finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
		else:
			self.finder = AStarFinder()

		self.path = []

	def empty_path(self):
		self.path = []

	def update_matrix(self, matrix):
		self.matrix = matrix
		self.grid = Grid(matrix = matrix)

	def create_path(self, start_pos, final_pos):

		start_x, start_y = start_pos
		start = self.grid.node(start_x,start_y)

		end_x,end_y = final_pos
		end = self.grid.node(end_x,end_y)

		self.path,_ = self.finder.find_path(start,end,self.grid)
		self.grid.cleanup()

		return self.path
		