stringInput = input("Enter a word or string with more than two character: ")

if len(stringInput) >= 2:
    print(stringInput[::2])
else:
    print("")