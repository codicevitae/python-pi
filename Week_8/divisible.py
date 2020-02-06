numberList = []

for nextInRange in range(1000, 3001):
    if nextInRange%5 == 0 and nextInRange%7==0:
        numberList.append(str(nextInRange))

print(','.join(numberList))

