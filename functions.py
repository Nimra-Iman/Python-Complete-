# benefits of function:
# 1- ek to y k line of code kam ho jata h q k agar hm n baar baar 2 numbers
#  ka arithematic mean nikalna h to hmy baar baar hr number k liye code 
# likhna pry ga, lekin agar m function bna leti hu to mujy baar baar code likhny ki 
# zroorat nhi ho gi bal k m sirf us function ko call kru gi
# 2 - doosra benefit jo k pass s related h vo y h k hm project pr mil k kaam k rhy th, 
# m n apny dost s kha k tum add vala function bna kr mujy send kr dena , m sirf use kru ga 
#  to m n function bna kr ander pass likh dia or agy us function ko use kr lia
# jab body ban gai to vo bhi lga di function m 
def add(a,b):
    print(a+b)
    a+b
a =10
b=20
add(a,b)

c=2
d=3
add(c,d)

# use of pass
# agar m n function bna lia but us ki body nhi bnai,
#  m n socha  k yar body baad m end m bnau ga, agar m n vo function esy hi chor dia 
# t to indentation ka error ay ga; is s bachny k liye m pass likh du gi ta k 
# compiler agy code execute kr d
def mean(a,b):
    pass
print("nimra")


# *******************function arguments***************************
# @@@@@@@@@@@@@@@@@@@@@@@@  default arguments:  @@@@@@@@@@@@@@@@@@@@@@
def average(a=9,b=6):
    print("the avaerage  = ",(a+b)/2)
average() 
 
# what if i do above code(line 33-35) like below:
def average(a=9,b=6):
    print("the avaerage  = ",(a+b)/2)
average(a=1,b=4)  # yha compiler a and b ki value 1 and 4 respectively consider kry ga

# i can also do it like that:
def average(a=9,b=6):
    print("the avaerage  = ",(a+b)/2)
average(1) # yha compiler a ki value 1 and b ki value 6 consider kry ga

# another case:
def average(a=9,b=6):
    print("the avaerage  = ",(a+b)/2)
average(b=2) # yha compiler a=9 and b=2 k saath kaam kry ga


# @@@@@@@@@@@@@@@@@@@@@@@@@ keyword arguments @@@@@@@@@@@@@@@@@@@@@@@@@
# order ki prvah kiye bagher arguments ko pass krna
def name (fname,secname):
    print("hello",fname,secname)
name(secname="iman",fname = "nimra")

# @@@@@@@@@@@@@@@@@@@@@@@ required arguments @@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def names(fname,secname,thirdname):
#     print("hello", fname,secname,thirdname)
# names("nimra","imna") # ab yha error ay ga q k third argument ki value pass krna zroori h 

# @@@@@@@@@@@@@@@@@@@@@ variable length argument @@@@@@@@@@@@@@@@@@@@@@
def var(*number):
    sum=0
    for i in number:
        sum=sum+i
        print("average is", sum/len(number))
var(1,2,3)

# example 2
def iman(*nim):
    for i in nim:
        print("hello", i)

iman("kin","za")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$  RETURN  $$$$$$$$$$$$$$$$$$$$$$$
def ret (a,b):
    return (a+b)
c=ret(2,3)
print("sum = ",c)
# (a+b) jo return hua vo c n receive kia


