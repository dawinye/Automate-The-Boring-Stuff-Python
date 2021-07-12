import random

numberOfStreaks = 0
streak = 0

for experimentNumber in range(10000):
    listOfHT = []
    for i in range(100):
        if random.randint(0,1) == 0:
            listOfHT.append('H')
        else:
            listOfHT.append('T')

    for i in range(len(listOfHT)):
        if listOfHT[i] == listOfHT[i-1]:
            streak +=1
            if streak >= 6:
                numberOfStreaks +=1
                streak = 0
        else:
            streak = 0



print(f"Chance of streak: {numberOfStreaks / 100} %")
