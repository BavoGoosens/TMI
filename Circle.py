import matplotlib.pyplot as plt

class Circle(object):
    """A class used to represent circles"""
    color = 1 

    def __init__(self, center, radius):
        self.center = center
        self.radius = float(radius)
        if (Circle.color % 4 == 0):
            self.plot = plt.Circle((self.getCenter().getX(),self.getCenter().getY()),radius,color='b',fill=False) 
            Circle.color = Circle.color + 1
        elif (Circle.color % 4 == 1):
            self.plot = plt.Circle((self.getCenter().getX(),self.getCenter().getY()),radius,color='g',fill=False)
            Circle.color = Circle.color + 1
        elif (Circle.color % 4 == 3):
            self.plot = plt.Circle((self.getCenter().getX(),self.getCenter().getY()),radius,color='r',fill=False)
            Circle.color = Circle.color + 1
        else:
            self.plot = plt.Circle((self.getCenter().getX(),self.getCenter().getY()),radius,color='black',fill=False)
            Circle.color = Circle.color + 1

    def display(self):
        print ("Center: ", self.center)
        print ("Radius: ", self.radius)

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius

    def getPlot(self):
        return self.plot
    
    def to_string( self ):
        return "|" + self.getCenter().to_string() + "|" + str(self.getRadius()) + "|" 


        




