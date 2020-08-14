wordWithoutVowels = ""
userWord = input("Please Enter a word: ")
userWord = userWord.upper()
for letter in userWord:
    if letter == 'A':
        #word = letter
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        wordWithoutVowels+=letter

print(wordWithoutVowels)
