q=['''WHAT IS CAPITAL OF PAKISTAN?
      a)Karachi          b)Lahore
      c)SGD              d)ISL ''', 
    '''WHAT IS CAPITAL OF INDIA?
      a)DELHI          b)LUKNAO
      c)PUNJAB         d)NO IDEA ''',
    '''WHAT IS CAPITAL OF CHINA?
      a)CHICAGO          b)BERLIN
      c)CHEEN_CAPI       d)NONE ''' ]

a = ['ISL','DELHI','NONE']
count = 0
while True:
    if (input('you wanna play? Y/N') == 'Y'):
        print("let's start")
        for i in range(len(q)):
            print(q[i])
            answer = input(' --------------enter your answer -------------')
            if (answer == a[i]):
                print(' ------------  CORRECT ***************')
                count = count+1000
            else:
                print('LOST MONEY ((((((((((((((((()))))))))))))))))')
            print(f'total money till now = {count}', count )
        print('total money you will get home = ', count)
    else:
        break











