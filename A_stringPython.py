# return a letter from question
def GetSpecificLetter(theQuestion: str) -> str:
    while True:
        # ask for the letter you want to get
        answer: str = input(theQuestion)
        # check that is only a single letter
        if len(answer) != 1:
            print("your answer is too long\nOnly type 1 letter")
            continue
        # check the answer is.Alpha
        if answer.isalpha() == False:
            print("your answer is not a letter")
            continue
        return answer

#Get the first index of inputed Word
def GetIndexWord(strToFind:str,strToCheck:str)->int:
    firstIndex = strToCheck.find(strToFind)
    print("hello my dear")