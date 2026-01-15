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

# constructor ka maqsad y hota h k agr 2 function hon, and dono m kuch parameters same hon
# and kuch different hon, to same parameters bhi hmy hr bar functions call krty huy daalny
# pry gy, to better h k construvtor bna lo, or saary params usi m daal do, ta k bar bar
# hr dfa functin call krny pr parameters na daalny pry 