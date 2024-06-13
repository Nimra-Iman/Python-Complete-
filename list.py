# one of the most important topics
l=[3,5,6]
print(l)
l[0] = 40 
print(l) #ab yha 3 ki jga 40 a gya
print(l[0])
print(l[1])
for i in l:
    print(i)
# list are ordered colection of data items
# list are changeable means they can be altered after creating them, yani hm n list
# bnany k baad kuch add krna ho to kr skty hn, list k kisi method k zrye; lekin tuple ko 
# chnage nhi kr skty
# list can also have more than 1 datatype
list = ["nimra",True, 3, 4,{"name": "iman", "age " : 2}]
print(list)

li=[1,2 , 3] # is list k index 2 hn but length 3 h
print(li[-2]) #-ve indexing

# to find whether certain element present in lisi or not:????
if "nimra" in list:
    print("yes")
else:
    print("no")

# example 2
if "nimra" and 9 in list:
    print("yes")
else:
    print("no")
# same thing applied for strings:
if "nir" in "nimra":
    print("yes")
else:
    print("no")

# to print all items of list:
print(list)
# second way
print(li[:])
print(li[1:]) #yha 1: k baad python last ko khud hi len(li) consider kr le ga
print(li[:3]) #yha start zero s kry ga

# jump indexing
feh = [1,2,4,"nimra",4,6,1,"iman",6,2,"d"]
print(feh[0:10:2]) # yha 2 ka matlab y hua k ap n 2 jumps krny hn

# **********************  LIST COMPREHENSIONS **************************
lst=[i for i in range(5)] #for i in range(5) likhny s vo 5 characters ay gy 
# vo phly valy "i" ko diye jayn gy or vhi phly vala "i" us ki "lst" m daal de ga
print(lst) #,,,,,,,,,, mazeed list comprehension ko is trah bhi kr skty hn

lst_update=[i*i for i in range(5)] #for i in range(5) likhny s vo 5 characters ay gy 
# vo lst m daalny s phly i*i kiye jayn gy
print(lst_update)


come = []
for i in range(20):
    if(i%3==0):
      come.append(i)
print (come) 
# uper valy ko hm ek line m likh skty hn, or is ko ham
#  list comprehension k zrye kr skty hn
com=[]
com = [i for i in range(10) if(i%3==0)]
print(com)


# $$$$$$$$$$$$$$$$$  LIST METHODS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
list=[1,2,3,4]
print(list)
list.append(9)
print(list)
# append,sort, reverse, index, count, copy, insert, extend, +(concatinationg), clear

fehri = [1,3,7,2,11,4,0,4,1,5,7,3,1]
print("actual = " ,fehri)
fehri.append(22)
print(" after appending",fehri)

# count
fehri = [1,3,7,2,11,4,0,4,1,5,7,3,1]
print("actual = " ,fehri)
print(fehri.count(2))

# index
fehri = [1,3,7,2,11,4,0,4,1,5,7,3,1]
print("actual = " ,fehri)
print(fehri.index(3))

# sort
fehri = [1,3,7,2,11,4,0,4,1,5,7,3,1]
print("actual = " ,fehri)
fehri.sort()   #ascending order
print(fehri)

                       # case 2
fehri = [1,3,7,2,11,4,0,4,1,5,7,3,1]
print("actual = " ,fehri)
fehri.sort(reverse=True)   #descending order
print(fehri)

                #    example 2
fer = ["a","o","i","u","e"]
fer.sort()
print(fer)

fera = ["a","y","i"]
fera.sort()
print(fera)

# reverse
fehri = [1,3,7,2,11,4,0,4,1,5,7,3,1]
print("actual = " ,fehri)
fehri.reverse()
print(fehri)

# copy
# case 1(important concept)
l=[1,2,5,3]
m=l #esa krna achi practice nhi hoti
m.append(4) #q k esa krny s jo changes "m" m kru gi m vo vali changes "l" m bhi ho gi
print(m)
print(l) # "m" and "l" dono ki output same ay gi 


# agar m chahti hu k jo chnages "m" m kru, vo sirf "m" m hi ay to esy kru gi(case 2)
# case 2
l=[1,2,5,3]
m=l.copy()
m.append(4)
print(m)
print(l)

# "+"
l=[1,2,3,4]
m=[3,4,5,6]
k=l+m
print(k)

# insert
l=[1,2,3,4]
l.insert(2,444) # yani k m chahti hu k 2nd index pr 444 insert ho jay
print("insert vala ",l)

# extend
l=[4,5,6,7,8]
m=[1000,344,22222]
l.extend(m) #is ka matlab y h k "m" ko utha kr "l" k end pr daal do, is m actually string conctinate nhi ho rhi bal k hm "l" ko edit kr rhy hn, jab k concatinate m ek new string m 2 strings add hoti h yani concatinate hoti h  
print(l)

# clear
a=int(input("enter number of digits to add in list"))
b=[]
for i in range(a):
    c=input()
    b.append(c)
print("list you eneterd=",b)
print("list after clearing all items = = ")
b.clear()
print(b)
