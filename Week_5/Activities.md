# Loops

## Activities

### Question 1

Consider the program below.  How many asterisks are printed?

```python
a = 0
while a < 10:
    print('*', end='')
    a += 1

print()
```

Input the program, either in the REPL or a file, and see if you're correct.

### Question 2

Consider the program below.  How many asterisks are printed?

```python
a = 0
while a < 10:
    print('*', end='')

print()
```

Input the program, either in the REPL or a file, and see if you're correct.

### Question 3

Consider the program below.  How many asterisks are printed?

```python
a = 0
while a > 100:
    print('*', end='')
    a += 1

print()
```

Input the program, either in the REPL or a file, and see if you're correct.

### Question 4

Consider the program below.

a. How many times does the loop body execute?
b. What does the program output look like?

```python
i = 0
output = 0
while (i < 5):
   output += i
   print(output, ", ")
   i += 1
```

Input the program, either in the REPL or a file, and see if you're correct.

### Question 5

A factorial number, written like this, $n!$, is equal to the first $n$ numbers multiplied together.  For example, 

$$4! = 4 \times 3 \times 2 \times 1 = 24$$

Modify the program from question 4 to print out the values of the first 5 factorial numbers.  That is,
  
$$1!, 2!, 3!, 4!, 5!$$

### Question 6

Modify the program from Question 5 to continue to ask the user for a number, $k$, and print out the first $k!$ numbers.

Exit the program when the user enters something that isn't a positive number.

Hint:  you can use the library function, isNumeric(), to determine whether an string input is numeric

```python
entered = input('Please enter a number: ')
if (entered.isnumeric()):
   print("Yup, that's a number")
```

### Question 7

Did you know that, in a room of 30 people, there's a very good chance (over 70%!) that two of them share the same birthday?  In a room of 50 people the probability goes up to 97% (!)  This might seem surprising given there are 365 days in a year, but it's true.

The probability, $p$, that 2 people do not share a birthday is:

$$
p = 364/365
$$

That's because there are 364 out of 365 days the second person can be born on that are not the first person's birthday.  

Similarly, the probability that, in a room of 3 people, nobody shares a birthday is:

$$
p = \frac{364}{365} \times \frac{363}{365}
$$

because the 3rd person has 363 days they can be born on that are neither the first person's nor the second person's birthday.

In a room of 10 people the probability is:

$$
p = \frac{364}{365} \times \frac{363}{365} \times \frac{362}{365} \times \frac{361}{365} \times \frac{360}{365} \times \frac{359}{365} \times \frac{358}{365} \times \frac{357}{365} \times \frac{356}{365} \times \frac{355}{365}
$$

Do you see the pattern?  Write a program that calculates the probability nobody shares a birthday in our classroom today.
