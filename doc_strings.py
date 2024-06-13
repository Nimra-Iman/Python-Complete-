# VIP Q

# doc string : y helpful hoty hn functions ko understand krny k liye yani agr hm kuch esa chahy k 
# function k saath saath hmy us ki discrpition bhi mil
#  jay to kitna acha ho, so: dos_strings isi k liye user hoti hn
# doc strings ko hm sirf function k liye hi nhi bal k classes, modules, methods k liye bhi
#  use krty hn doc strings comments nhi hoty ; in ko hum ya to right after function
#  definition ya right above function body show krty hn , just like below:
def add (a,b):
    '''this function add two variables and return value''' #agar hm is line ko body k
    # neechy likh dety to is print(add.__doc__) ki output hmy "none" milti q k 
    # doc_string ko sirf hm 
    # right after function definition hi likhty hn
    return(a+b)
c=add(3,2)
print(c)
# ab agr hm is function ki discrition bhi chahty hn, yani k doc string k ander
# jo kuch likha h vo show ho jay to hm esy kry gy
print(add.__doc__) # y line show krti h k doc string comments nhi hn, agr y 
# comments hota to interpreter totally ignore ke deta comment ko, lekin y code
# ki line 13 likhny s us n hmy doc string show kr di



# ^^^^^^^^^^^^^^^^^^^^^^^^^^  PEP 8  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# pep(python enhancement proposal) was develeoped in 2001. it is a document that describes
#  different new features for python. the purpose of pep is to make your program readable, 
# maintainable and consistent. there are several types of pep 8. or y basically btata h k 
# kis trah ap ka python code behtreen likha jay, yani ap ko different rules btay ga
#  jesy "TABS USE KRY YA SPACES KO USE KIA JAY INDENTATION K LIYE? " to is ki explaination
# PEP8 m esy likhi hui h:

# Tabs or Spaces?
# Spaces are the preferred indentation method.

# Tabs should be used solely to remain consistent with code that is already indented with tabs.

# Python disallows mixing tabs and spaces for indentation.


# ^^^^^^^^^^^^^^^^^^^^^^^^  ZEN OF PYTHON  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Agr ap powelshell m ya python m "import this" to is s ZEN OF PYTHON show hota h 
# y basically ek poem h 
import this
# or import this yani zen of python ka esa koi use nhi h

