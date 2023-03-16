str = input("Enter the string to check: ")
 
if (str.isalnum() == True):
    print(str, ":Contains numbers & characters only")
else:
    print(str, ":Contains special characters")

if (str.isalpha() == True):
    print(str, ": Is alphabetical")
else:
    print(str, ":Is not an alphabetical")

if (str.isdigit() == True):
    print(str, ":Is a digit")
else:
    print(str, ":Is not a digit")

if (str.islower() == True):
    print(str, ":Lower case")
else:
    print(str, ":Contains upper case")