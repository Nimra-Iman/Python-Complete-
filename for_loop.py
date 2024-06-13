# x={"name" : "nimra", "age":20}
# for i in x:
#     print(i)
#     print(x[i])

# list = [1,0,8,4,"nimra","iman"]
# print(list)
# for elements in list:
#     if(str(elements).isnumeric() and elements>6):
#         print(elements)

dictonery = {"nimra":1,"iman":2}
for a in dictonery:
    print("the keys in dictonery is",a) # to get only keys in dictonery
    print("the values in dictonery = ",dictonery[a])

# nested loops
for x in range(3):
    print("----")
    for items in dictonery:
        print("the keys in dictionrey = ",items )

# handeling with lists
list = ["nimra","iman","rer"]
for items in list:
    print (items)
    for a in items:
        print(a)

# range
for k in range(20, 40, 2):
    print(k)

# table of two
for p in range(1,20):
    print("2 x ",p,"=",p*2)

# table of any number entered by user
x=input("enter any number")
y=int(x)
for i in range(1,11):
    print(y ,"x" ,i,"=",i*y)


    

    


   



      