def readFile(inFile):
    file = open(inFile, "r")
    words = file.read()
    wordsList = words.split("\n")
    print(wordsList)
    
if __name__ == "__main__":
    readFile("top-20-common-SSH-passwords.txt")