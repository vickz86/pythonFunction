listTest = ["un deux", "troix quatre", "cinq six", "seven"]


def OpenFile(filePath: str = "_data.txt") -> list:
    """Returns a list where each line in the file is an element, with trailing newline characters removed."""
    try:
        with open(filePath, "r") as fObj:
            # Read lines and strip trailing newline characters
            outList = [line.strip() for line in fObj]
        return outList
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' was not found.")
        return []
    except IOError:
        print(f"Error: Could not read the file '{filePath}'.")
        return []


def WriteFile(listWrite: list, filePath: str = "_data.txt"):
    """write a list to a file, the list must only contain string"""
    writeList = []

    # add /n to all element of the list , but the last one
    for val, el in enumerate(listWrite):
        # check all element are string
        if isinstance(el, str) != True:
            print(f"ERROR ,{el} is not of type string")

        # check if it is the last element
        if val == (len(listWrite) - 1):
            writeList.append(el)
        else:
            el += "\n"
            writeList.append(el)

    with open(filePath, "w") as fObj:
        fObj.writelines(writeList)
    pass


# WriteFile(listTest)
