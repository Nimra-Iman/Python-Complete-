class papa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def parent_func1(self):
        print(f'i am inside parent function {self.name} is my name  and {self.age} is my age')

    def papa(self):
        print('i am papa')

class mama(papa):
    def __init__(self, name, age, classs):
        super().__init__(name, age)
        self.classs = classs


    def parent_func1(self):
        print(f'insode child {self.name}')
        # super().parent_func1()


class son(mama):
    def __init__(self, name, age, color, classs):
        mama.__init__(self, name, age, classs)
        self.color=color

    def parent_func1(self):
        print(f'i am inside son having name is {self.name}, ae {self.age}, color {self.color}, class {self.classs}')
        papa.parent_func1(self)
        mama.parent_func1(self)


p = papa('robina', 60)
# p.parent_func1()

c=mama('nimra', 20, 'BSSE')
# c.parent_func1()

s = son('asd', 26, 'brown', 'MS')
# s.parent_func1()     
# print()
# print()
# s.papa()





# ------------   WALRUS  -----------------------

print ('ok') if (a:=int(input('enter a number')) >2 ) else print('no')

