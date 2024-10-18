def OpenFile(filePath:str = "_data.txt")->list:
    """return a list object,each line is an element"""
    with open(filePath,"r") as fObj:
        #create the list object
        rawList = fObj.readlines()
        #create a new list obj
        outList = []
        #remove \n at the end of the line
        for line in rawList:
            outList.append(line.strip())
        # return the list
        return outList


