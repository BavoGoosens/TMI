class Position(object):
    """A class used to represent Position"""

    def __init__(self , x, y):
        self.x = x
        self.y = y 

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self, other):
        return sqrt((self.getX() - other.getx())^2 - (self.getX() - other.getY())^2)
    
    def to_string( self ):
        return "(" + str(self.getX()) + ", " + str(self.getY()) + ")"




