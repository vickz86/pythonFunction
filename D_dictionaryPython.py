# example of a dictionnary
exDi = {"name": "jon", "age": 22, "sex": "m"}
# example of a list
exLi = ["first second", "third four", "five six", "seven height"]


def PrintKeyValue(dic: dict):
    """print all the key and value of a dictionary"""
    for k, v in dic.items():
        print(f"{k}  :  {v}")


def DicFromList(lis: list) -> dict:
    """create a dictionnary from list,list MUST contain 2 element"""
    # create an empty dictionnary
    outDic = {}
    # loop through element of incoming list
    for el in lis:
        # check it has 2 element
        listel = el.split()
        if len(listel) != 2:
            print(f"{el} doesnt have 2 element! ERROR")
        # add to dictionary
        outDic[listel[0]] = listel[1]
    return outDic


def AddToDic(dic: dict) -> dict:
    """add an element to a dictionnary"""

    # get key
    while True:
        # get the key
        keyVal = input("type the key to add :")
        # check the key is the correct value
        check = input(f"is {keyVal} the key you want to add y/n\n")
        if check.lower() == "y":
            break

    # get value
    while True:
        # get the key
        valVal = input("type the value to add :")
        # check the key is the correct value
        check = input(f"is {valVal} the value you want to add y/n\n")
        if check.lower() == "y":
            break

    # add to dic
    dic[keyVal] = valVal
    # return
    return dic


PrintKeyValue(exDi)
AddToDic(exDi)
PrintKeyValue(exDi)
