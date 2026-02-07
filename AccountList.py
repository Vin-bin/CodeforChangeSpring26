#I'm making a seperate classs to hold the accounts to make it easer to switch accountts
import Acount
class AccountList:
    def __init__(self):
        self.account_list=[]

    def addaccount(self,name,age,sex,height,weight,maingoal,exceriselvl):
        for accounts in self.account_list:
            if accounts.getname()==name:
                print("account already exists")
                return False
        self.account_list.append(Acount.Acount(name,age,sex,height,weight,maingoal,exceriselvl))
    def getAccount(self,name):
        for accounts in self.account_list:
            if accounts.getname()==name:
                return accounts



