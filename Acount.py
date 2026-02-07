#food data system
class Acount:
    # AccountList=[]
    def __init__(self, name, age, sex,height, weight,maingoal, excerise, cal=0 ):
        self.name=name
        self.maingoal=maingoal #goal  can be lose/maintain/gain
        self.age=age
        self.sex=sex
        self.height=height
        self.weight=weight
        self.exercise=excerise
        self.maingoal=maingoal
        self.cal=cal

        #finding BMR
        n=1
        if self.sex=="female":
            self.targets=(10*self.weight)+(6.25*self.height)-(5*self.age)-161
        elif self.sex=="male":
            self.targets = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) +5
        if self.exercise==1.2:
            n=1.2
        elif self.exercise==1.4:
            n=1.4
        elif self.exercise==1.6:
            n=1.6
        elif self.exercise==1.75:
            n=1.75
        elif self.exercise==2:
            n=2
        self.BMR=self.targets*n #BMR is the cal remove by existing

        #getters
    def getname(self):
        return self.name
    def gettargets (self):
        return self.BMR

    def getgoal(self):
        return self.maingoal
    #sets goal
    def setgoal(self,goal2):
        self.maingoal=goal2

    def addcal(self,inputted_cal):
        self.cal+=inputted_cal

    def getcal(self):
        return self.cal

    #checks if cal is less than or greater than goal
    def checkcal(self):
        if self.cal<self.maingoal:
            print("did not achieve main goal")
        else:
            print("achived goal")









