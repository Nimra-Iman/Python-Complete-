# important question for interview
# for and while loops k saath bhi else statement use hoskti h, jab for ya while ki saari
# iterations complete ho gy to else vali condition chaly gi, the programs exits the loop
#  only after else statement is executed
for i in range(3):
    print(i)
else:
    print("code is finished")

# another very imporatnt question
for i in range(5):
    print(i)
    if i==3:
        break  # ab is case m yha else statement nhi chaly gi, agar yha else chal prta
    #  to is ka matlab y hota k loop khatam hua h vo break nhi hua yani loop apni akhri
    # value tak gya, but yha loop akhri value tak nhi gya vo loop break hua , successfully
    # khatam nhi hua
else:
    print("code is finished")

# yhi case while loop k saath bhi ho skta h






