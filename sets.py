# sets are unordered collection of objects,  unordered ka matlab y hua k jis order m ap n 
# elements ko set k ander likha h possible h k us order m ap ko output m elements show na ho
# isi liye hm in ko indexes k zrye nhi access kr skty

# sets m duplicate elements nhi aty, ap set bnaty huy agr elements duplicate kro gy to output
# m duplicated elements nhi ay gy, output m vo element sirf ek dfa hi ay ga

# sets k elements ko change nhi kr skty but sets m elements ko add or remove kr skty hn
# sets m elements ko add, remove kr skty hn but sets are unchangeable yani agr ap n set m 
#  2,3,4,5 add kia hua h to hm 2 ki jga 9 nhi kr skty, yani ap us element ko replace nhi kr 
# skty, ha albata ap un ko add ya remove kr skty ho
  
a={5,3,7,1,"nimra",True}
print(a) 


s={2,1,"nim",True, 33}
print(s)
#  When you create a set containing True, it is considered the same as
# 1 in the context of sets because in Python, True is equivalent to 1 
# and False is equivalent to 0. Therefore, the set {2, 1, "nim", True, 33}
# will have only one occurrence of 1, not both 1 and True, as they are considered
# the same element.

b={3,5,8,"nimra"}
for i in b:
    print(i)

# to create empty set: we do it like that
z=set()
print(type(z))
# agar hm eplty set is trah bnay "z={}" to is ki type dictonery ho jay gi

# ^^^^^^^^^^^^^^^^^^^^^^  list methods  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#             union(), update(), intersection(),intersection_update(),
#             symmetric_difference(), symmetric_difference_update(), difference(), 
#             difference_update(), isdisjoint(), issuperset(),issubset(),add(), discard(), 
#             remove(),pop(),del(),clear()
# union()
s1={2,3,4,1}
s2={4,5,7}
d=(s1.union(s2))
print(d)
          #union s y tha k two sets mil kr ek new set m gay or s1 ands s2 change nhi huy
          #  but update s s1 hi chnage ho gya
# update()
s1={2,3,4,1}
s2={4,5,7}
s1.update(s2)
print(s1)
print(s2)

# intersection()
s1={2,3,4,1}
s2={4,5,7}
w=s1.intersection(s2)
print(w)
print(s1)
print(s2)

# intersection_update
s1={2,3,4,1}
s2={4,5,7}
print("yhan s")
s1.intersection_update(s2)
print(s1)
print(s2)

# symmetric difference   symmetric_difference: jo elements dono m common na ho
s1={2,3,4,1}
s2={4,5,7}
print("yhan s")
w=s1.symmetric_difference(s2)
print(w)
print(s1)
print(s2)

# symmetric difference update
s1={2,3,4,1}
s2={4,5,7}
print("yhan s")
s1.symmetric_difference_update(s2)
print(s1)
print(s2)

# difference  difference: jo elements ek m ho but doosry m na ho
s1={2,3,4,1}
s2={4,5,7}
print("yhan ssss")
w=s2.difference(s1) #and this line will give different output than "w=s1.difference(s2)"
print(w)
print(s1)
print(s2)

# difference_update
s1={2,3,4,1}
s2={4,5,7}
print("yhan s")
s1.difference_update(s2) 
print(s1)
print(s2)

# isdisjoint()    disjoint: if A intersection B = 0
s1={2,3,4,1}
s2={4,5,7}
print("yhan s")
print(s1.isdisjoint(s2)) 

# issuperset()   agar s1 k ander s2 valy bhi saary elements ho gy to s1 super set ho ga s2 ka or s2 subset ho ga s1 ka
s1={2,3,4,1}
s2={4,5,7}
print("yhan s")
print(s1.issuperset(s2)) 

# issubset()   
s1={2,3,4,1}
s2={4,5,7}
print("yhan s")
print(s2.issubset(s1)) 

# add()   kisi set k ander koi element add krna ho to
s1={2,3,4,1}
s2={4,5,7}
print("yhan s")
s1.add(5)
print(s1)

# remove()/discard()  y dono methods hi sets s kisi element ko remove krty hn but
#  difference dono m y h k agar hm n koi esi value remove krna chahi jo k set m present
# hi nhi h to remove() value error raise kry ga but discard() koi error raise nhi kry ga
s1={2,3,4,1}
print("yhan s")
s1.remove(2)
print(s1)
# s1.remove(9) #it will raise error
# print(s1)
s1.discard(9)
print(s1)

# pop
s1={2,3,4,1}
print("yhan s")
s1.pop()  #pop set k last elemen ko remove krti h but set unordered hoty hn to
# last element koi bhi ho skta h , so pop() removes any element from set
print(s1)

# del     y ek keyword h jo poora ka pooora set hi delete kr deti h 
s1={2,3,4,1}
print("yhan s")
del(s1)
# print(s1)  #y line error raise kry gi k "set is not defined" q k set to delete ho gya

# clear()   #agar ap chahty ho k set k saary elements khatam ho jay, but set khatam na ho;
#  yani hmara saara set empty ho jay
s1={2,3,4,1}
print("yhan s")
s1.clear()
print(s1)

# to find whether certain element present in set or not:
s1={2,3,4,1}
if 2 in s1:
    print("yes")
else:
    print("no")

