letters = input("Enter input: ")
myDict = {}
for i in letters:
    counter = letters.count(i)
    myDict.update({i : counter})
print(myDict)