from imdbTask1 import* 

sortedYear=[]
duplicateYears=[]
def sortedYearFun():
    index=0
    while index<len(movieInfo):
        year=movieInfo[index]["movieYear"]
        sortedYear.append(year)
        sortedYear.sort()
        index=index+1
    i=0
    while i<len(sortedYear):
        if sortedYear[i] not in duplicateYears:
            duplicateYears.append(sortedYear[i])
        i=i+1
    return duplicateYears
sortYearOfMovie=sortedYearFun()

def group_by_year():
    j=0 
    CommonYearMovieDetails={}   
    while j<len(sortYearOfMovie):
        commonYearList=[]
        index=0
        while index<len(movieInfo):
            if sortYearOfMovie[j]==movieInfo[index]["movieYear"]:
                commonYearList.append(movieInfo[index])
            index=index+1   
        CommonYearMovieDetails[sortYearOfMovie[j]]=commonYearList
        j=j+1
    return CommonYearMovieDetails
movieYearOfList=group_by_year()
# pprint (movieYearOfList)