from pathlib import Path

exList = ["un deux", "troix quatre", "cinq six", "sept huit"]


def PathOpenFile(thePath: Path) -> list:
    """return a list from a pathFile"""
    # list to return
    returnList: list = []

    with thePath.open(mode="r", encoding="utf-8") as f:
        for line in f:
            returnList.append(line.strip())
    return returnList


def PathWriteFile(listToWrite: list, thePath: Path) -> list:
    "print a list to a filePath"
    with thePath.open(mode="w", encoding="utf-8") as f:
        outlist: list = []
        # add /n to each but last line
        outlist = [
            el + "\n" if nb != len(listToWrite) - 1 else el
            for nb, el in enumerate(listToWrite)
        ]
        f.writelines(outlist)


thePath = Path.cwd() / "_data2.txt"
PathWriteFile(exList, thePath)
