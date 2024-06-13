# magic/dunder methods:

# dunder--> double underscore
# they are special methods that give additional functionality to your classes.
# By implementing dunder methods, you can customize the behavior of your objects and 
# make them work seamlessly with Python's language constructs.
# in methods ko call krny k liye hmy "__" lgany ki zrurt bhi nhi hoti
# e.g: __init__, __len__, __str__, __repr__ etc etc

class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return self.name #to show nice representation in the form of string, otherwise
                         #call krny pr just memory location show hoti 
    
    def __repr__(self):
        return ("employee('nimra',20)") # asal m is method ka ideal way y h k 
    # us tareeka ko show krna jis k mutabik object ko recreate kia ja skta h
    # ab y programmer ki mrzi vo usy kis trah s use krta h, lekin ideal way yhi h jo 
    # phly btaya,,,, agar __str__ likha ho ga to __repr__ vala nhi chly ga
    
    def __len__(self):
        return len(self.name)
    
    def __call__(self):
        print ("this is call")

    def __add__(self,other):
        return (self.name +  other)
    
    
obj1=employee("nimra",20)
print(obj1)
print(obj1)
print(obj1 + " newwww")
print(len(obj1)) #length find krny ka tareeka yhi h, yani dunder methods class
# k behaviour ko is trah s customize krty hn k vo language constructs k mutabik
# chaly q k agar hm is class ko import krty hn to hm to length find krny k liye
# vhi tareeka use kryn gy jo h (len(obj1)) yani y vala

obj1() #esa likha ho ga to interpretor __call__ ko search kry ga or us k ander vala
# execute kry ga, I think the practicle use case of  def__call__(self ) : method will
#be to add conclusion to a class or it can used to find total amount at the end of class.
# The call method can be used to describe the function of the class

