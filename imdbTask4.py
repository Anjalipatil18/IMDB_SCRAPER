from imdbTask12 import*

def extract_data_from_imdb(movie_url):
    res=requests.get(movie_url)
    return BeautifulSoup(res.text,"html.parser")

dictionary={}
def extract_language_from_imdb(imdb_data):
    for i in range(1):
        try:
            sum_data=imdb_data.find("div",class_="article",id="titleDetails")
            data=sum_data.find_all("div",class_="txt-block")
            Language_list=[]
            for index in data[:5]:
                h4_data=index.find("h4",class_="inline").get_text()
                if h4_data == "Language:":
                    language=index.findAll("a")
                    for i in language:
                        lANGUAGES=i.get_text()
                        Language_list.append(lANGUAGES)
                if h4_data == "Country:":
                    country=index.a.get_text()
        except AttributeError: 
            continue
    dictionary["Languages"]=Language_list
    dictionary["country"]=country

def extract_director_from_imdb(imdb):
    bio_main_div=imdb.find("div",class_="plot_summary")
    bio_detail=bio_main_div.find("div",class_="summary_text").get_text().strip()  #The strip() method returns a copy of the string with both leading and trailing characters removed (based on the string argument passed).and remove for space
    director_detail=bio_main_div.find("div",class_="credit_summary_item")
    allDirector=director_detail.findAll("a")
    directorList=[]  
    for dir in allDirector:
        director=dir.get_text()
        directorList.append(director)    
    dictionary["director"]=directorList
    dictionary["bio"]=bio_detail
    
def extract_movie_heading_from_imdb(imdb):
    heading_detail=imdb.find("div",class_="title_wrapper")
    movie_name=heading_detail.h1.get_text()
    name_split=movie_name.split()   #The split() method splits a string into a list.
    name=" ".join(name_split[:-1])  #The join() is a string method which returns a string concatenated with the elements of an iterable.


    movie_runtimes=imdb.find("div",class_="subtext").time["datetime"]
    time=" "     
    for i in movie_runtimes:
        if i.isdigit():  #The isdigit() method returns True if all characters in a string are digits. If not, it returns False.
            time=time+i
    movie_runtime=int(time)
    
    allGenre=imdb.find("div",class_="subtext").findAll("a")
    allGenreList=[]
    for genre in allGenre[:-1]:
        movieGenre=genre.get_text()
        allGenreList.append(movieGenre)

    dictionary["genres"]=allGenreList
    dictionary["name"]=name
    dictionary["runtime"]=movie_runtime

def Scrap_Movie_Detail(movie_url):
    soup = extract_data_from_imdb(movie_url)  

    languagesAndcountry=extract_language_from_imdb(soup)

    all_headings=extract_movie_heading_from_imdb(soup)

    data_dict=extract_director_from_imdb(soup)

    movieCast=scrape_movie_cast(movie_url)

    poster_url=soup.find("div",class_="poster").img["src"]
    dictionary["poster_image_url"]=poster_url
    dictionary["cast"]=movieCast
    return dictionary
# movie_url="https://www.imdb.com/title/tt8108198/"
# particular_movie_detail=Scrap_Movie_Detail(movie_url)
# pprint(particular_movie_detail)
