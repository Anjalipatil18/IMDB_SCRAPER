from imdbTask9 import*

def castActorAndActressName(movies):
    actorAndActressName=[]
    for i in movies:
        movieOfCast=i["cast"]
        castUrlId=[]
        for index in movieOfCast:
            actorName=index["actorAndActressName"]
            actorAndActressName.append(actorName)
    return actorAndActressName
actorAndActressName=castActorAndActressName(movieDetailsWithCashing)

def duplicateActorAndActressName(movies):
    duplicateActressAndActorName=[]
    for index1 in range(len(movies)):
        if actorAndActressName[index1] not in duplicateActressAndActorName:
            duplicateActressAndActorName.append(actorAndActressName[index1])
    return duplicateActressAndActorName
duplicateActressAndActorName=duplicateActorAndActressName(actorAndActressName)

def castMovieUrlId(movies):
    castUrlId=[]
    for i in movies:
        movieOfCast=i["cast"]
        for index in movieOfCast:
            movieUrlId=index["imdbId"]
            castUrlId.append(movieUrlId)
    return castUrlId
movieCastUrlId=castMovieUrlId(movieDetailsWithCashing)

def duplicateCastUrlId(movies):
    duplicateCastMovieUrlId=[]
    for index1 in range(len(movies)):
        if movieCastUrlId[index1] not in duplicateCastMovieUrlId:
            duplicateCastMovieUrlId.append(movieCastUrlId[index1])
    return duplicateCastMovieUrlId
duplicateCastMovieUrlId=duplicateCastUrlId(movieCastUrlId)

dictionary={}
def analyse_actors():
    for i in range(0,(len(duplicateActressAndActorName))):
        count=0
        dict={}
        for j in actorAndActressName:
            if duplicateActressAndActorName[i] == j:
                count=count+1
        if count > 1:
            dict["name"]=duplicateActressAndActorName[i]
            dict["num_movies"]=count
            dictionary[duplicateCastMovieUrlId[i]]=dict
    return (dictionary)
countOfActorAndActress=analyse_actors()
# pprint(countOfActorAndActress)
