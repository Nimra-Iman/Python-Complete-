# THREE TYPES OF ACCESS SPECIFIERS/ ACCESS MODIFIERS
# Public: jo k class k baher access go skty hn
# private: jo class k baher access nhi ho skty
# protected: jo class k bilkul baher use nhi ho skty but child classes m use ho skty hn

# jo bhi method ya variable class k ander bnaty hn vo by_defualt public hoty hn


# python m directly public,private and protected ka koi concept nhi h


class template():
    def __init__(self):
        self.name="nimra"

obj=template()
print(obj.name) #access kia ja skta h q k koi bhi method ya variable by_default 
# public hi hota h



 #   !!!!!!!!!!!!!         CONSIDERED PRIVATE    !!!!!!!!!!!!!!
class Temp():
    def __init__(self):
        self.__name="iman" # "__" lgany s hm isy class k baher access nhi kr skty
        # yani is variable ko ab private consider kia ja skta h, This is known as
        #  a "weak internal use indicator" and it is a convention only,
        # not a strict rule.
        #  but esa nhi h k hm is bilkul access kr hi nhi skty class k baher,
        #  hm is ko "name mangling" k zrye class k baher access kr skty hn, 
        # "__" lga kr hm kisi variable ko outside class access nhi krny dety lekin
        # is k bavajood bhi access to kia ja skta h, y bilkul esy hi h jesy hm apni
        # car baher khari kr den bagher lock k or saath likh de k koi is ko touch na kry
        # lekin phir bhi koi bhi is ko touch to kr skta h, to yani hm variables k saath
        # "__" likh kr y indication lga skty hn k is variable k saath chera chari mat krna



obj=Temp()
# print(obj.__name)  #give an error of course
print(obj._Temp__name) #this is NAME_MANGLING

obj._Temp__name="my_name"
print(obj._Temp__name)

# print(obj.__dir__()) #y show krta h k obj pr kon kon s methods apply ho skty hn


#     PROTECTED
class Student:
    def __init__(self):
        self._name = "Harry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
# calling by object of Subject class
print(obj1._name)    
