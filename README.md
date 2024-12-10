# dictionaryAttack
Final Class Project CS2104

To operate the program, you start it and then type in a password made from the words in the dictionary provided.  There should be no spaces in between the words.  Once you input a password, the program will crack it and then prompt for another password.  This will continue until you type “q” to exit the program.  Once you exit the program, the statistics of the passwords being cracked will be displayed in 2 different png files, one for SHA256 and the other for SHA512.

Our program splits the dictionary attack into two parts; hash256 and hash512.  They call their respective functions, which go through three for-loops to compare every word combination to the userInput.  When it is found, the time taken and iterations through the possible words are returned, and displayed on graphs.

The dictionary file used was a modified version of “500-worst-passwords.txt”.  I cut off the last 300 words and renamed it “200-worst-passwords.txt” to better fit the instructions of the assignment.  It is attached within this zip file.