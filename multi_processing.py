# https://picsum.photos/200/300 #is url ko jab bhi upload kry gy, ek new image
#  generate ho gi
# import multiprocessing as mp
# import requests
# url="https://picsum.photos/200/300"
# def download(link,name):
#     print("started downlowding...")
#     r=requests.get(link) 
#     open(f"file_{name}.jpg", 'wb').write(r.content)
#     print("file downlowded...")
# def generate():
#     for i in range(4):
#         yield i
# if __name__=="__main__":

#     gen=generate()

#     t1= mp.Process(target=download, args=(url,next(gen)))
#     t2= mp.Process(target=download, args=(url,next(gen)))
#     t3= mp.Process(target=download, args=(url,next(gen)))

#     t1.start()
#     t2.start()
#     t3.start()

#     t1.join()
#     t2.join()
#     t3.join()

#     print("all files downloded")


# ----------------------------------  another way(obtaining return value)
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
import requests
urll="https://picsum.photos/200/300"
def download(link, name):
    print("start downloading...")
    r=requests.get(link)
    open(f"img {name}.jpg","wb") . write(r.content)
    return ("file downloaded")

li=[i for i in range(10)]
url=[]
for i in range(10):
    url.append(urll)

if __name__=="__main__":
    with ProcessPoolExecutor() as executor:
        r= executor.map(download, url, li)
        for j in r:
            print(j)

