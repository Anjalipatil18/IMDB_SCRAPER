from imdbTask4 import*
from imdbTask12 import*
from imdbTask1 import*

movie_url="https://www.imdb.com/title/tt8108198/"
movieDetailsCast=[]
def scrape_movie_cast_and_details(movie_caste_url):
        for index in movie_caste_url[:4]:
                url=index["movieLink"]
                movieDetails=Scrap_Movie_Detail(url)
                movieCast=scrape_movie_cast(url)
                movieDetails["cast"]= movieCast
                new=movieDetails.copy()
                movieDetails.clear()
                movieDetailsCast.append(new)
        return (movieDetailsCast)
allMovieDetails=scrape_movie_cast_and_details(movieInfo)
# pprint(allMovieDetails)