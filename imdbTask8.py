import os.path
from imdbTask1 import*
from imdbTask4 import*


def withCashingScrapeMovieDetails():
    allMovieData=[]
    for i in movieInfo:
        movieUrl=i["movieLink"]
        id=movieUrl.split("/")
        urlId=id[4]
        filename="urlId/"+urlId+".json"
        if os.path.exists(filename):
            idJsonFile=open(filename,"r")
            data=idJsonFile.read()
            dictData=json.loads(data)
            allMovieData.append(dictData)
        else:
            movieUrl1=Scrap_Movie_Detail(movieUrl)
            writeFile=open(filename,"w")
            stringData=json.dumps(movieUrl1)
            writeFile.write(stringData)
            writeFile.close()
    return(allMovieData)
cashingData=withCashingScrapeMovieDetails()
# pprint (cashingData)