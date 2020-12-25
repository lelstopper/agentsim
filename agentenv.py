#imports
import random
import numpy as np
import matplotlib.pyplot as mplPP


#classes
class agent:
    #creates the agent of the simulation

    global FirstNameMale
    global FirstNameFemale
    global LastName
    FirstNameMale = ['Raj', 'Mohan', 'Pranav', 'Praneel']
    FirstNameFemale = ['Nora', 'Shreya', 'Pramila']
    LastName = ['Agrawal', 'Rao', 'Singh']
    
    def __init__(self):            
        self.age       = random.randint(18,60)      #random number between 18-60, useless until families are implemented
        self.gender    = random.randint(0,1)        #M - 0/F - 1
        self.name      = self.naming()              #random name from a preexisting dict
        self.job       = self.farmer()              #starts w farmer, changes to a higher value later on
        self.health    = 100                        #if health reaches 0 then agent dies and death of old age...
        self.prod      = 100                        #can probably be modified by a bunch of factors including health
        self.x         = random.random()
        self.y         = random.random()

    def naming(self):
        if self.gender == 0:
            firstname = random.choice(FirstNameMale)
        else:
            firstname = random.choice(FirstNameFemale)

        lastname = random.choice(LastName)\
        self.name = firstname + lastname

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
def AgentInitialise(): #creating the required agents at the start of the sim
    global agents
    global InitialAgentNos
    for i in range(InitialAgentNos):
        a = agent()
        agents.append(a)

def BabyRate():
    global NewAgents
    global agents
    
    NewAgents = 0 #reproduction rate influenced by the rel. prosperity of the farmers: more importanty3
    for a in range(NewAgents):
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
    mplPP.scatter(x, y, c = c) #color implementation - probably doesnt completely work
    mplPP.show()


def CallAgent():
    global agents
    agentReq = str(input('This is a placeholder prompt: Entering the first and last name will bring you the profile of the agent you want to see'))

    for a in agents: 
        if a.name == agentReq:
            #display the agent details in a UI element
            pass
    else:
        print('the agent you requested cannnot be found')

        
#control room/ vars        
InitialAgentNos = 100 #no of agents initially
agents = []
AgentInitialise()
year = 0 #counter of the simulation year;

ModelAgent = agent()
agents.append(ModelAgent)

'''
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
'''


#tests
print(len(agents))
PlotSim()

