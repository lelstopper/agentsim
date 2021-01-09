#imports
import random
import numpy as np
import matplotlib.pyplot as mplPP

        
#control room/ vars        
InitialAgentNos = 100 #no of agents initially
agents = []
BuyingRate = 1.0
SellingRate = 1.0
subsistence = 40 #food required per year to survive
sellerlist = []
year = 0 #counter of the simulation year;
r = 0.1

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
        self.prod      = random.randint(1,100)      #can probably be modified by a bunch of factors including health
        self.x         = random.random()
        self.y         = random.random()
        self.name()                                 
        self.farmer()                               #starts w farmer, changes to a higher value later on
        self.credit = 100

        if self.prod > subsistence:
            self.sell()

        else:
            self.buy()

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

    def sell(self):
        global subsistence
        
        self.sell = self.goods - subsistence#arbitrary no. of goods to sell
        self.marker = 'seller'
        pass

    def buy(self):
        global subsistence
        
        self.buy = subsistence - self.goods #arbitrary no. of goods to buy
        self.marker = 'buyer'
        pass

    def neighbours(self):
        global agents
        
        self.neighbours = [n for n in agents if ( self.x - n.x ) ** 2 + (self.y - n.y ) ** 2 < r ** 2 and n != self and n.marker == 'buyer'] # terrible performance

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
    
    '''
        steps to the algo
        1. identify sellers
        
        2. find nearest neighbours of sellers
        3. round robin trades iterating through each one of the nearest neighbours for each one of the sellers

        TODO:
        4. implement credits so that if person is poor, he cannot buy anymore stuff
        5. inplement a flexible market rate

    '''

    global agents, sellerlist
    
    for a in agents:
        if a.marker == 'seller':
            sellerlist.append(a) #step 1
            #print(a.sell) #step 1a

        else:
            pass

    for seller in sellerlist: #step 2
        seller.neighbours()
        #print(seller.neighbours)


    for seller in sellerlist:

        for a in seller.neighbours:
            toSell = subsistence - a.buy
            if seller.sell > toSell:
                seller.sell -= toSell
                a.buy += toSell

            else:
                a.buy += seller.sell
                seller.sell = 0

    '''
    for a in agents: #test code
        if a.marker == 'buyer':
            print(a.buy)
    '''


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
SupplyDemand()

