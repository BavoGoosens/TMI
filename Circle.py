import matplotlib.pyplot as plt
from Position import Position

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

    def center_distance(self, other):
        return self.getCenter().distance(other.getCenter()) 

    def intersect(self, otherCircle):
        result = []
        xverplaatsing = (self.getRadius() - otherCircle.getRadius() + self.center_distance(otherCircle)) / (2*self.center_distance(otherCircle))
        yverplaatsing = sqrt(self.getRadius()^2 - xverplaatsing^2)
        if (yverplaatsing == 0):
            return result.append(Position(self.getCenter().getX() + xverplaatsing, self.getCenter().getY() ))
        else:
            result.append(Position(self.getCenter().getX() + xverplaatsing, self.getCenter().getY() + yverplaatsing))
            result.append(Position(self.getCenter().getX() + xverplaatsing, self.getCenter().getY() - yverplaatsing))
            return result
    
    def to_string( self ):
        return "|" + self.getCenter().to_string() + "|" + str(self.getRadius()) + "|" 


        




