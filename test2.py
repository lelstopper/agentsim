'''
    test t2 to redo the supply demand model more simply
'''

class agent():     
    def __init__(self):
        pass

    def sell(self):
        self.sell = 100 #arbitrary no. of goods to buy
        self.marker = 0
        pass

    def buy(self):
        self.buy = 50 #arbitrary no. of goods to sell
        self.marker = 1
        pass


def SupplyDemand():
    
    '''
        steps to the algo
        1. identify sellers
        1a. print sellers initial goods (test ke liye)
        
        2. find nearest neighbours
        3. round robin trades iterating through each one of the nearest neighbours for each one of the sellers
        4. print sellers final goods (test ke liye)

    '''
    if a.marker == 0:
        sellerlist.append(a)

    else:
        pass
    




for a in range(10): #arbitrary no. of agents
    a = agent()
    random.choice(a.sell(), a.buy())
    agents.append(a) #appends the agent instance to the agent list
    
        
