stringInput = input("Enter a sentence: ")

if "not" in stringInput and  "poor" in stringInput:
    print(stringInput.replace("not that poor", "good"))
else:
    print(stringInput)