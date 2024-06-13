# agar hm kisi function ko define krny s phly ek variable define kr den say x=10 kr den
# to hm us function k ander bhi us x jis ki value 10 hi ho gi use kr skty hn, like that:
x=10    # global variable
def fun():
    print(x)
    y=5  #local variable
    print(y)
fun()
# print(y)


# lekin agar hm kisi esy variable ko function k baher use kry gy jis ko hm n function k
# ander hi define kia to hm us ko function k baher use nhi kr skty, just like the 
# variable "y" which we difined within function and it cannot be used outside
x=10    # global variable
def fun():
    print(x)
    y=5  #local variable
    print(y)
fun()
print(x) #x=10 



# if we want k function k baher jesy hi nikly to global x jis ki value 10 thi vo change 
# ho jay to hm global keyword ko use kry gy 
x=10    # global variable
def fun():
    global x
    x=5 
    y=6  #local variable
    print(y)
fun()
print(x) #x=5 now


    #                      another case

x=10    # global variable
def fun():
    x=4   #local variable
    print(x)  #x=4 here
fun()
print(x)  #x=10 here



            # -------->>>>>>  it is not good practice to use global keyword 
            # inside function to change the value of global keyword, because
            # it makes code difficuylt to debug. so prefer not to use it
