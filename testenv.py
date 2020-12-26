#imports
import random
import numpy as np
import matplotlib.pyplot as mplPP

#classes
class agent:
    #creates the agent of the simulation
    
    def __init__(self):            
        self.age       = random.randint(18,60)      #random number between 18-60, useless until families are implemented
        self.gender    = random.randint(0,1)        #M - 0/F - 1
        self.name      = 'A'                        #random name from a preexisting dict
        self.job       = self.farmer()              #starts w farmer, changes to a higher value later on
        self.health    = 100                        #if health reaches 0 then agent dies and death of old age...
        self.prod      = 100                        #can probably be modified by a bunch of factors including health
        self.x         = random.random()
        self.y         = random.random()

    def job(self): 
        print(self.job.desc)    #functions for calling nested classes


    def color(self):
        print(self.job.color)
        
    class farmer():
        #differing rates of production, productivity etc.
        def __init__(self):
            self.color = 'green'
            self.desc  = 'farmer'
            #self.goods
            #self.productivity

    class doctor():
        def __init__(self):
            self.color = 'blue'
            self.desc  = 'doctor'
            
    class miner():
        def __init__(self):
            self.color = 'grey'
            self.desc  = 'miner'

    class jeweller():
        def __init__(self):
            self.color = 'yellow'
            self.desc  = 'jeweller'


#functions
def agentInitialise(): #creating the required agents at the start of the sim
    global agents
    global InitialAgentNos
    for i in range(InitialAgentNos):
        a = agent()
        agents.append(a)

def BabyRate():
    global NewAgents
    NewAgents = 0 #reproduction rate influenced by the rel. prosperity of the farmers
    for a in agents:
        a = agent()
        a.age = 0
        agents.append(a)
        
def PlotSim(): #graphical rep of the agents, jobs, health etc
    global agents
    
    x = []
    y = []
    c = []
    for a in agents:
        x.append(a.x)
        y.append(a.y)
        c.append(a.job.color)
    mplPP.scatter(x, y, c = c) #color implementation
    mplPP.show()





#control room/ vars        
InitialAgentNos = 100 #no of agents initially
agents = []
agentInitialise()
year = 0 #counter of the simulation year;
jobs = ['farmer', 'miner', 'doctor', 'jeweller', 'warrior']

ModelAgent = agent()
agents.append(ModelAgent)





while year <= 10: #simualation step
    for a in agents:
        a.age += 1
        if a.health <= 0:
            del a #delete the agent

    if year % 10 == 0: #yields statistics for mapping
        global farmgoods #total value of surplus farm goods in the system
        global popn
        popn = len(agents)
        
    
    year += 1




#tests
print(len(agents))
PlotSim()





#todo:
'''
1. occupations:
    *trader?
    * warriro
2. environmental counters
    *graphical rep. of jobs, popn, goods, cities, IMR, reproduction rate etc
    
    
3. to be implemented
    *productivity of a farmer dictates the amt of suprlus produced. this surplus allow specialisation of labour and increases the value chain.
    *luxuries and leisure (productivity boost?)
    * natural disasters
    
    
4. possible mechanics
    * settlements:
        randomly selected points on a 2D plane
        using behavioral algos, you can simulate clustering of occupations. people will attempt to be closer to traders, which offer higher prices the closer you are to them

5. problems to be solved
    * How to simulate demand variations in such a way that not everyone is a jeweller in the end?
    * Clustering and formation of towns
    * supply demand mechanic
'''
