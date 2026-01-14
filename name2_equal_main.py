def harry():
    print("this is function body ")
    print('inside function NAME IS ', __name__)
# # harry()
print('this is from name2_equal_main')
print(__name__)
if(__name__ =="__main__"):
    harry()
    
# is __name__ ka matlab h k y kha s print ho rha h , agar is ki output __main__ ati h to
# is ka matlab y hua k y isi file s hi print ho rha h but agar is ki output is file ka
# name ati yani name_equal2 ati to is ka matlab y tha k is module ko import kia gia h
#  

# is file s name=main hta kr dekho or phir name_equal_main.py m import kro is
#  module ko (yani name2_equal_main)
# just import kro and you will see k harry vali output show ho gi, although 
# hm n harry ko call kia hi nhi
