# f-strings: very important , new feature developed in 3.6 versions
# f-strings are used to solve problems of file formating
#  It is also known as Literal String Interpolation or more
#  commonly as F-strings (f character preceding the string literal). 
# The primary focus of this mechanism is to make the interpolation easier.
# file formating:
str="my name is {} and i am fro {}"
name="nimra"
country="pak"
print(str.format(name,country))
# ab agr m y chahu k .format vali line likhty vqt m name and country ko us tarteem s na du
# jis tarteeb s uper str m show kiye huy h , yani k m is ko esy de du jesy neechy show kia h m n 
str="my name is {} and i am fro {}"
name="nimra"
country="pak"
print(str.format(country,name)) #to ab y name ko pak and country ko nimra consider kry ga 
# jo k ghalat ho ga , is msly ko hal krny k liye m esy kru gi, jesy neechy kia h
str="my name is {1} and i am fro {0}"
name="nimra"
country="pak"
print(str.format(country,name)) #yani country "0" pr h or name "1" pr h to m btana y chah rhi hu k 
# bracket{} m jha 1 likha h vha name a jay or jha {0} likha h vha country a jay 
# lekin bary projects m y bhhttt mushkil ho ga k {0} vala konca h , {1} vala kon ca h ,{2} vala kon ca h , yani gintay hi reh jao gy bas

# *************  USE FSTRINGS T0 SOLVE THESE ISSUES  *******************************
name="nimra"
country="pak"
str=f"my name is {name} and i am fro {country}" #yani ap direct varaiable daal skty ho
print(str)

# agar ham chahty hn k f string hony k bavajood hm y show key output m
# "my name is {name} and i am from {country}" to esy krna h : The f-string can be formatted in much same as the str.format() method.
name="nimra"
country="pak"
str=f"my name is {{name}} and i am fro {{country}}" #yani ap direct varaiable daal skty ho
print(str)
# aar esa show krna h "my name is {} and i am from {}"
str=f"my name is {{}} and i am fro {{}}" 
name="nimra"
country="pak"
print(str)


# ^^^^^^^^^^^^^^^^^^ practice questions  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Create a program that asks the user to enter their name and their age. Print
#  out a message addressed to them that tells them the year that they will turn
#  100 years old.

a=input("enter your name")
b=int(input("enter your age"))
birth_year=2023-b
v=birth_year + 100
str=print(f"you will become 100 years old in {v} my dear {a}")


#    ###########  OR  ###########  (this is valid for all years such as 2024,2025 and so on)
age=int(input("enter your age"))
from datetime import date
dat=date.today()
c_Year=int((dat.strftime("%Y")))
b_day=(c_Year - (age+1))
print(f"your date of birth= {b_day}")



# Write a program that calculates the area of a rectangle.
#  Prompt the user for the length and width, then display the result using an f-string.
a=int(input("enter length"))
b=int(input("enter width"))
c=a*b
print(f"area of rectangle = {c}")


# Develop a simple currency converter program. Ask the user for
#  an amount in USD and convert it to euros using a fixed conversion
#  rate. Display the result using an f-string.
a=int(input("enter $ "))
euros=a*0.94
print(f"{a} $ equals to {euros} euros")





