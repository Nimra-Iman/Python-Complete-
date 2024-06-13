Q=['''WHAT IS CAPITAL OF PAKISTAN?
      a)Karachi          b)Lahore
      c)SGD              d)ISL ''', 
    '''WHAT IS CAPITAL OF INDIA?
      a)DELHI          b)LUKNAO
      c)PUNJAB         d)NO IDEA ''',
    '''WHAT IS CAPITAL OF CHINA?
      a)CHICAGO          b)BERLIN
      c)CHEEN_CAPI       d)NONE ''' ]

a=["isl", "delhi","none"]
m=[1000,2000,3000]
money=0
choice=input("You Wanna Play?  (Y/N)")
if(choice=="y"):
    for i in range(len(Q)):
        print("Question for rupees",m[i],"is\n",Q[i])
        ans=input("****  TYPE ANSWER  ****")
        if(ans==a[i]):
            money=money+m[i]
            print("Congratulations! you won ",m[i],"$")
            print("TOTAL MONEY YOU WILL GET BACK HOME=", money)
        else:
            print("oops! you lose money of this Question, the total money that you will get back home=", money)
        
        if(i<2):
            choose=input("press 'C' to continue and 'E' to exit ")
            if(choose=="E" or choose=="e"):
                 print("OK! TOTAL MONEY YOU WILL GET BACK HOME=", money)
                 break
            elif(choose=="C" or choose=="c"):
               print("OK! MOVE TO THE NEXT")
      
else:
    print("well, it's your choice , Bye!")


