word = input("Enter the string to check: ")
split = word.split()
if (split[0] == "Is"):
    print(word)
else:
    newword = "Is " + word
    print(newword)
