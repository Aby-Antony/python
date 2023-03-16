"""
Write a Python program to iterate the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of both three and five print "FizzBuzz".
"""

for i in range (1, 51):
    if ((i % 3 == 0) and (i % 5 == 0)):
        print("FizzBuzz")
    elif (i % 5 == 0):
        print("Buzz")
    elif(i % 3 == 0):
        print("Fizz")
    else:
        print(i)


