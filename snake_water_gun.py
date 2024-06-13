# gun kills snake so gun wins
# snake drinks water so snake wins
# guns drown in water so water wins

list=["snake","water","gun"]

attempts=int(input("how many attempts you wanna play?"))

import random

user_wins=0
comp_wins=0

i=1
while(attempts>=i):
    random_n=random.randint(0,2)
    random_c=list[random_n]
    print(random_c)
    
    user=input("enter s,w,g")
    if(user=="s" and random_c=="gun" ):
        print("you loss, gun(computer) wins")
        comp_wins=comp_wins+1
    elif(user=="g" and random_c=="snake" ):
        print("you win, snake(computer) loss")
        user_wins=user_wins+1

    elif(user=="w" and random_c=="snake"):
        print("you loss, snake(computer) wins")
        comp_wins=comp_wins+1
    elif(user=="s" and random_c=="water"):
        print("you win, water(computer) loss")
        user_wins=user_wins+1


    elif(user=="g" and random_c=="water"):
        print("you win, water(computer) loss")
        user_wins=user_wins+1
    elif(user=="w" and random_c=="gun"):
        print("you loss, gun(computer) wins")
        comp_wins=comp_wins+1

    elif((user=="s" and random_c=="snake") or (user=="w" and random_c=="water") or (user=="g" and random_c=="gun")):
        print("down")
    else:
        print("byee")
    i=i+1
print("game ends")
print("COMPUTER WINS",comp_wins,"TIMES")
print("YOU WINS",user_wins,"TIMES")
if(comp_wins>user_wins):
    print("*******  IN TOTAL: YOU LOSS  **************")
else:
    print("  *************  IN TOTAL: YOU WINS  *************")