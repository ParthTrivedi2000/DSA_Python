# Q) print all the possible combination for the given number on dice.

def dice(processed, target):
    if target == 0:
        print(processed)
        return

    for i in range(1, 7):
        if i <= target:
            dice(processed + " " + str(i), target - i)
        else:
            break


# dice("", 4)

# Q) with return.

def diceRet(processed, target):
    if target == 0:
        # print(processed)
        final = []
        final.append(processed[:])
        return final

    l1 = []
    # i = 0
    for i in range(1, 7):
        if i <= target:
            l1.extend(diceRet(processed + " " + str(i), target - i))
        else:
            break
    return l1


# print(diceRet("", 4))

# Q) Sometimes it was given in question that 7 faces of dice or 8 faces dice. i mean custom faces on the dice then?

def diceFace(processed, target, face):
    if target == 0:
        # print(processed)
        final = []
        final.append(processed[:])
        return final

    l1 = []
    # i = 0
    for i in range(1, face+1):
        if i <= target:
            l1.extend(diceFace(processed + " " + str(i), target - i, face))
        else:
            break
    return l1

print(diceFace("",4,7))
