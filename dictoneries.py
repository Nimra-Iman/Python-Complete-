# dictoneries are ordered collection of data items, python 3.7 onwards dictoneries otdered hn 
# but us s phly dictoneries unordered hoti thi

dict={"name":"nimra", "age":3}
print(dict["name"])  # to print value of that key, error de ga if that key not exst
print(dict.get("name"))  # to print value of that key, agar key exist na hui to error 
# nhi de gi just "none" show kry gi

# to access multiple keys
print("all keys=",dict.keys())
# to access multiple values
print("all values=",dict.values())
# it can also be done like that
for i in dict.keys():
    print(dict[i])

info={4:"nimra",11:"mahnoor",21:"aqsa",23:"tayyaba",3:""}
print(info)
print(info[21])
print("all keys=",info.keys())
print("all keys=",info.values())
for i in info.keys():
    print(info[i])
print(info.items())
for i,j in info.items():
    print(f"the value corresponding to {i} is {j}")


# ^^^^^^^^^^ nested dictoneries  ^^^^^^^^^^^^^^^^^^^^^^^^^
dict={"nimra":{"age":2,"degree":"nursery"}, "iman":{"age":4,"degree":"prep"}}
print(dict["nimra"]["age"])
print(dict["iman"]["degree"])

# ^^^^^^^^^^^^^^^^^^^  dictonery comprehensions  ^^^^^^^^^^^^^^^^^^^
dict=[i*i for i in range(1,11)]
print(dict)  #tis is list basically


# ^^^^^^^^^^^^^^^^^^^^^^^^  METHODS  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# update(), clear(), pop(), popitem(), del()

# update()  update dono ki key values to join kr k de ga lekin y sirf usi vaqat esa kry ga 
# jab dono dictoneries ki keys different hu,  if the keys are the same in both 
# dictionaries, the values from the second dictionary will overwrite the values of the
# same keys in the first dictionary.
dict1={4:"nimra",2:"iman"}
dict2={6:"kinza",5:"shiza"}
dict1.update(dict2)
print(dict1)

# clear()  y dictonery ko empty kr de ga
dict1={4:"nimra",2:"iman"}
dict2={6:"kinza",5:"shiza"}
dict1.clear()
print(dict1)

# pop()  y dictonery k us item ko delete kr de ga
dict1={4:"nimra",2:"iman"}
dict2={6:"kinza",5:"shiza"}
dict1.pop(4)
print(dict1)

# popitem() y last valy poory item ko delete kr de ga
dict1={4:"nimra",2:"iman",3:"Asaad"}
dict2={6:"kinza",5:"shiza"}
dict2.popitem()
print(dict2)

# del  yha del poori dictonery ko delete kr de ga
dict1={4:"nimra",2:"iman",3:"Asaad"}
dict2={6:"kinza",5:"shiza"}
del dict2
# print(dict2) this line will create error because dict2 is deleted

dict1={4:"nimra",2:"iman",3:"Asaad"}
dict2={6:"kinza",5:"shiza"}
del dict2[6]
print("this one",dict2)


