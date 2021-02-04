'''
simulate 'x' number of workers and try and fulfil end conditions as well as possible.

current end condition:
    * gross economic output after a set amt of time

multiple AI will be used, and they will periodically interact with each other; maybe even trade

each agent gets
    * productivity
        * factors ???
        
    * basic needs
    * tax rate - AI definable
    * social security - AI definable
    *
    
trade rules:
    *

TODO:
    * flowchart of functions so that we can see the simulation progress
        ie. AgentInitialise -> [ MarketInitialise -> SupplyDemand ] x years

    * credit system

    * inplement a flexible market rate
    * tax rate


 database used to store values of the occupation details to be queried
 '''

#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as mplPP
import random

#control room
FirstNameMale = ['Raj', 'Mohan', 'Pranav', 'Praneel', 'Rohan', 'Anish', 'Akhil', 'Jay']
FirstNameFemale = ['Nora', 'Shreya', 'Pramila', 'Bhavya']
LastName = ['Agrawal', 'Rao', 'Singh', 'Yadav', 'Prasad', 'Jithendra']

InitialAgentNos =  100 #no of agents initially
agents = []

subsistence = 50

r = 0.1


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
                          'Name: ': [n.name for n in self.neighbours],
                          'Age': [n.age for n in self.neighbours],
                          'Job ': [n.job for n in self.neighbours],
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
 
def MarketInitialise():
    
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
                if a.sell >= b.buy: #credit argument too
                    pass
                        #a.goods, a.buy, a.credit
                        #b.sell, b.goods, b.credit
                        #create a token for the trade that has taken place

MarketInitialise()
    
#Data


BuyerData = {'Name: ': [a.name for a in agents if a.marker == 'buyer'],
              'Age': [a.age for a in agents if a.marker == 'buyer'],
              'Job   ': [a.job for a in agents if a.marker == 'buyer'],
              'Sex': [a.gender for a in agents if a.marker == 'buyer'],
              'Productivity': [a.prod for a in agents if a.marker == 'buyer'],
              'Cash': [a.credit for a in agents if a.marker == 'buyer'],
              'Status': [a.marker for a in agents if a.marker == 'buyer'],
              
              #creates a data visualisation for buyers of the simulation
            }
BuyerTable = pd.DataFrame(data = BuyerData)
print(BuyerTable, '\n', '\n')


SellerData = {'Name: ': [a.name for a in agents if a.marker == 'seller'],
              'Age': [a.age for a in agents if a.marker == 'seller'],
              'Job   ': [a.job for a in agents if a.marker == 'seller'],
              'Sex': [a.gender for a in agents if a.marker == 'seller'],
              'Productivity': [a.prod for a in agents if a.marker == 'seller'],
              'Cash': [a.credit for a in agents if a.marker == 'seller'],
              'Status': [a.marker for a in agents if a.marker == 'seller'],
              
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
              
              #creates a data visualisation of the simulation
            }

AgentTable = pd.DataFrame(data = AgentData)
print(AgentTable, '\n', '\n')

