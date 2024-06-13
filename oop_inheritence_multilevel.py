# #                   Types of inheritance:
# # Single inheritance
# # Multiple inheritance
# # Multilevel inheritance
# # Hierarchical Inheritance
# # Hybrid Inheritance

# #!!!!!!!!!!!!!  SINGLE INHERITENCE  !!!!!!!!!!!!!!!!!!!!!!!!!!
# # this is most common and most easy. sab s ziada use hoti
# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def employee_data(self):
#         print(f"employee info:  {self.name} has id {self.id}")

# class Child(Employee):
#     def occupation(self):
#         print(f"{self.name} has id {self.id} and is a developer actually")
    
# P=Employee("nimra",4)
# P.employee_data()
# # P.occupation() it is error because Parent can't use properties of child

# c=Child("iman",41)
# c.occupation()
# c.employee_data()


# #  !!!!!!!!!!!!!!!!!!!!  MULTIPLE INHERITANCE  !!!!!!!!!!!!!!!!!!!!!!
# # the inheritance where child class inherites from more than one parent, usually
# # 2 parents liye jaty hn but 2 s ziada bhi ho skty hn

# class Employe: #(1st parent)
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"the employee is {self.name}")

# class Dancer: #(2nd parent)
#     def __init__(self,dance):
#         self.dance=dance
#     def show(self):
#         print(f"the dance is {self.dance}")
        
# class EmployeeDancer(Employe,Dancer):
#     def __init__(self, name, dance):# Call constructors of both parent classes explicitly
#         Employe.__init__(self, name)
#         Dancer.__init__(self, dance)
#     def data(self):
#         print(f"this is data {self.name} and {self.dance}") #yhan {self.dance} m error
#         # ay ga k "EmployeeDancer' object has no attribute 'dance'" q k child
#         # class constructor bhi sirf usi class ka uthay ga jo phly likhi ho gi, 
#         # is liye behter h k dono classes k constructors ko alag alag yhan call kro
    
# p1=Employe("nimra")
# p2=Dancer("kathak")
# child=EmployeeDancer("nimra","kathak")
# chuld2=EmployeeDancer("nameee","danceeee")
# child.show() #yha pr Employe class ka show() call ho ga q k jan hm n inherit kia to
# # Employe class ko phly likha tha, jis ko phly likhyn gy us ka method call ho ga 
# child.data()
# chuld2.data()
# print(EmployeeDancer.mro())

# # mro() stands for method resolution order, print(child.mro()) krny s y btay ka k method
# # kis tarteeb s kha kha dhoonda jay ga, is case m koi bhi method sab s phly EmployeeDancer
# # m doonda jay ga then Employe m then Dancer m dhoonda jay ga, lekin agar m esy kr deti k
# # class EmployeeDancer(Dancer,Employe): to phly EmployeeDancer m dhoonda jata then
# # Dancer m then Employe class m dhoonda jata


#  !!!!!!!!!!!!!!!!!!!!  MULTI LEVEL INHERITANCE  !!!!!!!!!!!!!!!!!!!!!!!!!
# the inheritance where derived class inherits from another derived class. phly parent
# the us ka child then us child ka child yani child2. ab child2 apna direct parent k
# methds ko bhi use kr skta h or sab s ooper valy parent k methods ko bhi use kr skta h
# EK PARENT S CHILD THEN CHILD THEN CHILD THEN AGIAN CHILD AND SO ON YANI Y CHAIN
# BHT LMBI HO SKTI H

class Human:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def run(self):
        print(f"human {self.name} with age {self.age} is running")
    def show(self):
        print(f"{self.name} with age {self.age} of parent")

class Employee(Human):
    def __init__(self,name,age,id):
        super().__init__(name,age) #agar parent class ka constructor child m bhi call krn
        # h to child class ka construtor bnaty huy hmy vo saary parameters bhi daalny
        # hn jo k parent class ka constructor le rha h, agar hm child class ka 
        # constructor bnaty huy vo saary parameters pass nhi krty to hmy parent class
        # k constructor ko call krty huy esy krna ho ga: like below:
        # def __init__(self,name,id): #ab yhan hm n age mention nhi ki to neechy parent class
                                      # ka constructor call krty huy us ki value saath den gy 
        #     Human.__init__(name,age=20) 
        self.id=id
    def leave(self):
        print(f"employee {self.name} having age {self.age} with id {self.id} is on leave")
    def show(self):
        Human.show(self)
        print(f"{self.name} with age {self.age} of child1 having id {self.id}")

class Programmer(Employee):
    def __init__(self,name,age,id, code_id):
        super().__init__(name,age,id)
        self.code_id=code_id
    def code(self):
        # print(f"programmer {self.name} is writting code with id {self.code_id} ") #ab yhan
        # error ay ga {self.name} pr q k m n is ka construtor bnaya to is constructir
        # n parent k constructor ko replace kr dia, parent ka constructor lanny k liye
        # mujy us ka constructor bhi call krna ho ga 
        print(f"programmer is writting code with id {self.code_id} ")

    def show(self):
        Employee.show(self)
        print(f" code_id of child2 is {self.code_id} ,{self.name}")

p=Human("human_nimra",20)
c1=Employee("employee_harry",30,6)
c2=Programmer("p_name",20,34,34)
c2.code()
print(Programmer.mro())
c2.show()
        

# print(f"{self.name} with age {self.age} of parent")
# print(f"{self.name} with age {self.age} of child1 having id {self.id}")
# print(f" code_id of child2 is {self.code_id}")