# ek parent s kafi childs then un childs s agy childs ,, yani ek tree like structure
# e.g jesy CEO hota h phir us k neechy kafi managers hoty hn, phir hr ek managers
# k neechy bht c associations hoti hn etc etc

class CEO:
    def __init__(self,name,pen):
        self.name=name
        self.pen=pen
    def signature(self):
        print(f"the CEO '{self.name}' will sign with '{self.pen}'")
    
class Manager1(CEO):
    def __init__(self,task,name):
        super().__init__(name,pen="doller")
        self.task=task
    def work(self):
        print(f"the manager will manage '{self.task}' with pen {self.pen} if ")
        super().signature()

class Manager2(CEO):
    def management(self):
        print(f"the manager2 will manage things only if ")
        CEO.signature(self)

P=CEO("CEO_tommy","CEO_DOLLER")
c1=Manager1("manage_room_1","man1")
c2=Manager2("CEO_POPY","CEO_piano")
P.signature()
c1.work()
c2.management()
