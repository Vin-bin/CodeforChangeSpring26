#self, name, age, sex,height, weight,maingoal, excerise, cal=0
import test

print("make an account")
_name=input("Name: ")
_age=input("Age: ")
_sex=input("Sex: ")
_height=int(input("Height: "))
_weight=int(input("Weight: "))
_maingoal=int(input("Main Goal: "))
_exceriselvl=int(input("1.2 is for little or no exercise\n 1.4 is for light exercise 1-2 times a week\n 1.6 is for moderate exercise 2-3 times/week\n 1.75 is for hard exercise 3-5 times/week\n2.0 if you've got a physical job or perform hard exercise 6-7 times/week "))
_name=test.Acount(_name,_age,_sex,_height,_weight,_maingoal,_exceriselvl)


def menu():
    m=input("1. add cal\n2.show main goal\n3. show current calorie amount")
    return m

while True:
    m=menu()
    if m=="1":
        c=int(input("Adding:"))
        _name.addcal(c)


