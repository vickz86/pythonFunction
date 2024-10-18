#example of a dictionnary
exDi = {"name":"jon","age":22,"sex":"m"}
#example of a list
exLi=["first second","third four","five six","seven height"]

def PrintKeyValue(dic:dict):
    """print all the key and value of a dictionary"""
    for k,v in dic.items():
        print(f"{k}  :  {v}")

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


