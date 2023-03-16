list = ["a", "e", "f", "g", "e", "e", "h", "i", "j", "b", "c", "d"]
print("input list is: ", list)

list.insert(2, "z")
print("\nInserted 'z' into the list: ", list)

list.remove("e")
print("\nRemoved 'e' from the list: ", list)

list.append("e")
print("\nAppended 'e' to the list: ", list)

list.sort()
print("\nSorted list: ", list)

tmp = list.pop()
print("\npop list: ", list, " & pop letter is: ", tmp)

list.reverse()
print("\nReverse list: ", list, "\n")