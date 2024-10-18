my_list = ["apple", "banana", "cherry", "date", "elderberry", "peach"]


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
    print(list1, list2)
