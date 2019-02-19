from ghost import *

class Ag(Ghost):
    def __init__(self,name,age,car):
        super(__class__,self).__init__(name,age)
        self.car=car

    def getCar(self):
        return self.car

    def setter(self,name,age,car):
        super(__class__,self).setter(name,age)
        self.car=car