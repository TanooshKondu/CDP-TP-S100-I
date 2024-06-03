def printThis(position):
    print("Leaving here", position)
    if position == 0:
        print("Base condition got hit")
        return
    if position % 2 == 1:
        print("Even Position:", position)
    else:
        print("Odd Position:", position)
    printThis(position -1)
    for index in range(position, -1, -1):
        print("Index :", index)
    print("Enter here: ", position)
printThis(12)