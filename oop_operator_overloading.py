# Operator Overloading means giving extended meaning beyond their predefined operational
# meaning. 

a=10
b=20
print(a+b) #jab hm y likhty hn to asal m y code run ho rha hota h: "int.__add__(20,30)"
# yani k int class m s __add__ ka method run kro,,, y cheeze predefined h from python.
# similarly:

a="nimra"
b="iman"
print(a+b) #jab hm y likhty hn to asal m y code run ho rha hota h: "str.__add__("nimra","iman")"
# yani k str class m s __add__ ka method run kro,,, y cheeze predefined h from python.

# lekin y cheeze predefined nhi h k hm vo objects ko add kry: e.g like below:
class temp:
    def __init__(self,x,y):
        self.x=x
        self.y=y
obj1=temp(2,3)
obj2=temp(6,7)
# print(obj1+obj2) #y cheeze predefined nhi h, to is liye hm operator ko overload
# kryn gy yani k predefined operation s ziada is ko operations provide kryn gy, like 
# below:

class temperory:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return (f"{self.x+other.x}")
o1=temperory(2,3)
o2=temperory(6,7)
print(o1+o2)  #ab yha y call ho rha h asal m:  temperory.__add__(6,2) yani k temperory 
# class m s __add__ ka method run kro


#another example
class A:
    def __init__(self, a):
        self.a=a
    def __add__(self,other):
        return self.a + other.b

class B:
    def __init__(self,b):
        self.b=b
ob1=A(2)
ob2=B(3)
print(ob1+ob2) #A.__add__(2,3)