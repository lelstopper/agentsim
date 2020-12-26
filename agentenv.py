#imports
import random
import numpy as np
import matplotlib.pyplot as mplPP

        
#control room/ vars        
InitialAgentNos = 100 #no of agents initially
agents = []
BuyingRate = 1.0
SellingRate = 1.0

year = 0 #counter of the simulation year;

FirstNameMale = ['Raj', 'Mohan', 'Pranav', 'Praneel']
FirstNameFemale = ['Nora', 'Shreya', 'Pramila']
LastName = ['Agrawal', 'Rao', 'Singh']
    

#classes
class agent():
    #creates the agent of the simulation
    #too many methods and things are being called; maybe it isnt flexible enough. :/

    def __init__(self):            

        self.gender    = random.randint(0,1)        #M - 0/F - 1
        self.age       = random.randint(18,60)      #random number between 18-60, useless until families are implemented
        self.health    = 100                        #if health reaches 0 then agent dies and death of old age
        self.prod      = 100                        #can probably be modified by a bunch of factors including health
        self.x         = random.random()
        self.y         = random.random()
        self.name()                                 
        self.farmer()                               #starts w farmer, changes to a higher value later on


    def name(self):
        global FirstNameMale, FirstNameFemale, LastName
        
        if self.gender == 0:
            firstname = random.choice(FirstNameMale)
        else:
            firstname = random.choice(FirstNameFemale)

        lastname = random.choice(LastName)
        self.name = firstname + lastname
                
    def farmer(self):
        self.color = 'green'
        self.job  = 'farmer'
        self.goods = self.prod
        #self.productivity

    def doc(self):
        self.color = 'blue'
        self.job  = 'doctor'
        self.goods = 0

    def miner(self):
        self.color = 'grey'
        self.job  = 'miner'

    def buyer(self):
        global BuyingRate
        
        pass#looks for goods in the market
    

    def seller(self):
        global SellingRate
        
        pass#looks to sell goods in the market
    
        
#functions
def AgentInitialise():
    #creating the required agents at the start of the sim
    
    global agents, InitialAgentNos
    for i in range(InitialAgentNos):
        a = agent()
        agents.append(a)
AgentInitialise()


def BabyRate():
     #reproduction rate influenced by the rel. prosperity of the farmers: more importantly it helps the sim progress. each persons progeny is slightly different,
     #allowing natural selection to determine which performs better
    
    global NewAgents, agents
    NewAgents = 0
    
    for a in range(NewAgents):
        a = agent()
        a.age = 0
        agents.append(a)
        
        
def PlotSim():
    #graphical rep of the agents, jobs, health etc
    
    global agents
    
    x = []
    y = []
    c = []
    for a in agents:
        x.append(a.x)
        y.append(a.y)
        c.append(a.color)
    mplPP.scatter(x, y, c = c) #color implementation - probably doesnt completely work
    mplPP.show()


def CallAgent():
        #when the user attempts to request certain agnts details, this fn is called
    
    global agents
    agentReq = str(input('This is a placeholder prompt: Entering the first and last name will bring you the profile of the agent you want to see'))

    for a in agents: 
        if a.name == agentReq:
            #display the agent details in a UI element
            
            pass
    else:
        print('the agent you requested cannnot be found')


def SupplyDemand():
    #at the end of every yr, when an agent attempts to sell his produce, this function is called.
    #it dictates how many of each job is present in the simulation as well
    
    global agents, subsistence, farmgoods
    subsistence = 40
    farmgoods = 0 #farm goods in the market
    
    for a in agents:

        if a.job == 'farmer' and a.goods >= subsistence:
            #trial implementation
            a.goods -= subsistence
            a.seller()
            farmgoods += a.goods

        else:
            a.buyer()


def Step():
    while year <= 10: #simualation step    
        for a in agents:
            a.age += 1
            if a.health <= 0 or a.age >= 100:
                del a #delete the agent

            if a.age < 18:
                a.prod = 0        


ModelAgent = agent()
agents.append(ModelAgent)


if year % 10 == 0: #yields statistics for mapping
    global farmgoods, popn #total value of surplus farm goods in the system
    popn = len(agents)
        
    
    year += 1


#tests
PlotSim()

