import Acount
import AccountList


#main account list
a=AccountList.AccountList()

#account making
def makeAccount():
    print("Make an account!")
    _name=input("Name: ")
    _age=int(input("Age: "))

    #error checking
    while _age<0:
        print("Cannot be a negative number")
        _age = int(input("Age: "))

    #error checking
    _sex=input("Please type male or female\nSex: ").lower()
    while _sex!="male" or _sex!="female":
        print("Wrong Format")
        _sex = input("Please type male or female\nSex: ").lower()

    _height=float(input("Height: "))
    while _height<0:
        print("Cannot be a negative number")
        _height = float(input("Height: "))

    _weight=float(input("Weight: "))
    while _weight<0:
        print("Cannot be a negative number")
        _weight = float(input("Weight: "))

    _maingoal=float(input("Main Goal: "))

    _exceriselvl=float(input("Please type your activity level based on the following:\n1.2 is for little or no exercise\n1.4 is for light exercise 1-2 times a week\n1.6 is for moderate exercise 2-3 times/week\n1.75 is for hard exercise 3-5 times/week\n2.0 if you've got a physical job or perform hard exercise 6-7 times/week \n"))
    while (_exceriselvl!=1.2) or (_exceriselvl!=1.4) or (_exceriselvl!=1.6) or (_exceriselvl!=1.75) or (_exceriselvl!=2.0):
        _exceriselvl = float(input("Please type your activity level based on the following:\n1.2 is for little or no exercise\n1.4 is for light exercise 1-2 times a week\n1.6 is for moderate exercise 2-3 times/week\n1.75 is for hard exercise 3-5 times/week\n2.0 if you've got a physical job or perform hard exercise 6-7 times/week \n"))

    _name=Acount.Acount(_name,_age,_sex,_height,_weight,_maingoal,_exceriselvl)
    a.add(_name)
    return _name #returns account

#menu options {to be expanded}
def menu():
    m=input("-1. switch account\n0. make account\n1. add cal\n2.show main goal\n3. show current calorie amount")
    return m

_name=makeAccount()
while True:
    m=menu()
    if m=="1":
        c=int(input("Adding:"))
        _name.addcal(c)
    elif m=="2":
        print("Main Goal is to reach",_name.getgoal())
    elif m=="3":
        print("Total Calories:", _name.getcal())
    elif m=="0":
        _name=makeAccount()
    elif m=="-1":
        te=input("Put the Name of Account")
        _name=a.getAccount(te)





