## Activities

1.  Consider the program below.  How many asterisks are printed?

```python
a = 0
while a < 100:
    print('*', end='')
    a += 1

print()
```

2.  Consider the program below.  How many asterisks are printed?

```python
a = 0
while a < 100:
    print('*', end='')

print()
```
3.  Consider the program below.  How many asterisks are printed?

```python
a = 0
while a > 100:
    print('*', end='')
    a += 1

print()
```

4. Consider the program below.

    a. How many times does the loop body execute?    
    b. What does the program output look like?

```python
i = 0
output = 0
while (i < 5):
   output += i
   print(output, " ")
   i += 1
```

5. A factorial number, written like this, ```n!```, is equal to the first ```n``` numbers multiplied together.  For example, ````4! = 4 x 3 x 2 x 1 = 24````.  Modify the program from question 4 to print out the values of the first 5 factorial numbers.  That is, ```1!, 2!, 3!, 4!, 5!```.

6. Did you know that, in a room of 30 people, there's a very good chance (over 70%!) that two of them share the same birthday?  In a room of 50 people the probability goes up to a rather astonishing 97%!  This might seem surprising given there are 365 days in a year, but it's true.

The probability that, in a room of two people, *nobody* shares a birthday is
```
364/365
```

That's because there are 364 days the second person can be born on that are different than the first person's birthday.  

Similarly, the probability that, in a room of 3 people, nobody shares a birthday is
```
364/365 X 363/365
```

And, in a room of 10 people is
```
364/365 X 363/365 X 362/365 x 361/365 x 360/365 x 359/365 x 358/365 x 357/365 x 356/365
```

Do you see the pattern?  Write a program that calculates the probability nobody shares a birthday in our classroom today.