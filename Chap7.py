catNames = []
while True:
    print("Enter the name of Cat #" + str(len(catNames)+1 ))
    name = input()
    if name == '':
        break

    catNames.append(name)

print('the cat names are:')
i = 0
for i in len(catNames):
    print(catNames[i])
