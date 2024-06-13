# finally--> most asked question in interview
# chahy try or except m s jo kuch bhi chaly but finally k 
# ander likha hua har haaal m chaly ga
try:
    print(x)
except NameError:
    print("x not defined")
finally:
    print("always executed")
 
# is code m finally m jo likha h vo finally k bagher likhti to bhi chal jata to is
# ka matlab y nhi k finally bekaar h , finally ka main kaam functions m hota h 
# jab ham function ko return kr dety hn to return statement k neechy likha hua 
# kuch print nhi hota q k interpreter ko to kha gya k return ho jao , to is condition 
# finally m likha hua zroor chaly ga chahy vo return statement k baad bhi q na likha ho
print("yha s")
def sum(a,b):
    try:
        print(a+b)
        return 1
    except ValueError:
        return 0
    finally:
        print("always executed")
x=sum(2,3)
print(x)

  




