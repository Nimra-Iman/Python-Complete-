# agar koi function bht expensive h yani computationaly expensive means run hony k liye
# bhhttt time le rha e.g "10" value k liye us n almost 15 seconds liye, "5" value
# k liye almost 10 seconds liye, "7" k liye 14 seconds liye, yani bhhhttt time le rha
# h run hony k liye, ab jab doobara "10" value pas ki gi to hm nhi chahty k vo dubara
# 15 seconds le run hony k liye,,, to is liye hm caching krty hn,, caching y hota h
# k jo answer ek dfa kisi value k liye run ho kr ay vo answer save ho jay or phir
# dubara jab us value ko pass kia jay to function doobara s run na ho bal k 
# cached m store kia hua answer hi utha le, yani MEMOIZATION ho (MEMOIZATION means to
# store the result of computation so that it can be subsquently retrieved without 
# repeating the computation)

import time
from functools import lru_cache
@lru_cache(maxsize=None) #The maxsize parameter is used to specify the maximum number of
# results to cache. If maxsize is set to None, the cache will have an unlimited size.
def fun(n):
    time.sleep(3)
    return n*4

print(fun(5))
print("done with 5")
print(fun(51))
print("done with 51")
print(fun(2))
print("done with 2")

print(fun(5)) #ab yhan dubara "5" k liye itna nhi le ga bal k cached memory s answer 
# utha le ga q k function run hi nhi ho ga 
print("done with 5")

