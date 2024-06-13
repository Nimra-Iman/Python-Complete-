class RailwayForm:
    name="nimra"
    num=2
    def info(self):
        print(f"{self.name} your train is booked with number {self.num} ")

a=RailwayForm()
a.name="iman"
a.num=222
a.info()
RailwayForm.info(a) #y ek or tarika hota h class k methods ko cal krny ka
# is y achy s show ho rha h k self k ander "a" object ja rha h

# self s murad vo object jis k mutabik y method call kia ja rha h, ab yha a k mutabik
# call kia ja rha h to self k ander "a" aya or phir "self.name" k ander "a.name"
# aya and "a.name='iman'"
b=RailwayForm()
b.name="fatima"
b.num=1
b.info()

c=RailwayForm()
c.info()

# koi bhi jo method ap class m likho to "self" dena zruri hota h , in mossttlllyyy cases
# but not in all cases, e.g static methods m self ko dena zruri nhi hota 

# INTERVIEW m y question akser poocha jat h k class k ander kia hr method k ander ap ko
# self pass krna hota h to answer "NO" hota h because static methods k ander self pas krna
# zruri nhi hota 