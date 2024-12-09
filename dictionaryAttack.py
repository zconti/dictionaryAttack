import hashlib
import time
import matplotlib.pyplot as plt

def readFile(inFile):
    file = open(inFile, "r")
    words = file.read()
    wordsList = words.split("\n")
    print(wordsList)
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
                #print(comboWord)
                wordHexdigest256 = hashlib.sha256(comboWord.encode('utf-8')).hexdigest()
                #print(wordHexdigest256)
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
                #print(comboWord)
                wordHexdigest512 = hashlib.sha512(comboWord.encode('utf-8')).hexdigest()
                #print(wordHexdigest256)
                if wordHexdigest512 == userPassword512:
                    print("FOUND\n")
                    end_time512 = time.perf_counter()
                    elapsed_time512 = end_time512 - start_time512
                    return [elapsed_time512, counter]
    return 0

if __name__ == "__main__":
    userPassword256 = hashlib.sha256()
    userPassword512 = hashlib.sha512()

    userinput = input("Enter Password\nRestrictions - strictly composed of one to three words from the dictionary\nYour Password: ")
    print("Password is " + userinput)
    userPassword256.update(userinput.encode('utf-8'))
    userHexdigest256 = userPassword256.hexdigest()
    userPassword512.update(userinput.encode('utf-8'))
    userHexdigest512 = userPassword512.hexdigest()
    wordList = readFile("top-20-common-SSH-passwords.txt")
    print(userHexdigest256)
    print(userHexdigest512)
    print("\n\n")

    time256 = dictionary256(userHexdigest256, wordList)
    time512 = dictionary512(userHexdigest512, wordList)
    print(time256[0])
    print(time512[0])
    print(time256[1])
    print(time512[1])
    
    print(userHexdigest256)
    print(userHexdigest512)
    
    
    names = ['SHA256', 'SHA512']
    times = [time256[0], time512[0]]

    plt.figure(figsize=(9, 3))

    plt.subplot(131)
    plt.bar(names, times)
    #plt.subplot(132)
    #plt.scatter(names, values)
    #plt.subplot(133)
    #plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.savefig('plot.png')
