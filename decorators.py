# decorator ek function h jo k ek doosra function leta h or us ko thora bht chnage
#  kr k return kr deta h 

# e.g if i want jo bhi function run ho vo phly "good morning" or end m "thanks for using"
# print kry, y kaam m us function ko directly edit kr k bhi kr skti hu buit if 150 
# functions hyu to hr ek ek function k saath esa krna bht mushkil ho jay ga, that's
# why decorators are used


def greet(non_edited_fun):
    def edited_fun():
        print("good morning")
        non_edited_fun()
        print("thanks for using")
    return edited_fun

@greet
def helo():
    print("welcome to world")
helo() 

#agar m is helo function ko likhny s phly @greet na likhu to m esy bhi kr skti hu:
# greet(helo)() #is ka matab y h k "greet" ko "helo" fun pass krvao or phir is ko
# run kr do

# ab tak jo kia vo un functions k liye hn jin m arguments nhi hoty, lekin agar arguments
# hu to esy krna h

def greet(non_edited):
    def edited(*args, **kwargs):
        print("good nmorning\n")
        non_edited(*args, **kwargs)
        print("\nthank you")
    return edited

# The *args parameter allows your decorator to accept any number of positional arguments,
#  **kwargs parameter allows it to accept any number of keyword arguments.

@greet
def add(a,b):
    print(a+b)
add(b=2,a=4)  
# greet(add)(2,3) #0R call like this:

# it is better to write both *args and **kwargs because hm decorators ko ofcourse
# ek s ziada functions pr use krny valy hn , kuch functions m positional arguments
# ko pass kia ja rha ho ga or kuch m key word arguments pas kiye ja rhy hu gy,
# to is liye best yhi h k *args and **kwargs fono likho ta sab functions k liye
# decorator run ho sky