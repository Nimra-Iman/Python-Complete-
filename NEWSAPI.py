import requests
# from bs4 import BeautifulSoup #this is used for parsing html content, now content is
# in json, so we will used json library (what us meant by data is in json,,, read json.txt
# file in this folder)
import json
mulk=int(input('''press 
           1 for INDIA
           2 for GERMANY
           3 FOR TURKEY'''))
if(mulk==1):
    type=int(input('''CATRAGORY OF LATEST NEWS:
               1 for BUSINESS
               2 for ENTERTAINMENT
               3 for HEALTH'''))
    if(type==1):
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=8971448737974f728c098ccd4909d879")
        parsed_data=( json.loads(r.text))
        data=str(parsed_data)
        total_news=(data.count("title"))
        print( "THE TOTAL TODAY'S NEWS are : ", total_news)
        print(" ======>>> ALL HEADLINES ARE SHOWN BELOW: ")
        for i in range(total_news):
            print(F"HEADLINE  {i}   :    f{parsed_data["articles"][i]["title"]}")
        
        full_news=int(input("PRESS THE KEY OF A HEADLINE TO GET FULL NEWS!"))
        print(f"  THE URL IS : {parsed_data["articles"][full_news]["url"]}")
        
    elif(type==2):
        re=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=8971448737974f728c098ccd4909d879")
        parsed_data=(json.loads(re.text))
        data=str(parsed_data)
        total_news=data.count("title")
        print(f"THE TOTAL NEWS IS = ",total_news)
        print("=====>>>>  ALL HEADINGS ARE SHOWN BELOW:")
        for i in range(total_news):
            print(f"HEADLINE {i} : {parsed_data["articles"][i]["title"]}")
        full_news=int(input("ENTER THE KEY OF HEADLINE TO GET THE LINK OF FULL NEWS"))
        print(f"THE URL IS : {parsed_data["articles"][full_news]["url"]}")

    elif(type==3):
        re=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=8971448737974f728c098ccd4909d879")
        parsed_data=(json.loads(re.text))
        data=str(parsed_data)
        total_news=data.count("title")
        print(f"THE TOTAL NEWS IS = ",total_news)
        print("=====>>>>  ALL HEADINGS ARE SHOWN BELOW:")
        for i in range(total_news):
            print(f"HEADLINE {i} : {parsed_data["articles"][i]["title"]}")
        full_news=int(input("ENTER THE KEY OF HEADLINE TO GET THE LINK OF FULL NEWS"))
        print(f"THE URL IS : {parsed_data["articles"][full_news]["url"]}")


    

