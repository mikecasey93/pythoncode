def longest_word(word1, word2, word3):

    numOfLetters1 = 0
    numOfLetters2 = 0
    numOfLetters3 = 0

#Compares word length
    for i in word1:
        numOfLetters1 += 1

    for j in word2:
        numOfLetters2 += 1

    for k in word3:
        numOfLetters3 += 1

    if numOfLetters1 > numOfLetters2 and numOfLetters1 > numOfLetters3:
        return word1

    elif numOfLetters2 > numOfLetters1 and numOfLetters2 > numOfLetters3:
        return word2

    else:
        return word3

print("The longest word is:",longest_word("Reload", "Hi", "Buffalo"))
