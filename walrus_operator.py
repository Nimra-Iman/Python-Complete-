# to assign value to a variable within an expression, e.g
# print(a=4) #yhan ek expression k ander rehty huy ap assignment nhi kr skty, is liye 
# walrus operatior ka use kia jata h , ta k ek expression k ander rehty huy 
# assignments ki ja sky,,,,  print(a=4) yha  ek error ay ga "4" print nhi ho ga

print(a:=4) #yhan "4" jo k "a" ki value h vo print kr di gi, yani simple baat y h k
# phly m a=4 kr rhi hu or phir us ki value print kr rhi hu


# it is useful when you want to assign a value multiple times to a variable
# without repeating the calculation

# hr dfa loop chalny pr ek value list m s nikly gi phir updated list ki jo length ho gi
# vo "n" ki value ho gi
li=[56,67,43,23,6]
while((n := len(li)) >0):
    print("the poped value is = ",li.pop())
    print(n)
#without walrus operator: we will write code like this:(long code)
lis=[23,4,56,32,12]
while(len(lis)>0):
    print("poped value is ", lis.pop())
    n=len(lis)
    print("the value of n=",n)


#another example
food=[]
while True:
    f=input("what food you wanna eat?")
    if(f=="quit"):
        break
    food.append(f)
    print(food)

# via walrus is below:
food=[]
while ((f:=(input("what food you wanna eat?")))!="cake"):
    food.append(f)
    print(food) #it is good practice to use walrus operator



# a loop that calculates the sum of squares of numbers from 1 to 10
i=0
n=0
while(i<6):
    n=n+(i**2)
    i=i+1
print(n)
# via walrus is below:

# while i<(n:=6):




