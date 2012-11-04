class Map():

	def render(self, x, y):
		tiles = []

		# Draw bounds
		for i in xrange(0, x):

			# Tile row
			row = []

			for j in xrange(0, y):
				# Top, bottom, outer left and right always have walls
				if i == 0 or i == x - 1 or j == 0 or j == y - 1:
					row.append('#')
				else:
					row.append('@')

			tiles.append(row)

		self._printTiles(tiles)

	def _debugTiles(self, tiles):
		print tiles

	def _printTiles(self, tiles):
		for t in tiles:
			print ''.join(t)

if __name__ == '__main__':
	map = Map()
	map.render(20, 20)
