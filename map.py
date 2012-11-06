from __future__ import print_function
from random import choice
from shape import ForestShape, MountainShape

# from forest import shape

class Map():
    # Flag for colored terminal output + the codes
    USE_CMD_COLOR = False
    CMD_FORMAT = '\033[%sm%s\033[0m'
    
    # Token for Bounds
    TOKEN_WALL = '#'
    TOKEN_SPACE = '-'
    TOKEN_TREE  = 'T'
    TOKEN_WATER = 'W'
    TOKEN_MOUNTAIN = 'M'
    
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
        self._initColor();
    
    def _initColor(self):
        """Init's the color if cmd color is enabled"""
        if self.USE_CMD_COLOR is False:
            return
        
        self.TOKEN_WALL = self.CMD_FORMAT % ('1;30', self.TOKEN_WALL) # Grey
        self.TOKEN_TREE = self.CMD_FORMAT % ('32', self.TOKEN_TREE) # Green
    
    def _calculateForest(self):
        """Calculates the postions of the forest"""
        # todo calc all coords through?
        
        # Estimate the amount of forests. The trees should take one quarter of the map, 
        # each has 6 tiles at max
        forest = (self.size['width'] + self.size['height'] / 4) / 6;
        
        # Find some places where to start with a forest (via random)
        # Always check that the tree's are within the bounds
        # numForest = len(shape) # used to pick a random forest shape
        
        toPlace = []
        shaper = ForestShape()
        while True:
            # Find some random coords, -1 for the borders
            # todo find better coord's, sometimes forest is just to close to each other 
            x = choice(range(1, self.size['width']-1))
            y = choice(range(1, self.size['height']-1))
            
            # todo check if another forest is within reach/crosses our bounds
            # shapeType = choice(range(0, numForest))
            shape = shaper.getShape()
            
            # Check bounds
            if x + 3 >= self.size['width'] or y + len(shape) >= self.size['height']:
                # Inside border
                continue;
            
            # store
            toPlace.append({'x': x, 'y': y, 'shape': shape})
            
            # We need one less forest :)
            forest -= 1
            
            if forest == 0:
                break;
            
        self.forest = toPlace
        
    def _isBound(self, x, y):
        """Returns if the coordinates in the tiles are bounds"""
        return x == 0 or x == self.size['width'] - 1 or y == 0 or y == self.size['height'] - 1
    
    def _hasTree(self, x, y):
        # Todo this code could take care of any shape
        for i in self.forest:
            # We always draw from left to right, so check if the forest is within the coord's
            if i['x'] + 2 >= x and x >= i['x'] and i['y'] + 2 >= y and y >= i['y']:
                s = i['shape']
                
                # The deltas can be used as the array index of the shape
                deltaY = y - i['y']
                deltaX = x - i['x']
                
                try:
                    return s[deltaY][deltaX] == 1
                except (Exception) as e:
                    return False
                
    def _getToken(self, x, y):
        """Returns a tile token depending if there is a object place like a tree, mountain or water"""
        # Top, bottom, outer left and outer right always have walls
        if self._isBound(x, y):
            return self.TOKEN_WALL
        else:
            # We don't want a boring map, what about some water, trees and blocks? 
            if self._hasTree(x, y):
                return self.TOKEN_TREE
            else:
                return self.TOKEN_SPACE

    def _calculateTiles(self):
        """Calculates the map with all tiles"""
        self.tiles = [[self._getToken(x, y) for x in xrange(0, self.size['width'])] for y in xrange(0, self.size['height'])]

    def _printTiles(self):
        """Prints the map to the cmd"""
        [print(''.join(t)) for t in self.tiles]

    def render(self):
        """Renders the map"""
        self._calculateTiles()
        self._printTiles()

if __name__ == '__main__':
    tileMap = Map(40, 20)
    tileMap.render()