# class Employee:
#     companyName= "Apple"
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"{self.name} is an employee in company {self.companyName}")

#     @classmethod
#     def changeCompanyName(cls,newName):# (ab tak m n "@classmethod" ko comment kia
#         #  hua h)  #y simple ek instance method h jo k sirf us
#         # instance k liye company ka name change kry ga jis k liye hm isy call kryn gy
#         # "cls" ki jga kuch bhi likhdo , chahy "Self" likho chahy "gobhi" likho chahy
#         # "tomato" likho koi farak nhi prta, vo phly argument ko instance ko hi consider 
#         # krta h (ab tak m n "@classmethod" ko comment kia hua tha)   -----------------  
#         #  lekin agar ap isi methid k uper @classmethod ka
#         # decorator lga do to y ek classmethod ban jay ga yani k ab "cls" k ander
#         # vo instance nhi ay ga jis k liye is ko call kia ja rha h bal k is k ander
#         # class ay gi, yani a classMethod k liye class variables ko change kr skty ho
#             cls.companyName=newName

# obj1=Employee("nimra")
# obj1.show()
# obj1.changeCompanyName("Tesla")
# obj1.show()

# print(Employee.companyName)


#!!!!!!!!!!!!!!!  CONCLUSION  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# It's important to note that class methods cannot modify the class in any way. If you 
# need to modify the class, you should use a class level variable instead.
# Python class methods are a powerful tool for defining functions that operate
#  on the class as a whole, rather than on a specific instance of the class. They are 
#  useful for creating factory methods, alternative constructors, and other types of 
#  methods that operate at the class level.


#   !!!!!!!!!!!!!  CLASS METHODS AS ALTERNATE CONSTRUCTORS  !!!!!!!!!!!!!!!!!!!

# baaz oqat data different formats m dia jata h, such as "nimra_20" is trah de dia gia
# yani ek string ki form nijay is k '"nimra",20' , to hm vo data ("nimra_20" vala)
# directly constructor ko nhi de skty, hmy is ko phly required format m convert krna 
# hota h like i done below:  

# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def show(self):
#         print(f"{self.name} is an employee of age {self.age} years")

# obj1=Employee("harry",20)
# obj1.show()

# string="nimra_20"
# obj2=Employee(string.split("_")[0],int(string.split("_")[1])) 
# obj2.show() #but this is not a good practice k hm class k baher code ko itna ugly bna 
# rhyn hn, hmy kuch esa krna h k jab data pas kia jay to class k ander hi vo
# required format ho or phir constructor ko us format m pas kr dia jay jo vo 
# chahta h to is k liye hm classMethods ko as an alternative constructor k tor pr
#  use krty hn,,,,,,,,  so will do it like below:

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("_")[0],int(string.split("_")[1])) #ab yhan cls m 
    # Employee a gya or Employee k ander comma s phly "nimra" and comma k baad "20"
    # a gya , to is trah "nimra" name ko pas kr dia gya vo "name" jo uper vala jo
    # normal constructor h us k ander hota h or "20" age ko de dia gya ,,,,,
    # yani "cls(string.split("_")[0],int(string.split("_")[1]))" brabar h 
    # is line k "Employee("harry",20)" yani m jo return kr rhi hu vo class ka 
    # ek instance h

    # us return vali line ko m esy bhi likh skti hu like below:
        # name,age=string.split("_")
        # return cls(name,int(age))

    def show(self):
        print(f"{self.name} is an employee having age {self.age}")

string="nimra_20"
obj1=Employee.fromstr(string)
obj1.show()



        



