import matplotlib.pyplot as mplPP
import random
import numpy

r = 0.1
class City():
    def __init__(self):
        self.x = random.random()
        self.y = random.random()

    def Neighbour():
        global cities, knn
        
        self.neighbours = [n for n in cities if ( self.x - n.x ) ** 2 + (self.y - n.y ) ** 2 < r ** 2 and n != self ] # terrible performance
        knn =   numpy.array([self.neighbours[        

cities = []
cx = []
cy = []

for c in range(50):
    c = City()
    cities.append(c)

def PlotSim():
    global cities
    for c in cities:
        cx.append(c.x)  
        cy.append(c.y)

    mplPP.scatter(cx, cy)
    mplPP.plot()
    
    mplPP.show()

PlotSim()
