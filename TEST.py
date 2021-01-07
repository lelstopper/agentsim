import random

sellingprice = 10
subsistence = 40
farmgoods = 0
marketrate = 0
agents = []
r = 1

class agent():
    def __init__(self):
        self.credit = 100
        self.x = random.random()
        self.y = random.random()

    def neighbours(self):
        global agents
        
        self.neighbours = [n for n in agents
                          if ( self.x - n.x ) ** 2 + (a.y - n.y ) ** 2 < r ** 2 and n != a] # terrible performance
    def buyer(self):
        global subsistence, farmgoods, marketrate
        #farmgoods -= subsistence - self.goods
        self.marker = 0
        self.buy = sellingprice
        #self.credit -= self.buy * ( subsistence - self.goods )
        #print(farmgoods)
            
    def seller(self):
        global subsistence, farmgoods, marketrate
        self.sell = sellingprice - marketrate #??
        self.marker = 1
        
        #farmgoods += self.goods - subsistence
        #self.credit += self.sell * ( self.goods - subsistence )
        #print(farmgoods)


def supplydemand():
    global agents, subsistence, sellerlist
    
    buyerlist = []
    sellerlist = [] #dummy list
    
    for a in agents:
        if a.goods > subsistence:
            a.seller()
            sellerlist.append(a)

        else:
            a.buyer()
            buyerlist.append(a)
       
    for a in sellerlist:
        a.neighbours()
        for b in a.neighbours:
            if b.marker == 0:
                #offer a trade
                tosell = min((subsistence - b.goods), (a.goods - subsistence)) #temp var
                
                if a.goods < tosell:
                    break

                else:
                    #sales process happens here
                    a.credit += a.sell * ( tosell )
                    b.credit -= b.buy * ( tosell )
                    a.goods -= tosell
                    b.goods += tosell
                
            else:
                pass
                    

    
x = agent()
x.goods = 100

b = agent()
b.goods = 50

c = agent()
c.goods = 10

for a in range(10):
    a = agent()
    agents.append(a)
    a.goods = random.randint(0,100)



supplydemand()
print(sellerlist)


