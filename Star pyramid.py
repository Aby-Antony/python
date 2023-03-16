
k = 0

for i in range(1, 5):
    for space in range(1, (5-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()