# Agar child m apna constructor nhi h to parent class ka constructor use hota h
# Agar child m constructor h or parent m bhi h to child class m child vala constructor
# hi use ho ga, parent valy ko use nhi kr skty, child vala constructor parent constuctor
# ko replace kr de ga
# Agar child m constructor h or yhm chahty h k child class m child vala constructor 
# bhi use ho or parent vala bhi to us case m hm super() keyword ko use krty hn


# #!!!!!!!!!!!!!  SINGLE INHERITENCE  !!!!!!!!!!!!!!!!!!!!!!!!!!
# # this is most common and most easy. sab s ziada use hoti
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def employee_data(self):
        print(f"employee info:  {self.name} has id {self.id}")

class Child(Employee):
    def occupation(self):
        print(f"{self.name} has id {self.id} and is a developer actually")
    
P=Employee("nimra",4)
P.employee_data()
# P.occupation() it is error because Parent can't use properties of child

c=Child("iman",41) #single inheritance krty hi parent class ka constructor bhi a jata h
# is liye yha ("iman",41) directly likh dia
c.occupation()
c.employee_data()

