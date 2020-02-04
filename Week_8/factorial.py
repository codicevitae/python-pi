import sys

valIn = input("Enter an integer : ")

# Validate input is an integer
try:
    x = int(valIn)
except:
    print("Value must be an integer!")
    sys.exit()

# Validate input is positive
if x < 0:
    print("Value must be positive!")
    sys.exit()

answer = 1

# Calculate answer using a while loop...
i = 1
while i <= x:
    answer = answer * i
    i += 1

# Or a for loop...
# for step in range(1, x + 1) :
#     answer = answer * step

print(valIn, "factorial is", answer)
   
