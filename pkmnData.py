#Pokedata
#central module for all Pokemon data
import conventionalCode as cc
import fileinput


#Pokemon name and type 
pokeFile_dict = {"Pokemon":"allPkmnGen1-7.csv", "Moves":"PokeAttackdex.csv"}
#fHandle = open(pokeFile)

##typesMatchup_dict2 = {"normal":{"rock":0.5, "ghost":0, "steel":0.5},\
##                        "fighting":{"normal":2, "flying":0.5, "poison":0.5,"rock":2,"bug":0.5,"ghost":0,"steel":2,"psychic":0.5,"ice":2,"dark":2,"fairy":0.5},\
##                        "flying":{"fighting":2, "rock":0.5, "bug":2,"steel":0.5, "grass":2, "electric":0.5},\
##                        "poison":{"poison":0.5,"ground":0.5, "rock":0.5, "ghost":0.5,"steel":0,"grass":2,"fairy":2},\
##                        "ground":{"flying":0, "poison":2,"rock":2,"bug":0.5,"steel":2,"fire":2,"grass":0.5,"electric":2},\
##                        "rock":{"fighting":0.5,"flying":2,"ground":0.5,"bug":2,"steel":0.5,"fire":2,"ice":2},\
##                        "bug":{"fighting":0.5,"flying":0.5,"poison":0.5,"ghost":0.5,"steel":0.5,"fire":0.5,"grass":2,"psychic":2,"dark":2,"fairy":0.5},\
##                        "ghost":{"normal":0,"ghost":2,"psychic":2,"dark":0.5},\
##                        "steel":{"rock":2,"steel":0.5,"fire":0.5,"water":0.5,"electric":0.5,"ice":2,"fairy":2},\
##                        "fire":{"rock":0.5,"bug":2,"steel":2,"fire":0.5,"water":0.5,"grass":2,"ice":2,"dragon":0.5},\
##                        "water":{"ground":2,"rock":2,"fire":2,"water":0.5,"grass":0.5,"dragon":0.5},\
##                        "grass":{"flying":0.5,"poison":0.5,"ground":2,"rock":2,"bug":0.5,"steel":0.5,"fire":0.5,"water":2,"grass":0.5,"dragon":0.5},\
##                        "electric":{"flying":2,"ground":0,"water":2,"grass":0.5,"electric":0.5,"dragon":0.5},\
##                        "psychic":{"fighting":2,"poison":2,"steel":0.5,"psychic":0.5,"dark":0},\
##                        "ice":{"flying":2,"ground":2,"steel":0.5,"fire":0.5,"water":0.5,"grass":2,"ice":0.5,"dragon":2},\
##                        "dragon":{"steel":0.5,"dragon":2,"fairy":0},\
##                        "dark":{"fighting":0.5,"ghost":2,"psychic":2,"dark":0.5,"fairy":0.5},\
##                        "fairy":{"fighting":2,"poison":0.5,"steel":0.5,"fire":0.5,"dragon":2,"dark":2}}


