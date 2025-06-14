
# !!!!!!!!!!!!!!!!!!  SHORT HAND IF ELSE  !!!!!!!!!!!!!!!!!!!!!!!!!!
# agar if and else m likha hua code ziada lines ka nhi h to code ko readable bnany k liye 
# short hand if else best hn
a=12
b=2
print("a") if (a>b) else print("=") if (a==b) else print("b")


kin = (input("enter your age"))
# >, <, >=, <=, ==, !=
if (int(kin) < 10):
  print("yoi can't drive")
else: 
  print("no0000")
a = input("enter num")
b = int(a)
print("entered number = ", b)
if (b > 18):
  print("you can drive ")
elif (b == 18):
  print("bro! you can drive but be cautious")
else:
  print("you cant drive")

# ********nested if**********
k = input("enter your numbers in maths")
b = int(k)
print(b)
if (b > 50):
  # print("yes bro! you are passed")
  if (b >= 90):
    print("excellent")
  elif (b >= 80):
    print("good")
  else:
    print("fair")
elif (b == 50):
  print("you are masssyyy pas")
else:
  print("you are fail")





a=int(input('enter a value between 2 and 9'))
# if (a<2 or a>9):
#   raise ValueError('entered nu,ber is wrong')
# else:
#   print('entered number is correct')

raise ValueError('number if wrong') if (a<2 or a>9) else print('ok')

