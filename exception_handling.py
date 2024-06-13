# agar try k ander kuch likha hua h or un lines of code m kuch error a gya to compiler
# forn s except k ander chla jay ga or phir except ko chalany k baad vo except k neechy vala
# code run krna start kr de ga

# NameError:    variable ko define kiye bagher us ko use krna
# SyntaxError:  if you write a wrong syntax
# TypeError:    it occured e.g when you want to sum string and integer
# Index errors: These occur when you try to access an element in a list
#                        or a string using an index that is out of bounds.
# Value errors: These occur when a built-in function receives an argument of
#                        the right type, but an inappropriate value.


# NameError us waqat ata h jab ap n us variable ko define hi nhi kia or use krny ki koshish kr rhy
try:
  print(x)  #NmaeError 
except:
  print("An exception occurred")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


try:
    lis=[1,2,3]
    print(lis[5])
except IndexError:
    print("index")
print("ok")
 
try:
  a=int(input("enter number")) #if someone give "nimra" as a number then valueerror raise
except ValueError:
  print("number is not integer")
print("end")


try:
  print(x)
except Exception as e:
  print(e)
print("nxty")




# practice questions:
attempts=0
num=55
try:
  while True:
      a=int(input("enter number"))
      if(a==num):
        print(f"congratulations won in {attempts} attempts")
        break
      elif(a>num):
        print("too high, print some lower")
        attempts=attempts+1
      else:
        print("too low print some more")
        attempts=attempts+1
except ValueError:
  print("entered number not integer")

# another practice
# a=int(input("enter a number"))  #y cheez yha nhi likhni, vrna except chaly ga hi nhi
try:
 a=int(input("enter a number"))
 for i in range(1,11):
    print(f"{a} x {i} = {a*i}")
except ValueError:
  print("value not integer")
except:
  print("sth. went wrong")
  

  
      


