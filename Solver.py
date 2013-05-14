import time
from math import sqrt
from collections import OrderedDict


class Solver(object):
    """executes the alogirithms in order to find the intersections"""

    def __init__(self, algo, cirkels):
        self.algo = algo
        self.cirkels = cirkels

    def find_intersect(self):
        if (self.getAlgo() == 1):
            return self.algo1()
        if ( self.getAlgo() == 2):
          return self.algo2()
        else:
            return self.algo3()

    def getAlgo(self):
        return self.algo

    # alle algos moeten ook de tijd teruggeven
    # we gebruiken een list met 2 velden 
    # veld 1 voor een set van de intersects of de string infinity indien oneindig veen oplossingen
    # veld 2 geeft de tijds complexiteit weer 

    def algo1(self):
        #do shizlle in O(N^2)
        result = list()
        intersections = set()
        infinity = bool(0)
        tijd = time.time()
        for circle in self.cirkels:
            # kopie van de originele array heeft dus grootte n - 1
            hulp = list(self.cirkels)
            hulp.remove(circle)
            for otherCircle in hulp:
                dis = circle.center_distance(otherCircle)
                if (otherCircle.getCenter().getX() >= circle.getCenter().getX()):
                    if not ( dis > (circle.getRadius() + otherCircle.getRadius())) and not (dis < abs(circle.getRadius() - otherCircle.getRadius())) and not (dis == 0 and circle.getRadius() == otherCircle.getRadius()):
                        intersect = circle.intersect(otherCircle)
                        for inter in intersect :
                            if not (inter in intersections):
                                intersections.add(inter)
                else:
                # geen oplossingen cirkels liggen te ver van elkaar
                # geen oplossingen cirkels liggen omvat in elkaar 
                # oneindig veel oplossingen samenvallende cirkels
                    if (dis == 0 and circle.getRadius() == otherCircle.getRadius()):
                         infinity = bool(1)
        tijd = time.time() - tijd
        if (infinity):
            result.append('infinity')
            result.append(time)
            return result
        else:
            result.append(intersections)
            result.append(time)
            return result

    def algo2(self):
        #do shizzle in O(N^2) maar verhoog de effici?ntie met doorlooplijn
        result = list()
        infinity = bool(0)
        intersections = set()
        tijd = time.time()
        circlesXwaarde = dict()
        for circle in self.cirkels:
            # sorteren op linkse x value
            circlesXwaarde[circle.getCenter().getX() - circle.getRadius()] = circle
        sortedDict = OrderedDict(sorted(circlesXwaarde.items()))
        hulp = OrderedDict(sortedDict)
        for circle in sortedDict.values():
            hulp.pop(circle.LEFT.getX())
            for otherCircle in hulp.values():

                if (otherCircle.LEFT.getX() > circle.RIGHT.getX()):
                    break
                else:
                    if (self.can_intersect(circle, otherCircle)):
                        intersect = circle.intersect(otherCircle)
                        for inter in intersect :
                            if not (inter in intersections):
                                intersections.add(inter)
                    else:
                        dis = circle.center_distance(otherCircle)
                        if (dis == 0 and circle.getRadius() == otherCircle.getRadius()):
                            infinity = bool(1)
        tijd = time.time() - tijd
        if (infinity):
            result.append('infinity')
            result.append(time)
            return result
        else:
            result.append(intersections)
            result.append(time)
            return result

    def can_intersect(self, circle, otherCircle):
        dis = circle.center_distance(otherCircle)
        return not ( dis > (circle.getRadius() + otherCircle.getRadius())) and not (dis < abs(circle.getRadius() - otherCircle.getRadius())) and not (dis == 0 and circle.getRadius() == otherCircle.getRadius())
            

    def algo3(self):
        #do shizzle in O((N+S)log2(N))
        todo

                 

