types = ["water", "fire", "grass"]
toFind = "fire"
choiceIndex = -1
for i in range(len(types)):
    if types[i] == toFind:
        choiceIndex = i
print(choiceIndex)
