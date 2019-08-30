from imdbTask7 import*
from imdbTask9 import*

dictionary={}
def analyse_language_and_directors(directors,movies):
    for i in directors:
        sameLanguage=[]
        for j in movies:
            if i in j["director"]:
                sameLanguage.extend(j["Languages"])
        duplicateLanguageName=[]
        for index in range(len(sameLanguage)):
            if sameLanguage[index] not in duplicateLanguageName:
                duplicateLanguageName.append(sameLanguage[index])
        index=0
        dict={}
        while index<len(duplicateLanguageName):
            j=0
            count=0
            while j<len(sameLanguage):
                if duplicateLanguageName[index] == sameLanguage[j]:
                    count=count+1
                j=j+1
            dict[duplicateLanguageName[index]]=count   
            index=index+1
        dictionary[i]=dict
    return(dictionary)
same_language_and_directors_name=analyse_language_and_directors(duplicateDirector,movieDetailsWithCashing)
# pprint (same_language_and_directors_name)