import string


name = input("Enter the name:")
englishmark = int(input("Enter English Mark:"))
mathsmark =  int(input("Enter Maths Mark:"))
sciencemark = int(input("Enter Science Mark:"))
malmark = int(input("Enter Malayalam Mark:"))
hinmark = int(input("Enter Hindi Mark:"))

totmark = englishmark + mathsmark + sciencemark + malmark + hinmark
avermark = totmark/250
percentage = avermark * 100

print("\nResult of", name)
print("Total Mark is", totmark)
print ("Average:", avermark)
print ("Percentage:", percentage)

if percentage >= 30:
    print(name, "is PASSED")
else:
    print(name, "is FAILED")