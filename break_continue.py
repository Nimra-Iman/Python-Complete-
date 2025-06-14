# breaking out of loop(yani  break s loop k baher, 
# break khy ga k loop ko chor kr nikal jao)
# break s ham loop k baher a jaty hn but continue s ham lo
#  sirf ek iteration ko khatam kr dety hn yani agr hm chahty hn k 10th 
# iteration perform na
# ho to ham continue ko use kry gy

# case 1 with break
for i in range(11):
    print("5 x",i,"=", i*5)
    if (i==3):
        break #yha pr vo 3 tak jay ga or us k baad chory ga

# case 2 with break
for i in range(11):
    if (i==3):
        break # yha pr vo 3 tak jay ga hi nhi phly hi loop ko chor de ga 
    print("5 x",i,"=", i*5) 
    

print("continue")
# continue
for i in range(11):
    if (i==3):
        print("5 ko 3 s multipy na kro")
        continue
    print("5 x",i,"=", i*5)

# sort function
list = [2,5,8,1,3,4]
list.sort()
print(list)

print('start yha s hio rha h ')
# breaks in nested loops(example 1)
list = ["nimra","iman","rer","kin","kinza"]
for items in list:
    print (items)
    for a in items:
         print(a)
         if(a=="r"):
            break
         
# # example 2 (more easy)
# for i in range(1,4):
#     for j in range(1,4):
#         if(i==j):
#             break
#         print(i,j) # nested loop m jab neechy vali loop m ham break lgaty
        # hn to us loop(yani neechy vali) ki saari iterations khatam ho jaty 
        # hn or forn hi loop uper vali pr vapis shift ho kar iteration restart krti h 
         
# # case 2
# list = ["nimra","iman","rer","kin","kinza"]
# for items in list:
#     print (items)
#     if(items =="iman"):
#         break
#     for a in items:
#          print(a)
# print("bas")

# # example 2 easy
# for i in range(1,4):
#     if(i==3):
#         break
#     for j in range(1,4):
#         print(i,j)


    
# # nested loop with continue
# for i in range(1,4):
#     for j in range(1,4):
#         if(i==j):
#             continue
#         print(i,j) 



          
        
            
        

            
       



    
    