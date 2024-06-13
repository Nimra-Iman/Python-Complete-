# this is neither a type of multi-threading nor multi-processing. this is just a way of 
# how to concruntly execute your code

# TYPICAL EXECUTION OF FLOW IN PYTHON IS:
import time
def fun1():
    time.sleep(3)
    print("func 1")

def fun2():
    time.sleep(3)
    print("func 2")

def fun3():
    time.sleep(3)
    print("func 3")

fun1()
fun2()
fun3()#phly 3 secs k baad fun1 chla phr 3 secs k baad fun2 chla phir 3 secs k baad fun3 chla

# BASIC IDEA OF ASYNC PROGRAMMING
# let we have 3 functions f1(),f2() and f3(). f1() run ho rha tha but achanak us ko kisi
# cheez ki zrurt pri ya phir vo sleep pr chla gya to us time CPU khali pra h, hm vo time
# waste nhi kry gy bal k us time pr f2() ko ya shayad f3() ko bhi start kr den gy

import asyncio
# async def mai():
#     await fun() #yani jab tak fun() complete nhi ho jata, agy nhi vhlna
#     print("a")
#     await asyncio.sleep(1)
#     print("b")

# async def fun():
#     print("1")
#     await asyncio.sleep(3)
#     print("2")

# asyncio.run(mai()) #abhi tak jo code likha vo asal m asynchronus nhi h , y asal m 
# syncronous hi h but it is inside asyncronous function.,,,, asyncronous coding is 
# shown below:

async def main():
    task=asyncio.create_task(fun1()) #is ka matlab y h k fun1() ko shedule kr dia yani jab
    # bhi main() function m koi sleep aya ya y koi cheeze network s leny k liye gya
    # ya kisi bhi vja s y CPU idle stae m gya to fun1() execute hony lgy ga (agar main() m
    # sleep aya hi na ya main() k doran bilkul CPU idle gya hi nhi to main() complete
    # hony k baad fun1() execute krna start ho ga)
    print("a")
    await asyncio.sleep(1)
    print("b")
async def fun1():
    print("1")
    await asyncio.sleep(3)
    print("2")
asyncio.run(main()) #ab is code m phly hm n fun1() ko shedule kr dia yani agr main() m 
# kisi vja s CPU idle hua to fun1() start kry ga execute hona, is code m phly to "a" print
# ho ga because "a" s phly CPU idle state m nhi gya , phir CPU idle stae m gya q k 
# 1 second ka sleep aya to is time m fun1() start ho ga execute krna yani k "1" print
# ho ga then fun1() m agy ab 3 seconds ka sleep a gya or main() m to just 1 second
# ka sleep tha to control doobara main() k paas jay ga q k agar yha 3 seconds wait krny lgy
# yani CPU ko 3 seconds idle state m rkha to ghlat baat h, is liye control doobara main()
# m jay ga or "b" print kry ga then doobara fun1() m kr "2" print nhi kry ga bal k
# terminate kr jay ga main() function, vo prva nhi kry ga fun1() k sleep ki(*****).,,,, in case
# agr main() m 3seconds ka sleep ata or fun1() m 3 second s km ka sleep hota to phly 
# "a" print hot then fun1() m ja kr "1" print hota then CPU sleep krta phir "2" print
# hota then "b" pri t ho ka main() terminate krta 

# ab m jo (*****) vali baat boli k vo prva nhi kry ga fun1() k complete hony ka, jis ki
# vja s ek msla y bhi a skta h k agar print("2") vali line k baad fun1() kuch return 
# kr rha hota to vo return vali value bhi hm achieve na kr paty main() m, to is ka hal
# y h k hm fun1() ko bhi await krvayn main() m yani k main() tab tak terminate na ho jab 
# tak k fun1() complete nhi ho jata: like i shown in below code:

print("jdfiljlfjf")
async def main_1():
    task=asyncio.create_task(fun1_1()) 
    # return_value=await task #(!!!!)
    print("a")
    await asyncio.sleep(1)
    print("b")
    return_value=await task # yhan sab s end m likha k await kro ta k main() esy hi terminate
    # na ho jay phly hr haal m fun1_1() ko complete kry, agar #(!!!!) m likhy gyn to 
    # asynchronous ka faida hi nhi q k phir to hm y keh rhyn hn k phly fun1() complete
    # ho chahy kitni hi der lgy chahy kitni hi der CPU idle rhy, this is according to
    # condition of above code , code ki condition k according kia maloom ap ko
    # await #(!!!!) pr hi krvana pry
    print("the returned value is = ",return_value)
