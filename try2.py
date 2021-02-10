'''
simulate 'x' number of workers and try and fulfil end conditions as well as possible.

current end condition:
    1. gross economic output after a set amt of time
    1a. keep as many children alive to enable condition 1

multiple AIs will be used, and they will periodically interact with each other; maybe even trade



sellers will be trying to get as many goods off their hands as possible, they will even sell at a slight loss to get rid of produce.
each agent gets
    * productivity
        * factors ???
        
    * basic needs
    * tax rate - AI definable
        * decline of individual income in proportion to the tax rate
        * fixed amount to tax entire society: AI can decide who gets taxed more

    * occupational role
    * social security - AI definable
    * selling / buying price of goods - marketrate - AI definable

children can be implemented as a challenge condition for social securities etc. as of right now they have no guardians, the state must take care of them. all new agents are children w age = 0;
they do not produce anything until the  age of 18, they require subsistence levels of goods and their occupation is locked in from the moment theyre born. otherwise standard agents


TODO:
    * flowchart of functions so that we can see the simulation progress
        ie. AgentInitialise -> [ MarketInitialise -> SupplyDemand ] x years

    * SQL Connectivity
    * credit system
    * inplement a flexible market rate
    * population changes
    * tax rate
    * occupational changes
        * everyone starts off as a farmer, and the AI can probably decide when to change a farmer to say, a trader.

DONE:
    * agent initilisation


 LIST OF POSSIBLE AI CONTROLLABLE 'NODES':
     * tax rate ( flexible )
     * rate of change of occupation
     * marketrate (possible)
 '''

#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as mplPP
import random

#control room
FirstNameMale = ['Raj', 'Mohan', 'Pranav', 'Praneel', 'Rohan', 'Anish', 'Akhil', 'Jay', 'Naresh', 'Rajesh', 'Manish', 'Hitesh']
FirstNameFemale = ['Nora', 'Shreya', 'Pramila', 'Bhavya']
LastName = ['Agrawal', 'Rao', 'Singh', 'Yadav', 'Prasad', 'Jithendra', 'Chandra', 'Gowda', 'Rajesh']

InitialAgentNos =  100 #no of agents initially
agents = []

subsistence = 40
MarketRate = 1
year = 0
r = 0.25


#classes
class agent():
    #creates the agent of the simulation
    def __init__(self):            

        self.gender    = random.choice(['M','F'])       
        
        self.x         = random.random()
        self.y         = random.random()
        self.prod      = random.randint(1,100)        
        self.age       = random.randint(18,60)      #random number between 18-60, useless until families are implemented
        self.name()                                 
        self.farmer()                               #starts w farmer, changes to a higher value later on
        self.credit = 100
        
        if self.prod > subsistence:
            self.sell()

        else:
            self.buy()

    def name(self):
        #forms the identity of the agent in Q
        
        global FirstNameMale, FirstNameFemale, LastName
        
        if self.gender == 'M':
            firstname = random.choice(FirstNameMale)
        else:
            firstname = random.choice(FirstNameFemale)

        lastname = random.choice(LastName)
        self.name = firstname + ' ' + lastname
        
    def farmer(self):
        self.color = 'green'
        self.job  = 'Farmer'
        self.goods = self.prod
        
    def doc(self):
        self.color = 'blue'
        self.job  = 'doctor'
        self.goods = 0

    def miner(self):
        self.color = 'grey'
        self.job  = 'miner'
        #self.productivity

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
        
        self.neighbours = [n for n in agents if ( self.x - n.x ) ** 2 + (self.y - n.y ) ** 2 < r ** 2 and n != self and n.marker == 'buyer'] # terrible implementation

        NeighbourData = {
                          'Name': [n.name for n in self.neighbours],
                          'Age': [n.age for n in self.neighbours],
                          'Job': [n.job for n in self.neighbours],
                          'Sex': [n.gender for n in self.neighbours],
                          'Goods': [n.goods for n in self.neighbours],
                          'Cash': [n.credit for n in self.neighbours],
                          'Buy': [n.buy for n in self.neighbours]

                          #creates a DF for the neighbours to be visualised
                        }

        NeighbourTable = pd.DataFrame(data = NeighbourData)

        print(self.name + ' Neighbours: ')
        print(NeighbourTable, '\n', '\n')


#functions
def AgentInitialise():
    #creating the required agents at the start of the sim
    
    global agents, InitialAgentNos
    for i in range(InitialAgentNos):
        a = agent()
        agents.append(a)
AgentInitialise()
 
