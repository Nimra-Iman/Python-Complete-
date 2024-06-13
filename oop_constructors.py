class Person:
    def __init__ (self,nam,oc):
        self.name=nam
        self.occ=oc

    def info(self):
        print(f"{self.name} is {self.occ}")
a=Person("nimra","DEV")
a.info()

b=Person("iman","developer")
b.info()