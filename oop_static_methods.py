# they are utitlity methods and they can't access properties of class
# They are methods jo k na to class methods s belong krty hn or na hi instance
# methods s belong krty hn
# In methods ko bnany k liye ap ko "self" ka keyword bhi pass nhi krna prta
# Zruri nhi hota k ap is method ko hr haal m instance k zrye call kro , ap is ko 
# directly bhi call kr skty ho class k name k zrye.
# Y method is liye bnay jaty hn k agar m class kisi ko send kro to he/she can
# get the advantage of that method of class q k it is possible k m jo bhi is method
# k ander likhu vo mujy any valy time m kaam ay


class temp:
    def __init__(self, num):
        self.num=num
    def show(self,no):
        self.num =self.num+no
    @staticmethod
    def add(a,b): #yhan to y method bhhttt aam sa method h, m is ko ofcourse class 
        # k baher bhi bna skti thi but agar y koi complex calculation ka method hua to
        # class k ander bnana ziada faida mand ho ga
        print(a+b )

obj=temp(2)
print(obj.num)
obj.show(3)
print(obj.num)

obj.add(2,3)
temp.add(2,3)