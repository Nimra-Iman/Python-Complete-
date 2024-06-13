from plyer import notification #pip install plyer
import time
import win32com.client
# NOTIFICATION WILL SHOW AFTER EVERY TWO HOURS TO DRINK WATER
while True:  # while True ka use good practice nhi h, use "TASK SHEDULER" in windows
    time.sleep(7200) 
    sp=win32com.client.Dispatch("SAPI.SpVoice")
    sp.Speak("DRINK WATER DEAR!")
    notification.notify(
        title= "DRINK WATER DEAR! ",
        message= "It is a healthy practice to drink water because it is good for your skin",
        timeout=5 #means display it for 5 seconds
    )

