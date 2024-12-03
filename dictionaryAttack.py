import hashlib
from hashlib import blake2b
h = blake2b()


def readFile(inFile):
    file = open(inFile, "r")
    words = file.read()
    wordsList = words.split("\n")
    for word in wordsList:
        h.update(b'word')
    print(wordsList)
    
if __name__ == "__main__":
    readFile("top-20-common-SSH-passwords.txt")

h.hexdigest()
print(h)