a="harry"
b="bhai"
print(a+b) #python is ko concatenate kr k de ga

a="3"
b="2"
print(a+b) # output= 32
# yhi problem h k hm python ko kis trah btayn k double quotes k ander likha
# hua mvad yani k jo string pas hui h vo ek valid integer h,,, is problem
# ko solve krny k liye hm TYPECASTING ka use krty hn (conersion of one datatype
# into other called typeCasting or typeConversions)
a="4"
b="6"
print(int(a) + int(b)) #this is explicit typecasting


# a="1"
# b="3.3"
# print(int(a)+int(b))
# the above commented lines will cause error because compiler don't
#  know how to convert 3.3 which is float into int.


# IMPLICIT TYPECASTING (jo typecasting python khud kry)
# python k ander data types k different levels hoty hn, kisi datatype ka high level
# hota h or kisi ka low level hota h, python low level vali datatype ko highlevel
# vali datatype m convert kr deta h in order to prevent data loss

a = 2
b = 3.4
print(a + b)  #yha output float m hi ay gi



# taking input
x=input("enter you name ")
print("my name is ", x)

# python input m li hui hr cheez ko string consider krta h, and we use typecasting here
# to resolve the issue
x=input("enter you 1st number")
y=input("enter you second number")
print("sum of x and y = " ,int(x) + int(y))