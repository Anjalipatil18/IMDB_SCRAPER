from imdbTask9 import* 
def analyse_movies_language(moviesDetails):
        genreList=[]
        for index in moviesDetails:
            genreList.extend(index["genres"])
        duplicatedGenre=[]
        for index1 in range(len(genreList)):
            if genreList[index1] not in duplicatedGenre:
                duplicatedGenre.append(genreList[index1])
        dict={}
        i=0
        while i<len(duplicatedGenre):
            j=0
            count=0
            while j<len(genreList):
                if duplicatedGenre[i] == genreList[j]:
                    count=count+1
                j=j+1
            dict[duplicatedGenre[i]]=count
            i=i+1
        return (dict)
countingOfGenre=analyse_movies_language(movieDetailsWithCashing)
# pprint(countingOfGenre)