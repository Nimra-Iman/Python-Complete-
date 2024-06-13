# "==" match krta h "value" ko
# "is" match krta h "exact location of object in memory"

# koi bhi datatype jo immutable ho yani k "int,string,tuple etc", to python un 2 variables
# ki same values ko memory ki same location pr rkhta h, e.g like below:
a="nimra"
b="nimra" #ab yhan memory m ek location pr nimra pra h or "a" and "b" dono usi ko
# hi refer kr rhyn hn, memry n "a" k liye alag "nimra" and "b" k liye alag "nimra"
# is liye nhi rkha q k "nimra" yani string immutable h yani chnage to hony
# valu nhi , is liye us n ek hi location pr rkh dia, doosri location ko same hi value
# k liye zaya nhi kia

x=[23,34,45]
y=[23,34,45] #y "x" and "y" memory ki ek location pr nhi hn because they are immutable
# esa bhi to ho skta h k "x" change ho jay or "y" ko chnage na kia jay, agar y same
# location pr hoty to "x" k chnage hony s "y" kha jata, yani "y" to phir us value
# ko refer kr hi nhi skta tha

# "a","b" k case m "a==b" and "a is b" dono true hon gy
# "x","y" k case m "x==y" is true but "x is y" will false

if(a is b):
    print("true")
else:
    print("not true")


if(x is y):
    print("yes")
else:
    print("no")





c=2
d=2
if(c is d):
    print("true")
else:
    print("not true")

c=2
d=2
if(c == d):
    print("true")
else:
    print("not true")

