# VIP Topic
my_var = "a"
x=10
match my_var:
    case "a":
        print("value is one")
    case "b":
        print("value is two")
# uper vali lines ka matlab y h k in logo n jo ek variable likha h
#  "my_var" k name s us ko match kry gy neechy valy cases s q k match 
# case m hm variable ko match krty hn k agr varaible ki value 17 h to
#  tab kia krna h or agar 18 h to tab kia krna h; to yani k line 1 s 
# line 6 m yhi ho rha k agar my_var ki value "a" h to y print kr do vrna
#  agr "a" nhi to kuch case ko chor kr agly pr chaly jao


# y jo cases hn y actually patterns hn or in patterns ko ham literalls
#  kehty hn, y patterns "strings, booleans, numbers" ho skty hn such as 
# we can write (case True) or (case "nimra") or(case 1) etc etc.

#considering above code example
my_var = "a"
x=10
match my_var:
    case "a" if (x>10): #this means if my_var is equals to "a" and if x>10 then print("value is one"); {if (x>10) they are called gaurds}
        print("value is one") 
    case "b":
        print("value is two")


# for "or" you can use this
my_var = "a"
x=10
match my_var:
    case "a"|"b": 
        print("value is one") 
    case "b":
        print("value is two")

# _case
my_var = "a"
x=10
match my_var:
    case "a"|"b": 
        print("value is one") 
    case "b":
        print("value is two")
    case _ :
        print("none of above")


        # ***************practice example********************************
a=input("enter birthday year")
match a:
    case "jan":
        print("your birthday is in ",a," so your star is leo")
    case "feb":
        print("your birthday is is ",a," so your star is scorpion")
    case _:
        print("i don't know")

        # **********calculator***************

a=int(input("enter value of a"))
b=int(input("enter value of b"))
operation=input("enetr operation")
match operation:
    case "+":
        print("a+b = ", a+b)
    case "-":
        print("a-b = ", a-b)
    case "*":
        print("a*b = ", a*b)
    case "/":
        print("a/b = ", a/b)
    case _:
        print("enter any suitable operation")

