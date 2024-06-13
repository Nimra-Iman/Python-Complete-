# There are several APIs available to convert text to speech in python. One of such
# APIs available in the python library commonly known as win32com library. It provides 
# a bunch of methods to get excited about and one of them is the Dispatch method of the
# library. Dispatch method when passed with the argument of SAPI.SpVoice It interacts
#  with the Microsoft Speech SDK to speak what you type in from the keyboard.



# win32com.client 
# pip install pypiwin32  (in order to import pwin32)

# import win32com.client   
# speaker = win32com.client.Dispatch("SAPI.SpVoice") 
  
# # list=["shoutout to nimra","shout out to me "] 
# list=["nimra","iman","kinza"]

# for i in list:
#     spe="shout out to " + i
#     print(spe)
#     speaker.Speak(spe) 

# CAN ALSO BE DONE LIKE THIS

# import win32com.client  
# speaker = win32com.client.Dispatch("SAPI.SpVoice") 
  
# # list=["shoutout to nimra","shout out to me "] 
# list=["nimra","iman","kinza"]
# spe=""
# for i in list:
#     spe=spe+ "shout out to " + i
# speaker.Speak(spe) 


#Ask user to enter text to convert it to speech
import win32com.client
speak=win32com.client.Dispatch("SAPI.spvoice")
input=input("enter text to convert it to sppech")
speak.Speak(input)