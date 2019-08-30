from imdbTask9 import* 

def analyse_movies_language(moviesDetails):
        languageList=[]
        for index in moviesDetails:
            languageList.extend(index["Languages"])
        new_list=[]
        dict={}
        i=0
        while i<len(languageList):
            j=0
            count=0
            while j<len(languageList):
                if languageList[i] == languageList[j]:
                    count=count+1
                j=j+1
            if languageList[i] not in new_list:
                dict[languageList[i]]=count
            i=i+1
        return (dict)
allMovieLanguage=analyse_movies_language(movieDetailsWithCashing)
# pprint(allMovieLanguage)