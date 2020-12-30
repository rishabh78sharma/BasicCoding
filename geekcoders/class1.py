class car():
    def __init__(self,modelname,year,price):
        self.modelname=modelname
        self.year=year
        self.price=price
    def price_incr(self): #class method
        self.price=(self.price*2)

honda=car('city',2017,1000000)
tata=car('Tiago',2020,8000000)
print(honda.price)
print(tata.year)
honda.cc=1500 #instance variable
print(honda.__dict__) #print all value associated with honda class object
honda.price_incr()
print(honda.price)

class supercar(car): #inheritance
    def __init__(self,modelname,year,price,cl):
        super().__init__(modelname,year,price)
        self.cl=cl
l=supercar('creta',2020,12000000,4000)
print(l.modelname)


