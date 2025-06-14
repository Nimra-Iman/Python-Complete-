import requests
#   !!!!!!!!!!!  get request  !!!!!!!!!!!!!1
r=requests.get("https://www.codewithharry.com") #get request krny s diye gay link ka saara 
# HTML code mily ga
# print(r.text) #bht difficult tha smjhna, code beautify nhi tha

# pip install bs4
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser') #HTML KO PARSE KR RHYN HN(parsing means to convert
# to more readable form, yani saary tags such as div tag etc to ek structured format m show krti h)
print( soup.prettify()) #jo html code mila us ko beautify krny k liye y use kia, yani proper indentation etc daal kr neat bnati hn

for headings in soup.find_all("h2"): #yani m chahti hu k jo saara code mila us m s sirf
    # <h2> heading k ander likha hua text show kro(yani ap scraping kr rhy ho or jab bhi 
    # scarp krty hn to phly usy parse krna hota h hr haal m)
    
    # findall() method iterates over a string to find a subset of characters that match a
    # specified pattern. It will return a list of every pattern match that occurs in 
    # a given string.
    print(headings.text)



# !!!!!!!!!!!  post request  !!!!!!!!!!!!!!!!!!!
# By design, the POST request method requests that a web server accepts the data enclosed
# in the body of the request message, most likely for storing it. It is often used when
# uploading a file or when submitting a completed web form. In contrast, the HTTP GET 
# request method retrieves information from the server.

import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    "name" : "nimra",
    "age":20
}

# Send POST request with JSON data using the json parameter
response = requests.post(url, json=data)

# Print the response
print(response.text)




