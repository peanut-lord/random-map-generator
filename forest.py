from random import choice

class ForestShape():
    def __init__(self):
        pass
    
    def getShape(self):
        """Returns the shape of a forest
        
        Creates a array with the shape of a forest. This shape will be created randomly each time
        """
        # The Dimensions of a forest are either 3 * 3 tiles or 2 * 3
        width = 3
        
        # A very small range (only 2 numbers) makes only one number appear all the time
        if choice(range(0, 100)) >= 50:
            height = 3
        else:
            height = 2
        
        shape = []
        for i in range(0, height):
            row = []
            for j in range(0, width):
                row.append(choice(range(0, 2)))
            
            shape.append(row)
            
        return shape

if __name__ == '__main__':
    shape = ForestShape()
    print shape.getShape()