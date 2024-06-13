# lambda function is small anonymois function without name and they are made when we
# want to make temporary small functions 
def double(x):
    return (x*2)
print("value via normal function is ",double(5)) #itny choty s kaam k liye itni line of code likhny s behter h k hm 
# lambda function bna len such as like below:

double = lambda x: x*2
print("value via lambda function" ,double(5))

#              2nd example
average= lambda x,y : (x+y)/2
print(average(2,3))



# the main use-case of lambda fuunction is when you pass function as an argument, yani
# function ko function bhi pass kr skty hn, or isi case m hi is ka mani use h or yhi is
# ko name nhi dety
def pri(square,val):
    return square(val) #yani val k ander jo 5 h vo square function k ander jay or square
# function execute ho ga yani 5x5 ho ga  
result=(pri(lambda x: x*x,5))
print(result) #agar hm normal ek square fun bnaty square=lambda x:x*x is trah s or jab is 
# ko call krty "print(square(5))" yani print k ander jis bhi trah s likha gya means lambda ko
# jis trah s call kia gia, kia kia us k ander daala gya vo sab vesy hi us function
# ki body m daalna h jis m hm lambda function ko paas kr rhy hn, now:  square(val) bilkul
# esy hi h jesy print(square(5)) h yani val ki jga 5 a gya 
 





 #                       second example
def main(average,val1,val2):
    return average(val1,val2) 
print (main(lambda x,y: (x+y)/2, 2,3))
   


def myfunc(x):
  return lambda y: x+y
otherVal = myfunc(10)
print(otherVal(100))



# Calculating Area: Write a function that calculates the area of different
# geometric shapes (circle, rectangle, triangle) based on user input. 
# Use lambda functions as arguments to calculate the area for each shape


areaa=input("enter shape")
if(areaa=="rectangle"):
    def out(area,len,wid):
        return area(len,wid) 
    print(out(lambda x,y: x*y, 2,2))


#  Build a program that converts temperatures from Celsius to Fahrenheit
# Use lambda functions to perform the conversions.
     
                       #  (0°C × 9/5) + 32 = 32°F

def temp(farhen,celsius):
    return farhen(celsius)
print(temp(lambda x: (x*9/5) + 32,0))



 





