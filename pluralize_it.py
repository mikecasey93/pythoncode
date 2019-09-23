# Asks the user for a number and a word
number = int(input("Enter a number "))
word = input("Enter a word ")

# Pluralizes words ending with "ife"
if word[-3:] == "ife" and (number == 0 or number > 1):
    newWord = list(word)
    for i in range(1, 4):
        newWord.pop()
    newWord.append('i')
    newWord.append('v')
    newWord.append('e')
    newWord.append('s')
    newWord = ''.join(newWord)
    print("In: ", number)
    print("In: ", word)
    print("Out: ", number, newWord)

# Pluralizes words ending with "sh" or "ch"
elif word[-2:] == "sh" or word[-2:] == "ch" and (number == 0 or number > 1):
    print("In: ", number)
    print("In: ", word)
    print("Out: ", number, word + "es")

# Pluralizes words ending with "us"
elif word[-2:] == "us" and (number == 0 or number > 1):
    newWord2 = list(word)
    for j in range(1, 3):
        newWord2.pop()
    newWord2.append('i')
    newWord2 = ''.join(newWord2)
    print("In: ", number)
    print("In: ", word)
    print("Out: ", number, newWord2)

# Pluralizes words ending with "ay", "oy", "ey" or "uy"
elif (word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy") and (number == 0 or number > 1):
    print("In: ", number)
    print("In: ", word)
    print("Out: ", number, word + "s")

# Pluralizes words ending with "y"
elif word[-1:] == "y" and (number == 0 or number > 1):
    newWord3 = list(word)
    newWord3.pop()
    newWord3.append('i')
    newWord3.append('e')
    newWord3.append('s')
    newWord3 = ''.join(newWord3)
    print("In: ", number)
    print("In: ", word)
    print("Out: ", number, newWord3)

# For everything else
else:
    print("In: ", number)
    print("In: ", word)
    if number == 0 or number > 1:
        print("Out: ", number, word + "s")
    else:
        print("Out: ", number, word)
