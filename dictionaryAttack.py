import hashlib
from hashlib import blake2b
m = hashlib.sha256()

userinput = input("Enter Password\nRestrictions - strictly composed of one to three words from the dictionary\nYour Password: ")
print("Password is " + userinput)
m.update(b'userinput')

def readFile(inFile):
    file = open(inFile, "r")
    words = file.read()
    wordsList = words.split("\n")
    for word in wordsList:
        h.update(b'word')
    #print(wordsList)
    
if __name__ == "__main__":
    readFile("top-20-common-SSH-passwords.txt")

hhexdigest = h.hexdigest()
user2bhexdigest = user2b.hexdigest()
print(hhexdigest)
print(user2bhexdigest)