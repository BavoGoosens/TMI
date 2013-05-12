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

    def algo1(self):
        #do shizlle in O(N^2)
        intersections = []
        for circle in self.cirkels:
            hulp = list(self.cirkels)
            hulp.remove(circle)
            for otherCircle in hulp:
                dis = circle.center_distance(otherCircle)
                if not ( dis > (circle.getRadius() + otherCircle.getRadius())) and not (d < abs(cirle.getRadius() - otherCircle.getRadius())) and not (dis == 0 and circle.getRadius() == otherCircle.getRadius()):
                        intersect = circle.intersect(otherCircle)
                        if not (intersect in intersections):
                            intersections.append(intersect)
                else:
                    # geen oplossingen cirkels liggen te ver van elkaar
                    # geen oplossingen cirkels liggen omvat in elkaar 
                    # oneindig veel oplossingen samenvallende cirkels
                    if (dis == 0 and circle.getRadius() == otherCircle.getRadius()):
                        return 'infinity'
        return intersections

    def algo2(self):
        #do shizzle in O(N^2) maar verhoog de effici?ntie met doorlooplijn
        todo

    def algo3(self):
        #do shizzle in O((N+S)log2(N))
        todo

                 

