# "super().ParentClassMethodName " likh kr m child class m parent class k methods ko 
# call kr skti hu, phir chahy vo parent class ka constructor ho ya parent class ka koi
#  or method ho

class Parent:
    def parentMethod(self) :
        print("i am parent method")

class Child(Parent):
    def childMethod(self):
        print("i am child method")
        super().parentMethod() #esa kr k m parentclass m mojod method ko cal kru gi

p=Parent()
p.parentMethod()
c=Child()
c.childMethod()




# When i want to access constructor:
class P:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def parentMethod(self) :
        print("i am parent method")

class C(P): #ab agar mujy is ander 2 arguments "p" class valy chahye or kuch 
    # apny izafy chahye to m esa nhi kru gi k is ka poora constructors doobara bnau, 
    # coding ka rule h k cheezon ko repeat nhi krty, to m simple is class ko 
    # inherit kr du gi "p" class s or us k constructor ko super()k zrye
    # call kr du gi or kuch apny jo izafi arguments th vo pass kr du gi, like below:
    def __init__(self, name, id, lang):
        super().__init__(name,id)
        self.lang=lang
    

    def childMethod(self):
        print(f"i am child method and my name is {self.name} with id {self.id} and my language is {self.lang}")
        super().parentMethod() #esa kr k m parentclass m mojod method ko cal kru gi

pa=P("kinza",4)
ch=C("abdullah",34,"python")
ch.childMethod()
