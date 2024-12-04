import hashlib
from hashlib import blake2b
userPassword = hashlib.sha256()

userinput = input("Enter Password\nRestrictions - strictly composed of one to three words from the dictionary\nYour Password: ")
print("Password is " + userinput)
userPassword.update(b'userinput')

def readFile(inFile):
    file = open(inFile, "r")
    words = file.read()
    wordsList = words.split("\n")
    for word in wordsList:
        h.update(b'word')
    #print(wordsList)
    
if __name__ == "__main__":
    readFile("top-20-common-SSH-passwords.txt")

userHexdigest = userPassword.hexdigest()
print(userHexdigest)