# jab hm kisi module ko import krty hn to us k saary methods, functions or variables ko
# access kr skty hn; 
import math
print(math.sqrt(9))
print(math.pi)
# if i do it like that:
import math as m
print(m.sqrt(4))
# from keyword

from math import cos #is s math k poory module m s sirf cos hi import ho ga
print(cos(90))

from math import sqrt as s
print(s(4))

from math import * # is s y ho ga k ap ko jo bhi 
# method ya function use krna h ap ko math. nhi likhna pry ga, y bilkul bhi achi practice nhi h,
# q k agar esa ho k math module m bhi "pi" name ka function ho or koi or module ho us m 
# bhi "pi" nam ka function ho to compiler ko nhi pta lgy ga k kis module k "pi" ko uthana h
# q k uper dono modules ko import kia hua h yani: from math import * and from harry import *
print(pi)

import math
print("all functions and variables in math modules -->", dir(math))


#                BASICALLY HOW IMPORT WORKS
from import2 import harry,nimra
harry()
print(nimra)
            
import import2 as hr
hr.harry()
print(hr.nimra)



