hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

hatList[2] = input("Hello enter the number you wish to replace for the middle number in the list: ")
del hatList[4]

print("The length of the list is: ",len(hatList))

print(hatList)