async def fun1_1():
    print("1")
    await asyncio.sleep(3)
    print("2")
    return 10
asyncio.run(main_1())



#  #kisi function ko shedule kiye bagher agar
#  hm n functions ko await kia hua h to jab tak vo function complete nhi ho ga doosra
#  nhi chly ga lekin agar kisi function ko shedule kia hua h or saath hi kisi or
#  function ko await bhi kia hua h to vo sheduled vala chal jay ga agar awaited function
#  ki execution k doran koi free time mila to,,,,,, lekin yaad rhy k rule y h k 
# CPU MUST BE IN LESS IDLE STATE, agar sheduled function jo k await function ki sleep 
# valy time m run ho rha h or us sheduled m bhi sleep a gya or vo sleep await valy
# sleep s ziada h to await vala hi continue rhy ga function, (agar sheduled ka or awaited
#  m sleep ka time equal h to await vala hi chly ga (@@@@CASE 3 @@@@)) lekin agar sheduled valy ka
# sleep kam h or await valy ka ziada h to sheduled valy m sleep ho kr thori c der vo sheduled
# valy ko continue kry ga or phir await valy m jay ga, like i shown below:
print("edeukqdofh")
async def main_11():
    task=asyncio.create_task(fun1_11())    
                                       # a 1 11 2 .... 22 b        (less idle state)
    print("a")
    await asyncio.sleep(1)
    await fun2()
    print("b")
    return_value=await task 
    print("the returned value is = ",return_value)
async def fun1_11():
    print("1")
    await asyncio.sleep(1)
    print("2")
    return 10
async def fun2():
    print("11")
    await asyncio.sleep(4)
    print("22")
asyncio.run(main_11())

# -------------------------------- ANOTHER CASE:

async def main_11():
    task=asyncio.create_task(fun1_11())    
                                       # a 1 11 . 22 b ....2       (less idle state)
    print("a")
    await asyncio.sleep(1)
    await fun2()
    print("b")
    return_value=await task 
    print("the returned value is = ",return_value)
async def fun1_11():
    print("1")
    await asyncio.sleep(4)
    print("2")
    return 10
async def fun2():
    print("11")
    await asyncio.sleep(1)
    print("22")
asyncio.run(main_11())


# ---------------------------ANOTHER CASE:
async def main_11():
    task=asyncio.create_task(fun1_11())    
                                       # a 11 1 . 22 b .... 2      (less idle state)
    print("a")
    await fun2()
    print("b")
    return_value=await task 
    print("the returned value is = ",return_value)
async def fun1_11():
    print("1")
    await asyncio.sleep(4)
    print("2")
    return 10
async def fun2():
    print("11")
    await asyncio.sleep(1)
    print("22")
asyncio.run(main_11())

# ------------------------------(@@@@CASE 3 @@@@))
async def f1():
    await asyncio.sleep(2)
    print("f1")
async def f2():
    await asyncio.sleep(2)
    print("f2")

async def main():
    task=asyncio.create_task(f1())
    await f2()
asyncio.run(main())

# another case in it:
async def main_11():
    task=asyncio.create_task(fu1_11())    
                                       # a 11 1 22 b 2     (less idle state)
    print("a")
    await fu2()
    print("b")
    return_value=await task 
    print("the returned value is = ",return_value)
async def fu1_11():
    print("1")
    await asyncio.sleep(1)
    print("2")
    return 10
async def fu2():
    print("11")
    await asyncio.sleep(1)
    print("22")
asyncio.run(main_11())


# !!!!!!!!!!!!!!!!!!! await asyncio.gather()  !!!!!!!!!!!!!!!!!!!
# agar hm chahty hn k hmary saary functions akathy chal pry:

import asyncio
async def fun1():
    print("1")
    await asyncio.sleep(2)
async def fun2():
    print("2")
    await asyncio.sleep(2)
async def fun3():
    print("3")
    await asyncio.sleep(2)

async def main():
    L=await asyncio.gather(
         fun1(),
         fun2(),
         fun3()
    )
    print(L)
asyncio.run( main()) #this is helpful in downloading all files simultaneously
