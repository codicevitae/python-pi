import sys

startString = input("Enter beginning of range to check: ")
endString = input("Enter end of range to check: ")
factor1String = input("Enter first factor to search: ")
factor2String = input("Enter second factor to search: ")

try:
   start = int(startString)
   end = int(endString)
   factor1 = int(factor1String)
   factor2 = int(factor2String)
except:
   print("Invalid input, please try again!")
   sys.exit()

if start >= end:
   print("Starting number must be less than ending number!")
   sys.exit()

numberList = []

for nextInRange in range(start, end + 1):
    if nextInRange%factor1 == 0 and nextInRange%factor2==0:
        numberList.append(str(nextInRange))

print(','.join(numberList))