typesMatchup_dict = {'Normal': {'Rock': 0.5, 'Ghost': 0, 'Steel': 0.5},\
                     'Fighting': {'Normal': 2, 'Flying': 0.5, 'Poison': 0.5, 'Rock': 2, 'Bug': 0.5, 'Ghost': 0, 'Steel': 2, 'Psychic': 0.5, 'Ice': 2, 'Dark': 2, 'Fairy': 0.5},\
                     'Flying': {'Fighting': 2, 'Rock': 0.5, 'Bug': 2, 'Steel': 0.5, 'Grass': 2, 'Electric': 0.5},\
                     'Poison': {'Poison': 0.5, 'Ground': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Steel': 0, 'Grass': 2, 'Fairy': 2},\
                     'Ground': {'Flying': 0, 'Poison': 2, 'Rock': 2, 'Bug': 0.5, 'Steel': 2, 'Fire': 2, 'Grass': 0.5, 'Electric': 2},\
                     'Rock': {'Fighting': 0.5, 'Flying': 2, 'Ground': 0.5, 'Bug': 2, 'Steel': 0.5, 'Fire': 2, 'Ice': 2},\
                     'Bug': {'Fighting': 0.5, 'Flying': 0.5, 'Poison': 0.5, 'Ghost': 0.5, 'Steel': 0.5, 'Fire': 0.5, 'Grass': 2, 'Psychic': 2, 'Dark': 2, 'Fairy': 0.5},\
                     'Ghost': {'Normal': 0, 'Ghost': 2, 'Psychic': 2, 'Dark': 0.5},\
                     'Steel': {'Rock': 2, 'Steel': 0.5, 'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Ice': 2, 'Fairy': 2},\
                     'Fire': {'Rock': 0.5, 'Bug': 2, 'Steel': 2, 'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Ice': 2, 'Dragon': 0.5},\
                     'Water': {'Ground': 2, 'Rock': 2, 'Fire': 2, 'Water': 0.5, 'Grass': 0.5, 'Dragon': 0.5},\
                     'Grass': {'Flying': 0.5, 'Poison': 0.5, 'Ground': 2, 'Rock': 2, 'Bug': 0.5, 'Steel': 0.5, 'Fire': 0.5, 'Water': 2, 'Grass': 0.5, 'Dragon': 0.5},\
                     'Electric': {'Flying': 2, 'Ground': 0, 'Water': 2, 'Grass': 0.5, 'Electric': 0.5, 'Dragon': 0.5},\
                     'Psychic': {'Fighting': 2, 'Poison': 2, 'Steel': 0.5, 'Psychic': 0.5, 'Dark': 0},\
                     'Ice': {'Flying': 2, 'Ground': 2, 'Steel': 0.5, 'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Ice': 0.5, 'Dragon': 2},\
                     'Dragon': {'Steel': 0.5, 'Dragon': 2, 'Fairy': 0},\
                     'Dark': {'Fighting': 0.5, 'Ghost': 2, 'Psychic': 2, 'Dark': 0.5, 'Fairy': 0.5}, \
                     'Fairy': {'Fighting': 2, 'Poison': 0.5, 'Steel': 0.5, 'Fire': 0.5, 'Dragon': 2, 'Dark': 2}}
##def titleDic(dic):
##    ret_dict = {}
##    for key in dic:
##        ret_dict[key.title()] = dic[key]
##    return ret_dict
##
##def titleDic2(dic):
##    ret_dict = {}
##    for key in dic:
##        ret_dict[key.title()] = titleDic(dic[key])
##    return ret_dict
##print(titleDic2(typesMatchup_dict))
    
    
def getFHandle(pokeFilePar, action = "r"):
    try:
        pokeFilePar = pokeFilePar.title()
        pokeFile = pokeFile_dict[pokeFilePar]
        fHandle = open(pokeFile, action)
    except:
        print("Please enter a valid file name:")
        for file in pokeFile_dict:
            print(file)
        print("Try typing a valid action: w+, w, r, a+")
        exit()
    return fHandle

def getFileName(pokeFilePar):
    fileName = ""
    try:
        pokeFilePar = pokeFilePar.title()
        fileName = pokeFile_dict[pokeFilePar]
    except:
        print("Please enter a valid file name:")
        for file in pokeFile_dict:
            print(file)
    return fileName

def getHeader(fHandle):
    header = fHandle.readline()
    header = cc.strNspl(header)
    return header


def printData(fHandle):
    for line in fHandle:
        line = cc.strNspl(line)
        print(line)

##def writeHeader(pokeFilePar):
##    headerStr = ""
##    header = []
##    #not all lines have filled column values and thus, may vary
##    #maxcolnCount keeps track of the largest column entries of any line
##    
##    fHandle = getFHandle(pokeFilePar, action = "r")
##    hdrCount = len(getHeader(fHandle))
##    fHandle = getFHandle(pokeFilePar, action = "a+")
##    
##    while len(header) < hdrCount:
##        hdrName = input("Please enter header name for column "+str(len(header)+1)+"/"+str(hdrCount)+":\n")
##        header.append(hdrName)
##
##    for hdrName in header:
##        headerStr += str(hdrName)+", "
##    fHandle.write(headerStr)
##    fHandle.close()
##

    

#creates a dictionary based on a given list of column names
def autoDict(fHandle, selectedColn_list = [], index = True):
    #fHandle = getFHandle(fHandle)
    retDict = {}
    coln_dict = {}
        
    #For now, I assume, a header is given for all files
    hdr = getHeader(fHandle)
    for name in selectedColn_list:
        if name not in hdr:
            print(str(name)+" is not a valid column name.")
            print("Please select from: "+str(hdr))
            break
        
    c = 0 #column dictionary index
    for name in hdr:
        coln_dict[name] = c
        c += 1
                      
    i = 0 #specific column index
    for line in fHandle:
        line = cc.strNspl(line)
        #if no columns are selected
        if selectedColn_list == []:
            retDict[line[0]] = tuple(line[1:])
        #if the first column is selected
        elif hdr[0] in selectedColn_list and index == False:
            for name in selectedColn_list[1:]:
                if line[0] not in retDict:
                    retDict[line[0]] = line[coln_dict[name]]
                else:
                    oldColn = retDict.get(line[0])
                    newColn = line[coln_dict[name]]
                    comColn = cc.rec_cascadeTuples((oldColn,newColn))
                    retDict[line[0]] = comColn
        else:
            moreColn = ()
            for name in selectedColn_list:
                if i not in retDict:
                    retDict[i] = line[coln_dict[name]]
                else:
                    oldColn = retDict.get(i)
                    newColn = line[coln_dict[name]]
                    comColn = cc.rec_cascadeTuples((oldColn,newColn))
                    retDict[i] = comColn
            i += 1
    return retDict


#summarizes single and dual types
#summarizes type relativity
def pokeTypeSummary():
    #fHandle = getFHandle("Pokemon")
    type_dict = autoDict(fHandle)
    dualTypeCount = 0
    for mon in type_dict:
        if type_dict[mon][1] == "":
            dualTypeCount += 1
    

def getDistinctTypes(fHandle):
    #fHandle = getFHandle("Moves")
    if fHandle.title() == "Moves":
        fHandle = getFHandle("Moves")
        types_dict = autoDict(fHandle, ["Type"])
        distType_list = []
        
        for key in types_dict:
           if types_dict[key] not in distType_list:
               distType_list.append(types_dict[key])
               
    elif fHandle.title() == "Pokemon":
        fHandle = getFHandle("Pokemon")
        types_dict = autoDict(fHandle, ["Type I", "Type II"])
        distType_list = []

        for key in types_dict:
            if types_dict[key] not in distType_list:
                distType_list.append(types_dict[key])
                
    return distType_list


#problem: unhashable type 'list' occurs when I try to count the distinct number of dual types
def countDistinct(poke_dict):
    count_dict = {}
    
    for types in poke_dict:
##        if isinstance(type_dict[types],list):
##                type_dict[types] = tuple(type_dict[types])
        if poke_dict[types] not in count_dict:
            count_dict[poke_dict[types]] = 1
        else:
            count_dict[poke_dict[types]] += 1
    return count_dict

#maybe: actual movesets for Pokemon, but it requires large database
#next step include pkmn name parameter

#function returns all moves of a certain type, given a list
def getAllMoves(moveTypes = []):
    retDict = {}

    for move in pkmnMoveType_dict:
        if pkmnMoveType_dict[move] in moveTypes:
            if pkmnMoveType_dict[move] not in retDict:
                retDict[pkmnMoveType_dict[move]] = move
            else:
                oldMove = retDict.get(pkmnMoveType_dict[move])
                newMoves = [oldMove,move]
                newMoves = cc.cascadeLists(newMoves)
                retDict[pkmnMoveType_dict[move]] = newMoves
    return retDict

#function returns the counts of all the moves per type, given a dictionary type as key, list of moves as value
def moveCounts(pkmnTMoves_dict):
    retDict = []
    for moveType,moves in pkmnTMoves_dct:
        retDict[moveType] = len(moves)
    return retDict

#------------------------------------------------

fHandle = getFHandle("Pokemon")
pkmnTypes_dict = autoDict(fHandle)

fHandle2 = getFHandle("Moves")
pkmnMoveType_dict = autoDict(fHandle2,["Name","Type"],index = False)


type_list = []
for key in typesMatchup_dict:
    type_list.append(key)




    
