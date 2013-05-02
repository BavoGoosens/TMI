class Circle(object):
    """A class used to represent circles"""
    
    def __init__(self, center, radius):
        self.center = center
        self.radius = float(radius)
 
    def display(self):
        print ("Center: ", self.center)
        print ("Radius: ", self.radius)

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius
    
    def to_string( self ):
        return "|" + self.getCenter().to_string() + "|" + str(self.getRadius()) + "|" 

        




