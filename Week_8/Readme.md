## Week 8 
### Tuesday, Feb 4th

## Lesson: Practical Exercises

#### Goals: 
* To better understand previously covered concepts and functions
* To be able to put these concepts together to solve new problems
* To discuss different ways of solving problems

## Exercise 1:
#### Goal:
Write a Python program which accepts the radius of a circle from the user and compute the area. (area = π r<sup>2</sup>)

_Sample Input:_  
r = 1.1  

_Sample Output:_  
Area = 3.8013271108436504

#### Review:
* How do we accept input and turn it into a number?
* How can we alert the user if they do not enter a positive number?

## Excercise 2:
#### Goal:
Write a Python program which will take an integer input from the user and write out the factorial value of that number.

_Sample Input:_
5

_Sample Output:_
120

#### Discuss: 
* How do we calculate the factorial? (n * n-1 * n-2 * ..... * 1)
* How can we repeat a step as many times as needed?

## Exercise 3:
#### Goal: 
Write a Python program that will find all numbers between 1,000 and 3,000 that are divisible by both 5 and 7.

_Sample Output:_
If our range was 1 to 50, the output would be:
35

#### Discuss:
* How should we check every number in our range?
* How do we know if a number is divisible by another number?
* How should we output the results?
* How could we modify this so that the user enters the start and end of the range to check as well as the two numbers each answer has to be divisible by?


## Week 8 
### Tuesday, Feb 6th

## Lesson: Understanding Code

#### Goals:
* To be able to read and understand Python scripts
* To think through logic and loops and predict the outcome

## Example 1:
#### What does the following Python code do?

```
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
```

## Example 2:
#### What does the following Python code do?
```
n=int(input("Enter number: "))
answer=0
while(n>0):
    x=n%10
    answer=answer*10+x
    n=n//10
print("Answer:",answer)
```

## Example 3:
#### What does the following Python code do?
```
for i in range(1,101):
   if i%3 == 0:
      print("fizz")
   elif i%5 == 0:
      print("buzz")
   else:
      print(i)
```

## Example 4:
#### What does this code do?
```
numbers = [0, 3, 1, 8, 5, 2, 9]

for number in numbers:
   i = 0
   answer = ""
   while i < number:
      answer += str(number)
      i += 1
   print(answer)
```
