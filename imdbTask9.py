from imdbTask1 import*
from imdbTask4 import*
import random
import time
import os.path

def get_movie_list_details_with_cashing(api):
    getDetails=[]
    for i in api:
        movieUrl=i["movieLink"]
        id=movieUrl.split("/")
        urlId=id[4]
        filename="cashingFolder/"+urlId+".json"
        if os.path.exists(filename):
            idJsonFile=open(filename,"r")
            data=idJsonFile.read()
            dictData=json.loads(data)
            getDetails.append(dictData)
        else:
            movieUrl1=Scrap_Movie_Detail(movieUrl)
            writeFile=open(filename,"w")
            stringData=json.dumps(movieUrl1)
            writeFile.write(stringData)
            timeLimit=random.randint(1,3)
            time.sleep(timeLimit)
            writeFile.close()
    return getDetails
movieDetailsWithCashing=get_movie_list_details_with_cashing(movieInfo)
# pprint(movieDetailsWithCashing)
# print len(movieDetailsWithCashing)
