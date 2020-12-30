class You():
    def __init__(self,length,breath,height):
        self.length=length
        self. breath=breath
        self.height=height
    def show(self):
        print( f'{self.length} \n{self.breath} \n{self.height}')

rish=You(20,30,49)
rish.show()
print(rish.__dict__)