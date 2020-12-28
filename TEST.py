sellingprice = 10
subsistence = 40
farmgoods = 0
marketrate = 0

class agent():
    def __init__(self):
        self.credit = 100

    def trade(self):
        global subsistence
        
        if self.goods > subsistence:
            self.seller()

        else:
            self.buyer()
        
    def buyer(self):
        global subsistence, farmgoods, marketrate
        farmgoods -= subsistence - self.goods
            
        self.buy = sellingprice
        self.credit -= self.buy * ( subsistence - self.goods )
        print(farmgoods)
            
    def seller(self):
        global subsistence, farmgoods, marketrate
        farmgoods += self.goods - subsistence

        self.sell = sellingprice - marketrate #??
        self.credit += self.sell * ( self.goods - subsistence )
        print(farmgoods)

        
    
a = agent()
a.goods = 100
a.trade()

b = agent()
b.goods = 50
b.trade()

c = agent()
c.goods = 10
c.trade()
