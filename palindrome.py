str = input("Enter the string to check: ")
#reverse srting from postion 1
strrev = str[::-1] 
if (str == strrev):
    print(str, "is a palindrome word")
else:
     print(str, "is a NOT palindrome word") 
