import hashlib
import time


def readFile(inFile):
    file = open(inFile, "r")
    words = file.read()
    wordsList = words.split("\n")
    print(wordsList)
    return wordsList
    
def dictionary256(userPassword, wordList):
    start_time = time.perf_counter()
    for word in wordList:
        word256 = hashlib.sha256()
        word256.update(b'word')
        print(word)
        wordHexdigest256 = word256.hexdigest()
        print(wordHexdigest256)
        if(wordHexdigest256 == userPassword256):
            print("\nFOUND\n")
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time

if __name__ == "__main__":
    userPassword256 = hashlib.sha256()
    userPassword512 = hashlib.sha512()

    userinput = input("Enter Password\nRestrictions - strictly composed of one to three words from the dictionary\nYour Password: ")
    print("Password is " + userinput)
    userPassword256.update(b'userinput')
    userHexdigest256 = userPassword256.hexdigest()
    userPassword512.update(b'userinput')
    userHexdigest512 = userPassword256.hexdigest()
    wordList = readFile("top-20-common-SSH-passwords.txt")
    print(userHexdigest256)
    print("\n\n")

    time256 = dictionary256(userPassword256, wordList)

    
    userHexdigest256 = userPassword256.hexdigest()
    print(userHexdigest256)
    userHexdigest512 = userPassword512.hexdigest()
    print(userHexdigest512)
