import sys
li=[]
for i in range(1,201):
    li.append(i)
print(li)
print("the size of list in memory is = " ,sys.getsizeof(li)," bytes") #1656bytes
# yha sirf list m 200 elements gay or itttnnnniii ziada memory occupy ho gi, agar 
# 2000000000 elements hoty to shayad code hi run na hota q k itttttnnnnniiii ziada
# memory to kia pta avaliable hi na hoti,, is liye hm generator function ko
# use krty hn jo k poori ki poori list ko memory m load nhi krta bal k ek ek kr k value
# ko generate krta h: e.g like below:

def generator():
    for i in range(1,201):
        yield i #yield i krny ka matlab y hua k jab tak next ko call na kia value 
        # generate nhi ho gi ,,, The yield statement returns a value from the generator 
        # and suspends the execution of the function until the next value is requested. 

gen=generator()
print(next(gen)) # The next() function is used to request the next value from the generator
print(next(gen))
print(list(gen))
print("the size of list in memory is = " ,sys.getsizeof(list(gen))," bytes") #56 bytes

for j in gen():
    print(j) #esy bhi kr skty hn, generator function m jitni range di hui h to ek ek
    # kr k elemnts khud hi generate ho jay gy


gen=(x**2 for x in range(5)) #this is also a generator, this is similar to list but list
# m yhan [] use hoti but generator m () hoti
print(sum(gen)) #30
print(sum(gen)) #0

# GENERATORS bhhttt complex bhi hotyn hn , ghbra mat jana dekh kr, jb bhi koi function
# return ki bijay yield kr rha ho to smjh jana k generator ki baat ho rhi h


# A usecase can be, when creating a image visualization tool that takes entire directory as
# the input, you may not want to load all the images. At that time, generators can be used.


# Benefits of Generators
# Generators offer several benefits over other types of sequences, such as lists, tuples,
# and sets. One of the main benefits of generators is that they allow you to generate the
# values on-the-fly (yani moky pr), rather than having to create and store the entire
#  sequence in memory.This makes generators a powerful tool for working with large or 
# complex data sets, as you can generate the values as you need them, rather
#  than having to store them all in memory at once.

# Another benefit of generators is that they are lazy, which means that the values are 
# generated only when they are requested. This allows you to generate the values in a more 
# efficient and memory-friendly manner, as you don't have to generate all the values up front.