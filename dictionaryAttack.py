import hashlib
import time
import matplotlib.pyplot as plt

def readFile(inFile):
    file = open(inFile, "r")
    words = file.read()
    wordsList = words.split("\n")
    return wordsList
    
def dictionary256(userPassword256, wordList):
    counter = 0
    start_time256 = time.perf_counter()
    for word in wordList:
        firstWord = word
        for word in wordList:
            secondWord = word
            for word in wordList:
                counter += 1
                comboWord = firstWord + secondWord + word
                wordHexdigest256 = hashlib.sha256(comboWord.encode('utf-8')).hexdigest()
                if wordHexdigest256 == userPassword256:
                    print("FOUND\n")
                    end_time256 = time.perf_counter()
                    elapsed_time256 = end_time256 - start_time256
                    return [elapsed_time256, counter]
    return 0

def dictionary512(userPassword512, wordList):
    counter = 0
    start_time512 = time.perf_counter()
    for word in wordList:
        firstWord = word
        for word in wordList:
            secondWord = word
            for word in wordList:
                counter += 1
                comboWord = firstWord + secondWord + word
                wordHexdigest512 = hashlib.sha512(comboWord.encode('utf-8')).hexdigest()
                if wordHexdigest512 == userPassword512:
                    print("FOUND\n")
                    end_time512 = time.perf_counter()
                    elapsed_time512 = end_time512 - start_time512
                    return [elapsed_time512, counter]
    return 0

if __name__ == "__main__":
    userinput = input("Enter Password\nRestrictions - strictly composed of one to three words from the dictionary\nYour Password: ")
    sha256times = []
    sha512times = []
    names = []
    guesses = []
    count = 0
    while(userinput != "q"):
        count += 1
        userPassword256 = hashlib.sha256()
        userPassword512 = hashlib.sha512()

        print("Password is " + userinput)
        userPassword256.update(userinput.encode('utf-8'))
        userHexdigest256 = userPassword256.hexdigest()
        userPassword512.update(userinput.encode('utf-8'))
        userHexdigest512 = userPassword512.hexdigest()
        wordList = readFile("200-worst-passwords.txt")

        time256 = dictionary256(userHexdigest256, wordList)
        time512 = dictionary512(userHexdigest512, wordList)
    
    
        names.append((str)(count))
        sha256times.append(time256[0])
        sha512times.append(time512[0])
        guesses.append(time256[1])
        words = len(wordList)-1
    
        userinput = input("Enter Password\nRestrictions - strictly composed of one to three words from the dictionary\nYour Password: ")
    plt.figure(figsize=(12,4))

    plt.subplot(131)
    plt.bar(names, sha512times)
    plt.ylabel('Time(sec)')
    plt.title('Time Taken to Crack SHA512')
    plt.subplot(132)
    plt.bar(names, guesses)
    plt.ylabel('Guesses')
    plt.title('Number of Guesses')
    plt.subplot(133)
    plt.bar("Dictionary", words)
    plt.ylabel('Words')
    plt.title('Words in Dictionary')
    plt.tight_layout()
    plt.savefig('512stats.png')
    
    plt.figure(figsize=(12,4))
    plt.subplot(131)
    plt.bar(names, sha256times)
    plt.ylabel('Time(sec)')
    plt.title('Time Taken to Crack SHA256')
    plt.subplot(132)
    plt.bar(names, guesses)
    plt.ylabel('Guesses')
    plt.title('Number of Guesses')
    plt.subplot(133)
    plt.bar("Dictionary", words)
    plt.ylabel('Words')
    plt.title('Words in Dictionary')
    plt.tight_layout()
    plt.savefig('256stats.png')
