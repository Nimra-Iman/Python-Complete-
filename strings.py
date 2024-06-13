print("he said,\"i wanna eat apple\"")

name = input("enter your name")
dialogue = """he said

i wanna eat

apple"""
print(name)
print(dialogue)
print("the first letter of your name = ", name[0]) #n
print("the second letter of your name = ", name[1]) #i
for character in dialogue:
  print(character) #it also considers new line and spaces 

#string length and string slicing
str = "mango"
print(len(str))
names = "nimra,iman,reruru"
print(names[0:5])  #0th index s le kr 4th index tak
print(
    names[-8:-1]
)  # 9-15(yhan indexes ki baat ho rhi yani vo 9th index s le kr 15th tk show kry ga)
# jab bhi negative slicing ki baat ho to ap string ki length m s us number ko minus kr do
name = "harry"
print(name[-4:-2])
a = "nimra"
a = "iman"
print(a)
# strings are immutable
print(len(a))
print(a.upper()) 

#************* important concept for interview****
a = "nimra"
print(a)
print(
    a.upper()
)  #kia y statement a="nimra" vali string ko upper case m convert kr de gi? to is ka answer ho ga k nhi kr skti q k strings are immutable, is statement "print(a.upper())" k zrye jo string ay gi vo ek new string ho gi , poorani vali string change nhi hui; yani string methods existing string pr operate krty hn or ek new string bnaty hn
a="nnnnnnimannnnnnnnnnnnnnn"
print(a.rstrip("n"))
#  'rstrip' function strips the character from right side and there is another command 'lstrips' which strips the character from left side and 'strip' function strips the character from anyside of the string
# upper(), lower(),len(),rstrip(),split(),center(),count(),find(),index(),endswith(), islanum(), isalpha(), islower(), isprintable(), isspace(), istitle(), isupper(), startwith(), swapcase(), title(),

a="55nimra Iman is Great555555"

print(a.isspace())
print(a.count("is"))
print(len(a))
print(a.upper())
print(a.lower())
print(a.capitalize()) #phla letter capital or baqi sary letters small krde ga 
print(a.rstrip("5"))
print(a.lstrip("5"))
print(a.strip("5"))
print(a.split("r"))
print(a.title())
print(a.endswith("t"))
print(a.endswith(" ",0,8)) #0th index s 7th index tak check kro k kia itna part
# " " yani space pr end ho rha h kia
print(a.isalnum()) #agar digits na bhi ay to bhi TRUE return kry ga yani
# A-Z or a-z or 0-9 hua yani in teeno m s koi ek bhi hua to true return ho ga
print(a.isalpha())
print(a.find("iman"))
print(a.find("rer")) #agar y cheez na mili to "-1" return kry ga
print(a.index("rer")) #agar y cheez na mili to "error" return kry ga  
print(a.startswith("a"))
print(a.swapcase())
print(a.isupper())
print(a.islower())
print(a.center(50,"*"))
print(a.center(50)) #itni spaces daal de ga agy peechy k total length 50 ho jay
print(len(a.center(50,"*")))
print(a.replace("nimra","kinza")) #replce all occurances
print(a.isprintable())
print(a.isspace())


# to find whether certain thing present in string or not:
if "nir" in "nimra":
    print("yes")
else:
    print("no")
# case 2
if "nim" in "nimra":
    print("yes")
else:
    print("no")




#     # to reverse a string
str="nimra"
print(str[::-1])
    # to remove only first letter of a string
str1="nimra is good"
print(str1[1:])
#    to get last letter of a string
str2="nimra"
print(str2[-1])