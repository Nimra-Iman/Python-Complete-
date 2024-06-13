# agar hm chahty hn k e.g user n koi esi value de di jo hm nhi chahty to is k liye hm 
# ek error raise kry gy khud s ta k hmara code vhi pr ruk jay, esa na ho k us ghalat 
# value s hmara code agy chaly, or esa bhi ho skta h k us ghalat value ki vja s jo
# k line 5 m enter ki gi us ki vja s line 12 m error ay to is s behter h k line 5 m
# hi hm error show kr den khud s
a=int(input("enter number b/w 2 and 9"))
if(a<2 or a>9):
    raise ValueError("your value is not between 2 and 9")
else:
    print("good")

# quick quiz
# 2-9, quit-->no error
# a =(input("enter number b/w 2 and 9"))
# if(a=="quit" ):
#     print("quit is not ok")
# elif( int(a)>2 and int(a)<9):
#     print("good")
# elif(int(a)<2 or int(a)>9 or str(a)!="quit"):
#     raise ValueError("not allowed")

# way 2:
# a =(input("enter number b/w 2 and 9"))
# if(a=="quit" or int(a)>2 and int(a)<9 ):
#     print("no error")
# elif(int(a)<2 or int(a)>9 or str(a)!="quit" ):
#     raise ValueError("not allowed")

# way3 ((eaassyyy))

num=input("enter number")
if(num=="quit" or 9>int(num)>2):
    print("ok")
else:
    raise ValueError("not accepted")