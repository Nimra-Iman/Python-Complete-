import time
#  !!!!!!!!!!!!!!!!!  time.sleep()  !!!!!!!!!!!!!!!!!!!!!!!
print("nimra")
time.sleep(3) # is line s phly jitna code likha tha vo chly ga or phir 3 seconds
# ka pause ay ga or phir agy vala code chly ga 
print("this is printing after 3 seconds")

#  !!!!!!!!!!!!!!! time.time()  !!!!!!!!!!!!!!!!!!!!!!!!!
# time.time() return the current time in seconds since the Epoch. yani 1st JANuary 1970
# m jab y module bna tha to us vqt s le kr ab tak jitny seconds guzray to time.time() vo
# seconds show kry ga
def forloop():
    for i in range(500):
        print(i)
def whileloop():
    i=0
    while(i<=500):
        print(i)
        i=i+1

time_before_running_for_loop=time.time()
forloop()
time_took_by_this_forloop=time.time()-time_before_running_for_loop

time_before_running_while_loop=time.time()
whileloop()
time_took_by_this_whileloop=time.time()-time_before_running_while_loop
print("time taken by for loop is = ",time_took_by_this_forloop)
print("time taken by while loop is = ",time_took_by_this_whileloop)


#  !!!!!!!!!!!!!!!!!!!!!! time.localtime() and time.strftime()  !!!!!!!!!!!!!!!!!!!!!!!
print("today's date and current time is ")
t=time.localtime()
formatted_time=time.strftime("%d-%m-%y %H:%M:%S",t) #format esa hi likhna vrna answer ghla ay ga
print(formatted_time)
