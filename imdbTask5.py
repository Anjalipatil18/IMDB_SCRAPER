from imdbTask1 import*
from imdbTask4 import*

def get_movie_list_details(api):
    movieListDetails=[]
    for i in api[:10]:
        link=i["movieLink"]
        movieUrl=Scrap_Movie_Detail(link)
        new=movieUrl.copy()   #They copy() method returns a shallow copy of the dictionary.
        movieUrl.clear()      #The clear() method removes all items from the dictionary.
        movieListDetails.append(new)
    return movieListDetails
movieOfDetails=get_movie_list_details(movieInfo)
# pprint(movieOfDetails)
