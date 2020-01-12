# Day 1: While loop

## Supplement

Video [here](https://www.youtube.com/watch?v=T3hV1qSF-3U)

Powerpoint [here](https://1drv.ms/p/s!AlitrBXgrF2Biukd1fh8y0JKBWpAcA?e=nHzyxZ).

## Goals & Objectives
The goal of this lesson is to understand what a loop is in programming, when a loop is an appropriate tool for solving a programming problem, and the syntax for implementing an "indefinite" loop in Python using the ```while``` construct.

Specifically:

- The students will understand the anatomy of an ```indefinite loop``` (aka, the ```while loop```)

- The students will understand the what a loop invariant is how it helps ensuring the correcness of a loop

- The student will learn what an ```infinite loop``` is, will be to identify situations that cause one, and learn a couple "good ideas" for avoiding creating one.

## Lesson
*These concepts will be given interactively, via whiteboard/projector. Students can take notes during the discussion. Estimated time ~15 minutes.*

### Loop introduction

The concept of a loop is fairly common in everyday experience, although we rarely formalize them way we do in programming languages.

- Walk down the hall until the end, then make a right
- Work until 5pm
- If at first you don't succeed, try, try, again
- Repeat 12 times
  - Agents Todd and Dipold enter Starbucks holding hands
  - They stand in line debating what to order
  - etc
- Many examples in music!

If you analyze it, each of these examples share two main components:
- A ```condition``` to test
- A ```body``` to "execute" if the condition is met.

![alt text](https://i.imgur.com/NPAbL0p.png "Loop anatomy")

You've already learned, last week, the boolean expressions that govern a if/then/else branching conditionals.  A while loop's condition is very similar.  The difference is that the while loop will repeat itself until the condition "fails", whereas the if statement is a one-time deal.

Why is this useful?

Computers are excellent at executing statements exactly the same way over and over and over again.  They don't get bored! 

But, it's boring *for us* to type in the same commands over and over again.  And, bored programmers make mistakes.  Loops allow us to specify a tractable number of instructions and then ask the computer to do the busy work of repeating it over and over again, until some condition is met.  And, it's not uncommon to want to repeat a sequence of instructions more than once, sometimes in the exact same form, sometimes slightly changed.

### Indefinite loops

We talked about the similarity of my loop examples, earlier.  But, there's one big difference between the first two of these and the last.  
- Walk down the hall until the end, then make a right
- Work until 5pm
- If at first you don't succeed, try, try, again

In the first two examples, there's a *definite* end to the loop. 

In the case of a hymn, we know how many verses there will be up front.

These constructs are known as ```definite loops``` and are often implemented in Python using something called a ```for loop```, which you'll learn more about later.

But, what about "try, try again"?  *When* will you succeed?  *Will* you succeed?  These are known as ```indefinte loops``` and is a typical use-case for a ```while``` loop.

### Anatomy of an indefinite loop in Python

One of the first loops I ever wrote was something like this (though I wrote it in BASIC, not Python).

```python
i = 0
while (i < 10):
   print("Tom is cool!!!!")
   i = i + 1
```
Let's apply the anatomy lesson to this syntax.

The ```loop condition``` is a test of whether the variable ```i``` is less than 10.

The ```loop body``` was message I wanted my sister to see when she ran my program.

It's often the case that much of the logic in our loop body will be the same each iteration.

In the example I gave, it's the print statement.  That will execute the same exact thing each time.  

The assignment to ```i``` is a litte different.  The value of ```i``` changes each iteration -- and it better, otherwise the loop will never end (more on this later).

Loops become more interesting and more powerful when you can combine the concepts of changing and unchanging logic.

Contast

```python
print("99 bottles of beer on the wall, 99 bottles of beer.  Take one down, pass it around.  98 bottles of beer on the wall.")
print("98 bottles of beer on the wall, 98 bottles of beer.  Take one down, pass it around.  97 bottles of beer on the wall.")
print("97 bottles of beer on the wall, 97 bottles of beer.  Take one down, pass it around.  97 bottles of beer on the wall.")

# etc
# etc
# etc
#
# ...yawn

```

With

```python
num_bottles = 99
while (num_bottles > 0):
   print(num_bottles, "bottles of beer on the wall,", num_bottles, "bottles of beer.")
   print("Take one down, pass it around...")
   
   num_bottles = num_bottles - 1

   print(num_bottles, "bottles of beer on the wall.")
```

Which would you rather write and/or review for correctness? (did you spot the mistake I made in the first program?)

Identifying and separating the logic that changes each iteration from logic that stays the same to utilize a loop construct is a super-power computer scientists have.  It's one you will develop as you practice more programming.  In other words:

```python
is_perfect = False
while (not is_perfect):
   is_perfect = practice()
```


### Loop invariants

Sometimes, designing a loop and/or understanding what it does is challenging.  ```Loop invariants``` are statements about your program that make it easier to understand its execution.

More formally, A ```loop invariant``` is a statement about program variables that is true *before* and *after* each iteration of a loop.

A loop invariant has 3 main parts:

Initialization: The loop invariant must be true before the first execution of the loop.
Maintenance: If the invariant is true before an iteration of the loop, it should be true also after the iteration.
Termination: When the loop is terminated the invariant should tell us something that helps us understand the program.

As an example, let's look at the problem of summing the numbers from 1 to ```n```, where n is some number such that ```n >= 1```.  We can solve this problem using a loop.

```python

sum = 0
current = 1
# initialization: sum is the sum of numbers from 0 to current - 1

while (current <= n):
  # maintenance before loop
  sum = sum + current
  current = current + 1
  # maintenance after loop

# termination: at the end of the loop, sum is n + 1
```
### Infinite loops

It's perfectly sensible to not know up front how many `iterations` your loop will have, or even if it will ever end.

But, there are cases where you accidentally loop forever by mistake.  Consider:

```python
num_bottles = 99
while (num_bottles > 0):
   print(num_bottles, "bottles of beer on the wall,", num_bottles, "bottles of beer.")
   print("Take one down, pass it around...")
   
   num_bottles - 1

   print(num_bottles, "bottles of beer on the wall.")
```

Will this program ever finish?

# Day 2: While loops

## Common loop patterns

### Interactive loops

When would you want to use an indefinite, or even "infinite" loop?  One good use of the indefinite loop is to write interactive loops. Interactive loops allow a user to repeat certain portions of a program based on user input, and keep looping until the user provides a valid input.

Suppose we want to write a program to compute whether a year is a leap year or not.  The program will ask for a year and then print "YYYY is a leap year" or "YYYY is not a leap year".

What if the user inputs 'marshmallow' for the year?  How do we handle that?  A loop is one possibility:

```python
year_input = input("Please enter a year (YYYY): ")
while (not year_input.isnumeric()):
   print("That's not a year!")
   year_input = input("Please enter a year (YYYY): ")

# calculation of whether it's a leap year
# etc
```

### 'Loop and a half' (aka 'break' statements)

Sometimes, it's more convenient to *explicitly* tell Python to STOP looping, rather than implicitly doing it via the variant ```while condition```.  

Let's take the leap year example again.

Anolther way to implement that is:

```python

while (True):
   year_input = input("Please enter a year (YYYY): ")
   if (not year_input.isnumeric()):
      break

   print("That's not a year!")

# calculation of whether it's a leap year
# etc
```

The break statement is the keywork you can use to tell Python to stop looping.  
Some people frown upon these "short-circuit" patterns, but for simple cases it can be pretty useful.

### Nested loops

The examples we've looked at, so far, have had a single ```while``` loop.  But, you can put a ```while``` loop inside another ```while``` loop!

For example, suppose we want to print out the times table.  One way to do it would be something like

```python
x = 1

# 1x
while (x <= 10):
   print(1 * x, end="    ")
   factor = x + 1

print()
x = 1

# 2x
while (x <= 10):
   print(2 * x, end="    ")
   x = x + 1

print()
x = 1

# 3x
while (x <= 10):
   print(3 * x, end="    ")
   x = x + 1

print()
x = 1

# etc
# etc
# yawm
```

This works, but it's boring.  We can do better.

```python

y = 1

# 
while (y <= 10):
   x = 1

   while (x <= 10):
       print(y * x, end="    ")
       x = x + 1

   print()
   y = y + 1

```
### File loops

TBD

