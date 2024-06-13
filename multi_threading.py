# # yani things ko parallely krna, agar 50 files download krni h to esa nhi krna k ek ek kr k
# # download kro bal k 50 ki 50 ko akathi downloading pr lgana and this is acheived via 
# # multi_threading
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# # tim1=time.perf_counter()
# # def fun1(secs):
# #     print(f"waiting for {secs} seconds")
# #     time.sleep(secs)
# # fun1(2)
# # fun1(3)
# # fun1(5)
# # tim2=time.perf_counter()
# # total_time=tim2-tim1
# # print(f"total time taken in case of single threading is {total_time} seconds")

# # if we do above code with multi threading, our time will reduced heraankun
# tim1=time.perf_counter()
# def fun1(secs):
#     print(f"waiting for {secs} seconds")
#     time.sleep(secs)

# t1=threading.Thread(target=fun1, args=[2])
# t2=threading.Thread(target=fun1, args=[3])
# t3=threading.Thread(target=fun1, args=[5]) #esa krny s hm n threads bna liye but in ko an start
# # krna h yani cars khari hn ab start kro bas
# t1.start()
# t2.start()
# t3.start()
# tim2=time.perf_counter()
# total_time=tim2-tim1
# print(f"total time taken in case of multi threading is {total_time} seconds") #0.00 seconds
# # ab swal y bnta h k sab s slow process 5seconds ka h yani total time kam s kam 5seconds to 
# # lgna chahye tha q k misal k tor pr agar 3 log khana bna rhy hn rk bhindi bna rha us ko
# # 5 minute lgy, ek roti bna rha us ko 3 minte lgy or ek raita bna rka us ko 2 minute lgy to
# # khana total 5 minute m tyar ho ga , to yhan bhi time km s km 5 seconds to lgny chahye 
# # but yha 0.00 seconds q lg rhy? to is ka jvab y hota h k t1.start() likhny ka matlab
# # sirf process start kr do or agy chlo (yani process complete nhi hua sirf start hua h),
# #  phir khud hi process complete hota rhy ga, agar hm
# # chahty hn k vo process complete bhi ho or phir agy chly to hm t.join() likhy gy, vo bhi
# # t3.start() k neechy, agar hm t1.start() m k neechy hi likh den gy to phir multi_threading
# # ka faida hi nhi: below is updated above code:
# # print
# print("hdkh")
# tim1=time.perf_counter()
# def fun1(secs):
#     print(f"waiting for {secs} seconds")
#     time.sleep(secs)
#     return ("done")

# t1=threading.Thread(target=fun1, args=[2])
# t2=threading.Thread(target=fun1, args=[3])
# t3=threading.Thread(target=fun1, args=[5])
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# tim2=time.perf_counter()
# total_time=tim2-tim1
# print(f"total time taken in case of multi threading is {total_time} seconds") #y code 
# # likhny s esa ho ga k agar un functions n kuch return kia to hmy return vali value nhi
# # mily gi, or hm chahty hn k return bhi mily to hm "threadpoolexecutor" ko use kry gy


def fun1(secs):
    print(f"waiting for {secs} seconds")
    time.sleep(secs)
    return ("done")
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1= executor.submit(fun1, 2)
        future2= executor.submit(fun1, 3)
        future3= executor.submit(fun1, 5)
        print(future1.result())
        print(future2.result())
        print(future3.result()) #start saary akathy hun gy phir jesy jesy complete hoty rhyn 
        # gy result milta rhy ga 
# poolingDemo() #esy code likhny s code lmba ho jay ga agar 500 files download krni hn
# to 500 dfa esy likhna pry ga , is liye hm map() ka use krty hn


with ThreadPoolExecutor() as executor:
    l = [3, 5, 1, 2] #y list bta rhi h k phly function ki input 3 h, doosry ki 5 and so on
    results = executor.map(fun1, l) 
    for result in results:
        print(result)


# PRACTICE USE CASE:
url1= "https://media.istockphoto.com/id/1496615469/photo/serene-latin-woman-enjoy-sunset-with-gratitude.jpg?s=1024x1024&w=is&k=20&c=Boo17hpiJy-am_I4CSMRALI5tPRtTZKrVp2RHlI4wQw="
url2= "https://media.istockphoto.com/id/1193158640/photo/beautiful-young-woman-is-listening-to-music-on-headphones.jpg?s=1024x1024&w=is&k=20&c=1WkSKL0g5Jth4J8hNB2q7iZk4j2ZVz-ea-1fGlAPmGw="
url3="https://media.istockphoto.com/id/1047795840/photo/a-woman-in-the-sunlight-rejoices-in-life.jpg?s=1024x1024&w=is&k=20&c=5Aic0EXJwwPPoE_RpxfvcrEa7-tYcl0_-3gMy80qZho="

import os
import re
from concurrent.futures import ThreadPoolExecutor
import requests
def download(input_url):
    print("start")
    r=requests.get(input_url)
    n=os.path.basename(input_url)  # This method internally use os.path.split() method
    # to split the specified path into a pair (head, tail). e.g: path = '/home/User/Documents'
    # Above specified path will be splitted into (head, tail) pair as ('/home/User', 'Documents')
    name=n.split(".")[0]
    pattern="\-"
    text=name
    file_name=re.sub(pattern, "_", text)
    open(f"{file_name}.jpg", 'wb').write(r.content)
    return (f"done download")
list=[url1,url2,url3]
def fu():
    with ThreadPoolExecutor() as executor:
        results=executor.map(download, list)
        for result in results:
            print(result)

fu()


