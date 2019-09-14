word = input()

capitalLetter = []

for char in word:
    if char.isupper() == True:
        capitalLetter.append(char)

print("".join(capitalLetter))