import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

def scrape_movie_cast(movie_caste_url):
    response=requests.get(movie_caste_url)
    soup=BeautifulSoup(response.text,"html.parser")
    table=soup.find("table",class_="cast_list")
    trs=table.find_all("tr")
    cast=[]
    for i in trs[1:]:
        try:
            tds=i.find_all("td")
            href=tds[1].a["href"]
            castUrl="https://www.imdb.com/"+href
            link=soup.find("div",class_="see-more")
            movieCastUrl=link.a["href"]
            moviecastLink=castUrl+movieCastUrl
            movieOfCastUrl=moviecastLink.split("/")
            imdbId=movieOfCastUrl[5]
            name=tds[1].a.get_text()
        except IndexError: 
            continue
        dict={}
        dict["imdbId"]=imdbId
        dict["actorAndActressName"]=name.strip( "  \n")
        cast.append(dict)
    return cast
# url="https://www.imdb.com/title/tt8108198/"
# castDataOfMovie=scrape_movie_cast(url)
# pprint(castDataOfMovie)