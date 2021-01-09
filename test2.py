'''
    test t2 to redo the supply demand model more simply
'''

import random

agents = []
sellerlist = []
r = 0.1 #
subsistence = 75

class agent():     
    def __init__(self):
        self.x = random.random()
        self.y = random.random()

    def sell(self):
        self.sell = 100 #arbitrary no. of goods to buy
        self.marker = 'seller'
        pass

    def buy(self):
        self.buy = 50 #arbitrary no. of goods to sell
        self.marker = 'buyer'
        pass

    def neighbours(self):
        global agents
        
        self.neighbours = [n for n in agents if ( self.x - n.x ) ** 2 + (a.y - n.y ) ** 2 < r ** 2 and n != a and n.marker == 'buyer'] # terrible performance


def SupplyDemand():
    
    '''
        steps to the algo
        1. identify sellers
        1a. print sellers initial goods (test ke liye)
        
        2. find nearest neighbours of sellers
        3. round robin trades iterating through each one of the nearest neighbours for each one of the sellers
        4. print sellers final goods (test ke liye)

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
        print(seller.neighbours)


    for seller in sellerlist:
        for a in seller.neighbours:
            print(a.marker) #start from here

            
    


for a in range(100): #arbitrary no. of agents
    a = agent()
    x = random.choices((0,1))
    if x[0] == 0:
        a.sell()

    else:
        a.buy()
    print(a.marker)
    
    agents.append(a) #appends the agent instance to the agent list

SupplyDemand()
