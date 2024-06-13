tup=("nim")
print(tup)
tup=(2,4,5,"nimra")
print(tup)
tup=(1)
print(type(tup)) #is ki output integer ay gi q k jab bhi hm ek element k zrye tuple bnany
# ki koshish kry gy to vo is ko integer consider kry ga 
# if we want to create tuple of single element, we do like this
tup=(1,)
print(type(tup))

# jesy hm strings/lists m krty hn k phly ya doosry element ko chnage kr dety hn,
#  to yha esa krny s error ay ga just like that
# tup[0]=1
# print(tup)error den gy because tuples are immutable
   
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  TUPLE INDEXING  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tup=("nimra",True, 2,5,8,1,5,0,4,2,7)
print(tup[3:6]) 
print(tup)
# same is case with negative indexing just like strings and lists

# ^^^^^^^^^^^^^^^^^^^^^^  check for item  ^^^^^^^^^^^^^^^^^^

if "nimra" in tup:
    print("yes")
else:
    print("no")
# ^^^^^^^^^^^^^^^^^^^^^^  add, remove and change tuple  ^^^^^^^^^^^^^^^^^^^
               # we cannot directly add, remove or chnage tuple: we do it indirectly 
               # by converting it to list
tup=("nimra", 2,4,6,3,1,6,8)                   
cha = list(tup)
cha.append("rassia")
print(cha)
tup = tuple(cha)
print(tup)


# \\\\\\\\\\\\\\\\\\\\\\  OPERATIONS ON TUPLE  ////////////////////////////
# count
tuple=(1,4,2,6,9,2,2,2)
print(tuple.count(2))
# index
print(tuple.index(1))
# concatinating
tup=("pkaista",) # pkaista k baad "," is liye lgaya q k single lement h, python us single element ko ab ek string consider kry ga
tupp=tuple+tup
print("by concatinationg two tuples = ",tupp)
# length of tuple
print(len(tuple))
  

# List k saary methods aap tuple m use kr skty ho
# bas ek baar us tupke ko list m convert kr dena phir jo chahy kro q k phir
# us ko chnage kia ja sky ga lekin yaad rhy k baad m final modified tuple hasil krny k liye
# us list ko tuple m convert kr dena


