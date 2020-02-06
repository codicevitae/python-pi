import random

n = random.randint(1, 99)

usersNumber = int(input("Enter an integer from 1 to 99: "))

while n != usersNumber:
    print("thinking...")
    if usersNumber < n:
        print("too low")
        usersNumber = int(input("Enter an integer from 1 to 99: "))
    elif usersNumber > n:
        print("too high")
        usersNumber = int(input("Enter an integer from 1 to 99: "))

print("correct!")
