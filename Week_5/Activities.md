## Activities

1. Consider the program below.

    a. How many times does the loop body execute?    
    b. What does the program output look like?

```python
i = 0
output = 0
while (i < 5):
   output = output + i
   print(output, " ")
   i = i + 1
```

2. A factorial number, written like this, ```n!```, is equal to the first ```n``` numbers multiplied together.  For example, ````4! = 4 x 3 x 2 x 1 = 24````.  Modify the program from question 1 to print out the values of the first 5 factorial numbers.  That is, ```1!, 2!, 3!, 4!, 5!```.

3. Did you know that, in a room of 30 people, there's a very good chance (over 70%) that two of them share the same birthday?  In a room of 50 people the probability goes up to a rather astonishing 97%!  This might seem surprising given there are 365 days in a year, but it's true.

The probability that, in a room of two people, *nobody* shares a birthday is
```
364/365 X 363/365
```

The probability of that in a room of three people is
```
364/365 X 363/365 X 362/365
```

And, in a room of 10 people is
```
364/365 X 363/365 X 362/365 x 361/365 x 360/365 x 359/365 x 358/365 x 357/365 x 356/365 x 355/365
```

Do you see the pattern?  Write a program that calculates this probability for a room of 23 people.


4. Modify your program from (3) to ask the user for the number of people in a room and then print out the probability nobody in that room shares a birthday.

5. Can you modify your program to handle the case where the user enters something that isn't a number?  In python, you can test whether an input is a number using the ```isnumeric()``` library function.

````python
i = input("Please enter a number: ")
if (i.isnumeric()):
   print("You entered a number!")
else:
   print("You didn't enter a number!")
````