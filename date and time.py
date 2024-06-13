# from datetime import date
# date=(date.today())
# print(date)
# print(date.strftime("%d/%m/%y"))
# print(date.strftime("%d-%B-%y"))

# from datetime import datetime
# # print("date and time now is " , datetime.now())
# dateTime=datetime.now()
# print(dateTime.strftime("%d/%m/%Y, %H:%M:%S"))

from datetime import date
date=date.today()
print("today's date is = ", date.strftime("%d %B %Y"))
from datetime import datetime
dateTime=datetime.now()
t=dateTime.strftime("%H ")
print("time now = ", t)
int_t=int(t)
if ( int_t <=12 ):
    print("GOOD MORNING")
elif(int_t>=13 and int_t<=15):
    print("GOOD NOON")
else:
    print("GOOD NIGHT")
