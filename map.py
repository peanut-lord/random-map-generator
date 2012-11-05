from __future__ import print_function
from random import choice
from forest import shape

class Map():
	
	# Ready to draw a map element
	STATE_READY = 1
	
	# Started drawing map elements (like a group of trees for a forest9
	STATE_STARTED = 2
	
	# Token for Bounds
	TOKEN_WALL = '#'
	TOKEN_SPACE = '-'
	TOKEN_TREE  = 'T'
	TOKEN_WATER = 'W'
	
	# Dimension of the map
	size = {'width': 20, 'height': 20}
	
	# Coords of the forest
	forest = None
	
	# The map
	tiles = []
	
	def __init__(self, width, height):
		# Map dimensions will be used to calculate amount of forests, seas and blocks
		self.size['width'], self.size['height'] = width, height
		self._calculateForest()
	
	def _calculateForest(self):
		# todo calc all coords through?
		
		# Estimate the amount of forests. The trees should take one quarter of the map, 
		# each has 6 tiles at max
		forest = (self.size['width'] + self.size['height'] / 4) / 6;
		
		# Find some places where to start with a forest (via random)
		# Always check that the tree's are within the bounds
		numForest = len(shape) # used to pick a random forest shape
		
		toPlace = []
		while True:
			# Find some random coords, -1 for the borders
			x = choice(range(1, self.size['width']-1))
			y = choice(range(1, self.size['height']-1))
			
			# todo check if another forest is within reach/crosses our bounds
			shapeType = choice(range(0, numForest))
			
			# Check bounds
			if x + 3 >= self.size['width'] or y + len(shape[shapeType]) >= self.size['height']:
				# Inside border
				continue;
			
			# store
			toPlace.append({'x': x, 'y': y, 'type': shapeType})
			
			# We need one less forest :)
			forest -= 1
			
			if forest == 0:
				break;
			
		self.forest = toPlace
		
	def _isBound(self, x, y):
		"""Returns if the coordinates in the tiles are bounds"""
		return x == 0 or x == self.size['width'] - 1 or y == 0 or y == self.size['height'] - 1
	
	def _hasTree(self, x, y):
		for i in self.forest:
			# We always draw from left to right, so check if the forest is within the coord's
			if i['x'] + 2 >= x and x >= i['x'] and i['y'] + 2 >= y and y >= i['y']:
				# return True
				s = shape[i['type']]
				
				# The deltas can be used as the array index of the shape
				deltaY = y - i['y']
				deltaX = x - i['x']
				
				try:
					# Try to access root key
					if s[deltaY][deltaX] == 1:
						return True
					else:
						return False
				except (Exception) as e:
					return False

	def _calculateTiles(self):
		
		# Draw bounds
		for y in xrange(0, self.size['height']):

			# Tile row
			row = []

			for x in xrange(0, self.size['width']):
				# Top, bottom, outer left and outer right always have walls
				if self._isBound(x, y):
					row.append(self.TOKEN_WALL)
				else:
					# We don't want a boring map, what about some water, trees and blocks? 
					if self._hasTree(x, y):
						row.append(self.TOKEN_TREE)
					else:
						row.append(self.TOKEN_SPACE)

			self.tiles.append(row)

	def _printTiles(self):
		for t in self.tiles:
			print(''.join(t))

	def render(self):
		self._calculateTiles()
		self._printTiles()

if __name__ == '__main__':
	tileMap = Map(40, 20)
	tileMap.render()
