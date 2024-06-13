# object introspection:  k us object k ander kia kia methods, properties, attributes
# h  etc, python m sab kuch hi object hota h 

list=[1,2,3]
# print(dir(list)) # ab hmy y bta rha h k is k is list object k ander kia kia methods,
# propertries ya attricbutes hoty hn

string="this is string"
# print(dir(string))



# !!!!!!!!!!  __dict__  !!!!!!!!!!!
# The __dict__ attribute returns a dictionary representation of an object's attributes. 
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
obj1=person("nimra",20)
print(obj1.__dict__)


# !!!!!!!!!!!!!!!!  help()  !!!!!!!!!!!!!!!!!!!!!!!!!!

# The help() function is used to get help documentation for an object, including a
#    description of its attributes and methods.
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
obj1=person("nimra",20)
print(help(person))