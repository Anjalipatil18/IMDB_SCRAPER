from imdbTask9 import*
from imdbTask15 import*

def analyseLeadAndCo_actorsName(movie_list):
    leadAndCoActors=[]
    for i in movie_list:
        movieOfCast=i["cast"][:5]
        leadAndCoActors.append(movieOfCast) 
    return leadAndCoActors
leadAndCoActors=analyseLeadAndCo_actorsName(movieDetailsWithCashing)

def lead_actors(movie_list):
    leadActorName=[]
    for i in movie_list:
        movieOfCastLeadActors=i["cast"][0]["actorAndActressName"]
        leadActorName.append(movieOfCastLeadActors)
    return (leadActorName)
leadActorName=lead_actors(movieDetailsWithCashing)

def duplicate_lead_actors(movie_list):
    duplicateLead=[]
    for i in range(len(movie_list)):
        if leadActorName[i] not in duplicateLead:
            duplicateLead.append(leadActorName[i])
    return duplicateLead
duplicateLead=duplicate_lead_actors(leadActorName)

def analyse_co_actors(movie_list):
    new_list=[]
    for index in range(len(duplicateLead)):
        new=[]
        for index1 in movie_list:
            if duplicateLead[index] in index1[0]["actorAndActressName"]:
                new.append(index1)
        new_list.append(new)
    for i in range(len(duplicateLead)):
        dictionary={}
        for nestedList in new_list:
            dict={}
            lead_actor_id=nestedList[0][0]["imdbId"]
            lead_actor=nestedList[0][0]["actorAndActressName"]
            coActorName=[]
            co_actor_list=[]
            for list1 in nestedList:
                for dict1 in list1[1:]:
                    coActorName.append(dict1["actorAndActressName"])
                    if dict1 not in co_actor_list:
                        co_actor_list.append(dict1) 
            duplicateCoActor=[]
            for index in coActorName:
                if index not in duplicateCoActor:
                    duplicateCoActor.append(index)
            frecuent_co_actor=[]
            for i in range(len(duplicateCoActor)):
                count=0
                for j in coActorName:
                    if duplicateCoActor[i]==j:
                        count=count+1
                if count>1:
                    for counter in co_actor_list:
                        if counter["actorAndActressName"]==duplicateCoActor[i]:
                            counter["no_novie"]=count
                            frecuent_co_actor.append(counter)
            if frecuent_co_actor != []:
                dict["name"]=lead_actor
                dict["frequent_co_actor"]=frecuent_co_actor
                dictionary[lead_actor_id]=dict
    return(dictionary)
coActorName=analyse_co_actors(leadAndCoActors)   
# pprint(coActorName) 