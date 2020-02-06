n=int(input("Enter number: "))

answer=0

while(n>0):
    x=n%10
    answer=answer*10+x
    n=n//10

print("Answer:",answer)
