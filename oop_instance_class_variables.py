# instance variable sirf instances k liye hota h or class variable saary instances
# share krty hn, instance variable saary instances pr affect nhi hota but class
# variable saary instances pr affect hota h

class Emplyee:
    company_name="Apple" #class variable
    def __init__(self, name):
        self.name=name         #instance variable
        self.raise_amount=0.2   #instance variable
    def show(self):
        print(f"{self.name} is an employee is {self.company_name} and he will get raise amount of {self.raise_amount}")
        
obj1=Emplyee("harry")
obj1.raise_amount=0.3 #this is instance variable and will changed only for this instance,
                                        # not for obj2 instance
obj1.show()
        

obj2=Emplyee("rohan")
obj2.company_name="Google" #ab m y bhi sirf isi instance k liye change kia, sab s phly
# y dekha jata h k kia y variable instance variables m given h ya nhi, agar nhi hota to 
# usy class variables s le lia jata h, is case m m n company_name is instance k liye
# change kia h, to vo chnaged value hi de ga q k company name as an instance variable
# avaliable h, agar na hoti to class variable s hi value li jati,,,,  ab obj1 k case
# m company_name as an instance variable given nhi h to vo class variable ki value hi
# le ga 
obj2.show()


Emplyee.company_name="microSoft" #is trah ab class variable ki value hi chnage ho gi
obj3=Emplyee("kinza")
obj3.show()



# !!!!!!!!!!!!!!!!!!!!!!!  Conclusion:   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Instance variables are defined at the instance level and are unique to each instance of
# the class. They are defined inside the init method and are usually used to store 
# information that is specific to each instance of the class. For example, an instance 
# variable can be used to store the name of an employee in a class that represents an 
# employee.


# Class variables are defined outside of any methods and don't need to be explicitly
# declared as class variable. They are defined in the class level and can be accessed 
# via classname.varibale_name or self.class.variable_name. But instance variables are 
# defined inside the methods and need to be explicitly declared as instance variable by 
# using self.variable_name.



