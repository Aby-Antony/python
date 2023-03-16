# title Default title text
# program: password policy checking.
#

# Password requirements.
# * Atlest 1 uppercase
# * Atlest 1 lowercase
# * Atlest 1 digit
# * Atlest 1 special character
# * min length 8 characters
# * max length 12 characters

password = input("Enter your password: ")

uppercase   = False
lowercase   = False
digit   = False
special = False

if len(password) >= 8 and len(password) <= 12:
    for char in password:
        if char.isupper():
            uppercase = True
        elif char.islower():
            lowercase = True
        elif char.isdigit():
            digit = True
        else:
            special = True
    if uppercase and lowercase and digit and special:
        print("Super! \nValid password")
    else:
        print("Password doesn't meet the requirements")
else:
    print("Password is too short or large")