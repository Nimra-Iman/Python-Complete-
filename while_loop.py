i=0
while(i<3):
    print(i)
    i=i+1
print("done with loop")

# use of else with while loop
n=5
while(n>0):
    print(n)
    n=n-1
else:
    print("i am in else statement ") # yani agar while na chla ya while
    # chal kr mukammal ho gya to else vali condition chal jay gi


 # VIP QUSTION BELOW::::::::::::
    # emaluating do while loop(q k python m do while loop nhi 
    # hoti to is line ka matlb y hua k while loop ko is trah modify krna k vo
    # do while ki trah kaam kry )
    # do while also called  exit-controlled loop.

    # The most common technique to emulate a do-while loop in Python is to use
    # an infinite while loop with a break statement wrapped in an if statement
    #  that checks a given condition and breaks the iteration if that condition 
    #  becomes true:

while True: #is s y infinite loop bn jay gi
    number=int(input("enter number"))
    print(number)
    if(not number  > 0):
        break
    


