class P:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"this is name: {self.name}")

class C1(P):
    def __init__(self,age):
        self.age=age
    def show(self):
        super().show() #yhan error ay ga q k parent class k show() m self.name bhi h
        # or yhan m n self.name dia hi nhi , to behter y h k jab bhi super() k zrye
        # koi method parent class s call kro to constructor bhi bnao phly 
        # ta k vo saari cheezy jo parent valy method ko achy s chalny k liye 
        # chahye vo bhi run ho skyn  
        print(f"this is child 1 ka show() {self.age}")

parent =P("parent_robina")
chiold =C1(20)
chiold.show()


# multiple inheritance is the inheritance where child class inherites from more than one parent, usually
# 2 parents liye jaty hn but 2 s ziada bhi ho skty hn

class Employe: #(1st parent)
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the employee is {self.name}")

class Dancer: #(2nd parent)
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}")
        
class EmployeeDancer(Employe,Dancer):
    def __init__(self, name, dance):# Call constructors of both parent classes explicitly
        Employe.__init__(self, name)
        Dancer.__init__(self, dance)
    def data(self):
        print(f"this is data {self.name} and {self.dance} ")
p1=Employe("nimra")
p2=Dancer("kathak")
child=EmployeeDancer("nimra","kathak")
chuld2=EmployeeDancer("nameee","danceeee")
child.show() #yha pr Employe class ka show() call ho ga q k jan hm n inherit kia to
# Employe class ko phly likha tha, jis ko phly likhyn gy us ka method call ho ga, similarly
# jis ko phly likhyn gy constructor bhi usi ka jay ga just
 
child.data()
chuld2.data()
print(EmployeeDancer.mro())

# mro() stands for method resolution order, print(child.mro()) krny s y btay ka k method
# kis tarteeb s kha kha dhoonda jay ga, is case m koi bhi method sab s phly EmployeeDancer
# m doonda jay ga then Employe m then Dancer m dhoonda jay ga, lekin agar m esy kr deti k
# class EmployeeDancer(Dancer,Employe): to phly EmployeeDancer m dhoonda jata then
# Dancer m then Employe class m dhoonda jata
