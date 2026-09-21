lines = []
while True:
    line = input("Enter line:")
    if line == "":
        break
    lines.append(line.lower())

for l in lines:
    print(l)    