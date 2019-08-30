# webscrapping is a extract the data any website
# indian top movies by web scrapping from imdp website extract the data

from bs4 import BeautifulSoup  #bs4 is a package and beautifulsoup is python library
import requests  # Requests will allow you to send https requests.It allows you to access the response data of python in the same way.
from pprint import pprint # pprint used for makes our code beautiful.
import json  #json used for perform some methods on dictionay/json string(loads,dumps).

movieNames=[]
movieYears=[]
movieLinks=[]
movieRatings=[]

url="https://www.imdb.com/india/top-rated-indian-movies/"  #imdb api
response=requests.get(url)  #get the data from imdb api
movieData=response.text     #this data is html format
soup = BeautifulSoup(movieData,"html.parser") #parser is convert the data html and xml
tbody=soup.find("tbody",class_="lister-list")
trs=tbody.find_all("tr")

def scrape_top_list(moviesDetails):
    for index in trs:
        name=index.find("td",class_="titleColumn").a.get_text()
        movieNames.append(name) 
        year=index.find("td",class_="titleColumn").span.get_text()
        movieYears.append(year)
        url=index.find("a")["href"]
        moviesOfUrl="https://www.imdb.com"+url
        movieLinks.append(moviesOfUrl)
        rating=index.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movieRatings.append(rating)
    movies=[]
    for index1 in range(0,len(movieRatings)):
        movieDetails={}
        movieDetails["position"]=index1+1
        movieDetails["movieName"]=movieNames[index1]
        movieDetails["movieYear"]=int(movieYears[index1][1:5])
        movieDetails["movieLink"]=movieLinks[index1]
        movieDetails["movieRating"]=float(movieRatings[index1])
        movies.append(movieDetails) 
    return movies   
movieInfo=scrape_top_list(trs)
# pprint(movieInfo)