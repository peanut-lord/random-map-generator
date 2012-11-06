from random import choice

class ForestShape():
    def __init__(self):
        """Nothing to do constructor... :) """
        pass
    
    def getShape(self):
        """Returns the shape of a forest
        
        Creates a array with the shape of a forest. This shape will be created randomly each time
        """
        # The Dimensions of a forest are either 3 * 3 tiles or 2 * 3
        width = 3
        
        # A very small range (only 2 numbers) makes only one number appear all the time
        height = 3 if choice(range(0, 100)) >= 50 else 2
        
        shape = [[choice(range(0, 2)) for j in range(0, width)] for i in range(0, height)]
        return shape
    
class MountainShape():
    def __init__(self):
        """Nothing to do constructor... :) """
        pass
    
    def getShape(self):
        """Returns the shape of a forest
        
        Creates a array for the mountain shape
        """
        return [[0, 1, 0], [1, 1, 1]]

if __name__ == '__main__':
    forest = ForestShape()
    mountain = MountainShape()
    
    print forest.getShape()
    print mountain.getShape()