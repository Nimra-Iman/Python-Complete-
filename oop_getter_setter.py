# In conclusion, getters are a convenient way to access the values of an
# object's properties, while keeping the internal representation of the property hidden. 
# This can be useful for encapsulation and data validation.

class Value_fun:
    age=23
    def __init__(self,value):
        self.value=value
        
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
