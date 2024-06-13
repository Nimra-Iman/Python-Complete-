# MAP,FILTER and REDUCE  are higher-order functions as they take function as an argument

# !!!!!!!!!  MAP  !!!!!!!!!!!!!
# agar m chati hu k li=[2,3,4] jo list h , mujy is list k saary elements double
# ho kr ek "newli" naam ki list m milyn, to m esy kru gi which is a very long and 
# little bit difficult way

li=[2,3,4,5]
sqr=lambda x: x**2
newli=[]
for i in li:
    newli.append(sqr(i))
print(newli)

# is cheeze ko hm MAP k zrye bht easily kr skty hn, hmy kia krna h k:
# map ko ek list or function paas krna h or map vo function list k hr ek ek 
# element pr apply kr k de de ga , hmy elements ko leny k liye loop lgany ki bhi
# zroort nhi h

li=[2,3,4,5]
sqr=lambda x: x**2
newli=map(sqr,li) #y cheze map object return kry gyi for efficiency purposes, is ko
# hmy apny required datatype m convert kr lena h, like below:
newli=list(map(sqr,li) )
newli=tuple(map(sqr,li) )
print(newli)


#   !!!!!!!!!!!!!!!  FILTER  !!!!!!!!!!!!!!!!!!!!!!!!!
# filter ko hm  ek condition paas krty hn (via function) or ek list paas krty hn or filter
# us list k un saary elements ko show kr deta h jo jo us condition pr met hoty ho

li=[2,3,4,5,6]
greater=lambda x:x>2
newli=list(filter(greater,li)) # or you can directly pas a lambda function like below:
newli=list(filter(lambda x:x>2,li)) 
print(newli) #agar m yhi cheeze filter k bagher esy krti (like below) to bhhtt lmba ho jata

li=[2,3,4,5,6]
newli=[]
for i in li:
    if(i>2):
        newli.append(i)
print(newli)


#  !!!!!!!!!!!!! REDUCE  !!!!!!!!!!!!!!!!!!!
from functools import reduce
li=[2,3,4,5]
newli=reduce((lambda x,y: x+y), li)
print(newli)

# reduce ko hmy import krna prta h 