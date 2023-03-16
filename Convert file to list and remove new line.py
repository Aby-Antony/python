fileobj=open("domains.txt")
lines=[]
for line in fileobj:
    lines.append(line.strip())
print(lines)