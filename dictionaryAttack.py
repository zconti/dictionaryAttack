import hashlib
import time


def readFile(inFile):
    file = open(inFile, "r")
    words = file.read()
    wordsList = words.split("\n")
    print(wordsList)
    return wordsList
    
if __name__ == "__main__":
    userPassword256 = hashlib.sha256()
    userPassword512 = hashlib.sha512()

    userinput = input("Enter Password\nRestrictions - strictly composed of one to three words from the dictionary\nYour Password: ")
    print("Password is " + userinput)
    userPassword256.update(b'userinput')
    userPassword512.update(b'userinput')
    wordList = readFile("top-20-common-SSH-passwords.txt")
    print(userPassword256)
    print("\n\n")
    start_time = time.perf_counter()
    for word in wordList:
        word256 = hashlib.sha256()
        word256.update(b'word')
        print(word)
        print(word256)
        if(word256 == userPassword256):
            print("\nFOUND\n")

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    userHexdigest256 = userPassword256.hexdigest()
    print(userHexdigest256)
    userHexdigest512 = userPassword512.hexdigest()
    print(userHexdigest512)
