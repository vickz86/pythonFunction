#get an int value from the user
def GetInteger(question:str)->int:
    while True:
        #print the input
        print(question)
        #get the input from the user
        rawInput = input()
        #check if the value contain only number
        if rawInput.isdigit():
            return int(rawInput)
        else:
            print(f"{rawInput} is not a correct input\nTry again")

