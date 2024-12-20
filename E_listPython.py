my_list = [
    "apple",
    "banana",
    "",
    "cherry",
    "date",
    "",
    "elderberry",
    "peach",
]

exLi = ["hello;12;booby", "bonjour;12;james", "allo;15;billie"]


def SliceList(inList: list, cutRelEnd: int = 1) -> tuple:
    """return 2 list from list, cut relative to the end"""
    # get len of inList
    lenL = len(inList)
    # check if list is correct
    if lenL == 0:
        print("ERROR, list is empty")

    # check if cut is in correct range
    if cutRelEnd < 0 or cutRelEnd > lenL:
        print("ERROR, cut value is not in correct range")

    # cut value
    cutVal = lenL - cutRelEnd
    # create list1
    list1 = inList[:cutVal]
    # create list2
    list2 = inList[cutVal:]

    # return the tupple
    return (list1, list2)


def ListTuppleFromRawList(rawList: list) -> list:
    """create a list from a raw list from file"""
    finalOutList: list = []

    for el in rawList:
        elList: list = []
        # split each str in rawList
        elements = el.split(";")

        # for each single element of each string
        for part in elements:
            try:
                part = int(part)
                elList.append(part)
                continue
            except:
                pass

            try:
                part = float(part)
                elList.append(part)
                continue
            except:
                pass

            elList.append(part)

        finalOutList.append(tuple(elList))

    print(finalOutList)


def SeparateListAtEmptyLines(theList: list) -> list:
    """Separate the list at empty elements in the list, return a list of lists"""
    # Declare the return list
    returnList: list = []

    # Create the temp list
    tempList: list = []

    for nb, element in enumerate(theList):
        # Check if empty
        if element == "":
            if tempList:  # Only append non-empty tempList
                returnList.append(tempList)
            tempList = []  # Reset tempList for the next sublist
        else:
            # If element is not empty, append to tempList
            tempList.append(element)

    # Add any remaining elements in tempList to returnList
    if tempList:
        returnList.append(tempList)

    return returnList
