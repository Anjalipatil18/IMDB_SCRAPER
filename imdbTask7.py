from imdbTask9 import* 

def directorName(movies):
    directorList=[]
    for index in movies:
        directorList.extend(index["director"])
    return directorList
directorList=directorName(movieDetailsWithCashing)

def duplicateDirector(movies):
    duplicateDirector=[]
    for index1 in range(len(directorList)):
        if directorList[index1] not in duplicateDirector:
            duplicateDirector.append(directorList[index1])
    return duplicateDirector
duplicateDirector=duplicateDirector(movieDetailsWithCashing)

def analyse_movies_directors(movies):
        dict={}
        i=0
        while i<len(duplicateDirector):
            j=0
            count=0
            while j<len(directorList):
                if duplicateDirector[i] == directorList[j]:
                    count=count+1
                j=j+1
            dict[duplicateDirector[i]]=count
            i=i+1
        return (dict)
countingOfDirectors=analyse_movies_directors(movieDetailsWithCashing)
# pprint (countingOfDirectors)