# for example mery pas ek file abc h or doosri xyz h , m n abc ko import kia xyz k
#  ander to import abc krty hi abc k saary k saary functions xyz m bhi execute ho jay gy,
#  chahy mujy un ki zroort ho ya na ho; e.g
import name2_equal_main
print(name2_equal_main.harry())

print(__name__)
# agar m n name_equal2 valy module m harry() ko call kia ho ga to is module ko import
# krty hi vo vala (yani harry vala function) function automatically yhan bhi chaly
# ga yani k agar us harry() valy m kuch esa code likha hota jo k system ki saari
# files kp delete kr deta or usi module m usi function ko call bhi kr dia jata
# or us module ko yha import krny s vo vala function automatically chalta or is system
# ki files bhi saari ki saari delete kr skta, which is a very serious issue,,
# agar vha likha hua code files na bhi delete krny vala hota bal k kuch or hota 
# phir bhi yha import krny s automatically run ho jata, which is also damaging, so
# is s bachny k liye hm __name__==__"main"__ ko use krty hn




#              IS IT NECASSARY TO WRITE __name__="__main__"
# agar ap ko lgta h k is file ko import kia ja skta h to phir to zroor lgao q k
# agar us file m koi critical function hua to ek import krny s hi ap k system ki saaarii
# files delete bhi ho skti h



# IN SIMPLE WORDS: means each file has name = main if it is executed directly. we write
#  this code print(__name__), we will see the output as __main__, but when we import the
#  same function in a sepratae python file, we will see that print(__name__) will provide 
# the name of the python file in which this function is executed. means, in simple terms,
#  the name remain main unless it is not imported, but when we import a file or some 
# functions of this file, the __name__ of the file that is imported will
#  become 'file name' instead of __main__, or is trah conditon false ho gi, yani 
# ab _name_ main k equal nhi h, is liye function bhi automatic executaion s bacha 
# rhy ga


# 🧠 Final correct understanding (rewritten properly)

# Each Python file has its own __name__.
# Only the file that is executed directly gets __name__ == "__main__".
# When a file is imported, its __name__ becomes the file name, not __main__.
# Because of this, code inside
# if __name__ == "__main__":
# does not execute automatically when the file is imported
