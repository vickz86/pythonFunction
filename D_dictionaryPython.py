#example of a dictionnary
exDi = {"name":"jon","age":22,"sex":"m"}
#example of a list
exLi=["first second","third four","five six","seven height"]

def PrintKeyValue(dic:dict):
    """print all the key of a dictionary"""
    #get all key in a list
    keyList=list(dic.keys())
    #iterate and print over keys
    for key in keyList:
        print(f"{key} is a present")


def DicFromList(lis:list)->dict:
    """create a dictionnary from list,list MUST contain 2 element"""
    #create an empty dictionnary
    outDic = {}
    #loop through element of incoming list
    for el in lis:
        #check it has 2 element
        listel = el.split()
        if len(listel)!=2:
            print(f"{el} doesnt have 2 element! ERROR")
        #add to dictionary
        outDic[listel[0]]=listel[1]
    return outDic



# PrintKey(exDi)
for k,v in exDi.items():
    print(k)
    print(v)