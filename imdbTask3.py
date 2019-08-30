from imdbTask1 import*
from imdbTask2  import*

def group_by_decade():
    i=0
    decadeMovieDetails={}
    while i<len(sortYearOfMovie):
        decadeYear=[]
        decade=sortYearOfMovie[i]%10
        decades=sortYearOfMovie[i]-decade
        rangeYear=decades+10
        for index in range(decades,rangeYear):
            if index in sortYearOfMovie:
                decadeYear.append(movieYearOfList[index])
        decadeMovieDetails[decades]=decadeYear
        i=i+1
    return decadeMovieDetails
MovieOfdecadeYear=group_by_decade()
# pprint(MovieOfdecadeYear)