# Agar child m apna constructor nhi h to parent class ka constructor use hota h
# Agar child m constructor h or parent m bhi h to child class m child vala constructor
# hi use ho ga, parent valy ko use nhi kr skty, child vala constructor parent constuctor
# ko replace kr de ga
# Agar child m constructor h or yhm chahty h k child class m child vala constructor 
# bhi use ho or parent vala bhi to us case m hm super() keyword ko use krty hn


class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):  #overridden method
        return (self.x * self.y)
    
class circle(Shape):
    def __init__(self, r):
        self.r=r
    
    def area(self):  #method overriding
        return (3 * self.r**2)
    
s=Shape(2,3)
# print(s.area()) 
c=circle(2)
# print(c.area())


#  !!!!!!!!!!!!  method overriding using super  !!!!!!!!!!!!!!!!!
class Parnt:
    def p(self):
        print("in parent")
class Child(Parnt):
    def p(self):
        super().p()
        print("in child")

c=Child()
# c.p()


#########  another example using super
class Shape1:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):  #overridden method
        return (self.x * self.y)
    
class circle1(Shape1):
    def __init__(self, r):
        self.r=r
        super().__init__(r,r)
    
    def area(self):  #method overriding
        return (3 * super().area())
    
s=Shape1(2,3)
print(s.area()) 
c=circle1(2)
print(c.area())


