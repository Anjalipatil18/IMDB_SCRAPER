# bs4 is a package and beautifulsoup is python library
from bs4 import BeautifulSoup 
# Requests will allow you to send https requests.It allows you to access the response data of python in the same way.
import requests 
# pprint used for makes our code beautiful.
from pprint import pprint
# json used for perform some methods on dictionay/json string(loads,dumps).
import json

url="https://www.giveindia.org/certified-indian-ngos"
response=requests.get(url)
# print response.text
soup=BeautifulSoup(response.text,"html5lib")
# print soup
div=soup.find("div",class_="container")
# print div
name=soup.find("div",class_="d-flex f-d-col w-100 p-0 container")
# print name

NgoList=[]
dictionary={}
for i in name:
    names=i.find_all("div",class_="d-flex f-d-col col-10 col-sm-10")
    # print names
    for index in names:
        NgoName=index.h5.get_text()
        # print NgoName

        Ngocause=index.span.get_text()
        s=Ngocause.split("|")
        cause=s[0]
        # print cause
        state=s[1]
        # print NgoState
        dictionary["NgoName"]=NgoName
        dictionary["Ngocause"]=cause
        dictionary["NgoState"]=state
        NgoList.append(dictionary)
pprint (NgoList)

    



