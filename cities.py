import matplotlib.pyplot as mplPP
import random
import numpy

r = .4

class City():
    def __init__(self):
        self.x = random.random()
        self.y = random.random()
        self.Neighbour()
        self.plot()
        
    def Neighbour(self):
        global cities
        self.neighbours = numpy.array([[n.x for n in cities if ( self.x - n.x ) ** 2 + (self.y - n.y ) ** 2 < r ** 2 and n != self  ], # can also implement an upper neighbour limit
                                       [n.y for n in cities if ( self.x - n.x ) ** 2 + (self.y - n.y ) ** 2 < r ** 2 and n != self ]]) # terrible performance acc to big O notation; this scales terribly
        
    def plot(self):
        knnx = []
        knny = []
        for i in (range(2 * len(self.neighbours[0]))):
            if i % 2 == 0:
                knnx.append(self.x)
                knny.append(self.y)

            else:
                knnx.append(self.neighbours[0][i // 2])
                knny.append(self.neighbours[1][i // 2])
            mplPP.plot(knnx,knny)
        

cities = []
cx = []
cy = []

for c in range(10):
    c = City()
    cities.append(c)

def PlotSim():
    global cities
    for c in cities:
        cx.append(c.x)
        cy.append(c.y)

    mplPP.scatter(cx, cy)    
    mplPP.show()

PlotSim()
