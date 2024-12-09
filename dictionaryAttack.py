import hashlib
import time


def readFile(inFile):
    file = open(inFile, "r")
    words = file.read()
    wordsList = words.split("\n")
    print(wordsList)
    return wordsList
    
def dictionary256(userPassword256, wordList):
    start_time256 = time.perf_counter()
    for word in wordList:
        wordHexdigest256 = hashlib.sha256(word.encode('utf-8')).hexdigest()
        print(wordHexdigest256)
        if wordHexdigest256 == userPassword256:
            print("FOUND\n")
            break
    end_time256 = time.perf_counter()
    print("Done?")
    elapsed_time256 = end_time256 - start_time256
    return elapsed_time256

def dictionary512(userPassword512, wordList):
    start_time512 = time.perf_counter()
    for word in wordList:
        wordHexdigest512 = hashlib.sha256(word.encode('utf-8')).hexdigest()
        print(wordHexdigest512)
        if wordHexdigest512 == userPassword512:
            print("FOUND\n")
            break
    end_time512=  time.perf_counter()
    print("Done?")
    elapsed_time512 = end_time512 - start_time512
    return elapsed_time512

if __name__ == "__main__":
    userPassword256 = hashlib.sha256()
    userPassword512 = hashlib.sha512()

    userinput = input("Enter Password\nRestrictions - strictly composed of one to three words from the dictionary\nYour Password: ")
    print("Password is " + userinput)
    userPassword256.update(userinput.encode('utf-8'))
    userHexdigest256 = userPassword256.hexdigest()
    userPassword512.update(userinput.encode('utf-8'))
    userHexdigest512 = userPassword256.hexdigest()
    wordList = readFile("top-20-common-SSH-passwords.txt")
    print(userHexdigest256)
    print("\n\n")

    time256 = dictionary256(userHexdigest256, wordList)
    time512 = dictionary256(userHexdigest512, wordList)
    print(time256)
    print(time512)
    
    print(userHexdigest256)
    print(userHexdigest512)
