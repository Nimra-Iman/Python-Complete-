# agar hm y chahty hn k jab hm kisi sequence ko loop kry (such as strings, list, tuples)
# to hmy saath saath index ka bhi pta lgta rhy to hm enumaerte buit+in function ka 
# use kry gy
list=[23,54,78,54,21]
for index,i in enumerate(list):
    # print(index, i)
    print(f"the index of {i} is {index}")
# vesy index 0 s start hota h always but if we want k vo 1 s start ho to:
list=[23,22,45,54,72,61,43]
for index,i in enumerate(list,start=1):
    print(f'{i} is present in {index}th position')

li=[23,34,45,56,67,78,89,99,0]
for i in enumerate(li):
    print(i) #y ek tuple return krta h but for index,i in enumerate(li): likhny s vo tuple
    # unpack ho jati h 