def Market1Initialise():
    
    '''
        steps to the algo
        1. identify sellers
        
        2. find nearest neighbours of sellers
        3. round robin trades iterating through each one of the nearest neighbours for each one of the sellers, creating a list

        4. complete the trades, update the status of each buyer and seller
        5. start the next year by updating environmental variables and how agents react to it

        TODO:

    '''

    global agents

    for a in agents:
        if a.marker == 'seller':
            a.neighbours()

            for b in a.neighbours:
                print(b.name + ' wants to buy '+ str(b.buy))   #state the buyers demands
                print(a.name + ' can sell ' + str(a.sell))  #state the sellers inventory
                print('\n')

                #check if the trade is possible:
                if ( a.sell >= b.buy ) and ( b.credit > b.buy * MarketRate ): #credit argument too
                    a.sell -= b.buy
                    a.goods -= b.buy
                    a.credit += ( b.buy * MarketRate )
                    
                    b.goods += b.buy
                    b.credit -= ( b.buy * MarketRate )
                    b.buy = 0

                    a.neighbours.remove(b)
                    pass #create a token for the trade that has taken place in the SQL Database
                
                elif ( a.sell < b.buy ) and (b.credit > a.sell ): #credit argument too'
                    b.buy -= a.sell
                    b.goods += a.sell
                    b.credit -= ( a.sell * MarketRate )
                    
                    a.credit += ( a.sell * MarketRate )
                    a.sell = 0
                    pass #modified trade rules

                else:
                    print('The trade did not go through')
                    pass #trade cannot go through

Market1Initialise()
    
#Data

def YrUpdate():
    '''
    steps to the algo:
        1. initialise the counter
        2. start on the first year:
            * initialise all the agents
                * define their starting productivity values, jobs, ages, location etc.
                
            * define the starting subsistence rate
            * mark each agent ( either a seller or a buyer )
            * make a list of all the nearby buyers of each seller
            * for each seller, attempt a trade with each nearby buyer in order of the list.
                * buyer can not buy any more if he has run out of credits
                * buyer can not buy any more if the seller has run out of goods 
                * buyer will not buy any more if the subsistence level has been crossed ( this needs to be worked on )
                * the seller can not trade any more when he runs out of goods to sell.
                
            * once all possible trades have been attempted, end the marketplace
            * any agent without enough goods to reach the subsistence level will be terminated.
                * count the agents terminated
            * calculate the surplus
                * tax

        3. start the next year:
            * any agent terminated is replaced, with new agent ( agent properties to be worked on next )
            * modify all old agents
                * change productivity values, jobs, increase age by 1, etc.

            * 

    '''
    pass




BuyerData = {'Name: ': [a.name for a in agents if a.marker == 'buyer'],
              'Age': [a.age for a in agents if a.marker == 'buyer'],
              'Job   ': [a.job for a in agents if a.marker == 'buyer'],
              'Sex': [a.gender for a in agents if a.marker == 'buyer'],
              'Goods': [a.goods for a in agents if a.marker == 'buyer'],
              'Cash': [a.credit for a in agents if a.marker == 'buyer'],
              'Status': [a.marker for a in agents if a.marker == 'buyer'],
              
              #creates a data visualisation for buyers of the simulation
            }
BuyerTable = pd.DataFrame(data = BuyerData)
print(BuyerTable, '\n', '\n')


SellerData = {'Name: ':         [a.name for a in agents if a.marker == 'seller'],
              'Age':            [a.age for a in agents if a.marker == 'seller'],
              'Job   ':         [a.job for a in agents if a.marker == 'seller'],
              'Sex':            [a.gender for a in agents if a.marker == 'seller'],
              'Productivity':   [a.prod for a in agents if a.marker == 'seller'],
              'Goods':          [a.goods for a in agents if a.marker == 'seller'],
              'Cash':           [a.credit for a in agents if a.marker == 'seller'],
              'Status':         [a.marker for a in agents if a.marker == 'seller'],
              
              #creates a data visualisation for sellers of the simulation
            }

SellerTable = pd.DataFrame(data = SellerData)
print(SellerTable, '\n', '\n')

AgentData = { 'Name: ': [a.name for a in agents],
              'Age': [a.age for a in agents],
              'Job   ': [a.job for a in agents],
              'Sex': [a.gender for a in agents],
              'Productivity': [a.prod for a in agents],
              'Cash': [a.credit for a in agents],
              'Status': [a.marker for a in agents],
              'Goods': [a.goods for a in agents],
              #creates a data visualisation of the simulation
              #TODO: Implement all variables
                      
            }

AgentTable = pd.DataFrame(data = AgentData)

AgentTableSave = r'C:\Users\Pranav\Documents\GitHub\agentsim\CSVs\AgentData'
AgentTable.to_csv(AgentTableSave + str(year) + '.csv')
