class info:
    demo = 2     #class property
    def __init__(self, val1, val2):
        self.val1 = val1   #object property
        self.val2 = val2
    def sum(self):
        return self.val1+ self.val2


obj = info(2,3)
print(obj.sum())   #jab hm info module to khi import kryn gy or esy sum ko call kryn gy
# to sab ko pta lag jay ga k y ek method h



class info:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    
    @property
    def sum(self):
        return self.val1+ self.val2


obj = info(2,3)
obj.sum       # ab sum ek variable bn gya, hala k asl m y ek function h, 
# “getters actually class ke methods ko object properties ki tarah behave
#  karwaty hn, yani function call hide ho jata hai aur variable jaisa access milta hai.”



class info:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    
    @property
    def sum(self):
        return self.val1+ self.val2
    @sum.setter
    # def sum(self, new_value1, new_value2):
        # self.value = new_value1+new_value2 #cause error, because setter always 
        # take one argument
    def sum(self, values):
        self.val1, self.val2 = values   #tuple ko unpack kia just

obj = info(2,3)
print(obj.sum )

obj.sum = (3,3) #ek hi tuple pas hua, yani ek hi value pass hui 
print(obj.sum)   #ab actually y function h, lekin lag esy rha h k jesy variable h, this
# is the main concept behind getter and seter



#REAL LOFE USAGE 
class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

user_obj = User(20)
print(user_obj.age)
user_obj.age = -2
print(user_obj.age)












# In conclusion, getters are a convenient way to access the values of an
# object's properties, while keeping the internal representation of the property hidden. 
# This can be useful for encapsulation and data validation.


#  is s ap simply class k method ko ek variable bnaty ho or us variable ki value bhi
# chnage kr skty ho
class Value_fun:
    age=23    #class property
    def __init__(self,value):
        self.value=value   #object property
        
    @property
    def given_value(self):
        return self.value
    
    @given_value.setter
    def given_value(self,new_value):
         self.value = new_value

obj=Value_fun(23)
print(obj.given_value)
obj.given_value= (234)
print(obj.given_value)

# @property ko likhny s vo method getter ban jata h yani k us ki value ko ab hm class
# ki ek property ki trah use kr skyn gy or setter s hm us ki value ko change bhi kr skty hn
# getter ka main advantage y "encapsulation" m hota h , jab hm class ki internal
# details ko hide kr dety hn yani koi ab yhi smjhy ga k y class ki ek property h bal k
# asal m to y ek method h
