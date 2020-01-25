## Week 4 Day 1
Date: 1/7/2020 (Tuesday)

## Lesson: Conditional Execution

#### Goals:
* To understand what an algorithm is
* To understand the value of conditional execution
* To understand how to test for conditions
* To understand if statements
* To understand Python's if syntax and indentation requirements

#### Background/Review
* What does a computer do? (Exactly what you tell it to!)
* How does a computer store and process data and instructions?
  1. Ones and Zeros
  2. Review binary discussion
  3. Stored on disk as on/off bits magnetically
  4. Processed in CPU as on/off bit electrically and/or magnetically
* Why don't we have to think in ones and zeros? (Abstraction - higher-level langages are our friends!)

#### Algorithms
* See if anyone can define the term in their own words.
* How do you define a process or solution to a problem?
* An algorithm is a set of instructions designed to achieve a certain goal or solve a certain problem
* We all use algorithms every day of our lives, we just may not call them that
  1. How do you get ready for school in the morning?
  2. How do you make your bed?
  3. How do you make a Peanut Butter Sandwich? 
* Class participation - write an algorithm for PB&J on the board based on their input for steps

#### Limitations of Linear Program Flow
* Have students review what commands they have learned
* So far the instructions you have given the computer have been linear sequences of simple instructions
* All instructions executed once and once only
* No chance to deal with problems that arise
* Using PB&J algorithm from earlier, discuss the drawbacks of having one fixed set of instrctions that happen once each
  * What if the bag of bread is empty?
  * How do you know when to stop putting PB on the bread?
  * What if you stop after one scoop of jelly? Is it enough?
  * What if you run out of Peanut Butter?
  * What if you have more than one kind of jelly?

#### Logical Operators
* Have already covered Boolean type (TRUE/FALSE)
* `<, >, ==, !=, >=, <=`
  * `1 < 2` (True)
  * `2 < 1` (False)
* Can be chained using `and, or, not`
  * `1 < 2 and 2 < 4` (True)
  * `1 < 2 and 4 < 1` (False)
  * `1 < 2 or 4 < 1` (True)
  * `1 < 2 or 2 < 4` (True)
  * `not 1 > 2` (True)
* These allow us to produce boolean values based on the comparison of logical statements
  * `x = 1 < 2` (x = true)
  * `a = 1 >= 2` (a = false)
  * `b = 1 != 2` (b = true)
  * `isEqual = x == y` (true or false depending on what is in `x` and `y`)
* Logical statements in assignments can also be combined or chained
  * `x = 7 > 8 or 1 < 3` 
  * `a = x == y and u == v`
* Logical statements can be grouped
  * `x = (7 < 8 or 1 < 3) and 5 < 4` (False)
  * `a = (x == y and u == v) or true` (True)
* Logic in our algorithms comes from using these logical operators at runtime to figure out what to do
* `7 < 8` is always true, but `x < y` I have no idea about until the program actually runs

#### If statements
* Simple IF - Checks for a condition and executes or does not 
  * `If there are two slices of bread, make a sandwich`
  * `If there is no strawberry jelly, then eat something else`
* Short-circuiting is a mechanism whereby the computer stops as soon as it can determine the final true/falise state
  * `if 7 > 8 and 1 < 2`
  * `if 7 < 8 or 1 < 2`
  * `if x == y and u > v`
  * `if x == y or u == v`

#### Python particulars
* colon
* indentation
* multiple statement blocks
* Example:
   ```
  if x > y:
    print("x is greater than y")
  ```

#### Lab Exercises
* Write a short Python script that you can run at the command line that will:
  1. Request two input values
  2. Compare them
  3. If the first is less than the second, print out a statement telling the user the first is less than the second
* Stretch Goals:
  1. In the results printed out, include the actual values entered
  2. What happens if you do not enter number values?
  3. What happens if you enter one numeric value and one string? Two strings?

## Week 4 Day 2 - 
Date: 1/9/20 (Thursday)

## Lesson: Branching

#### Goals:
* To understand more complex conditional statements (if-else and if-elif-else)
* To understand how to nest conditional statements 
* To understand Python's syntax and indentation requirements

#### if-else
* What if an `if` statement is not enough?
* What if I need to take different actions based on the true/false result of a statement?
  * I can say:
    ```
    if x == y:
      print('yep')
    if x != y:
      print('nope')
    ```
  * But I always want one and only one of those to happen, why check twice?  

* `if-else` Checks for a condition and goes one of two ways (branching)
  * Now I can say:
    ```
      if x == y:
        print('yep')
      else:
        print('nope')
    ```
  * Less chance for error
  * Easier to understand what I mean
  * No chance both statements will ever be executed!
  
#### if / elif / else
* What if two options is not enough?

* `if-elif-else` Checks for multiple conditions in order and executes one (and only one) option
* `elif` is a short-hand way of saying "else if"

  ```
  if condition_1:
    ...
  elif condition_2:
    ...
  else:
    ...
  ```

* `if-elif-elif-elif-elif-elif-elif-elif-else`
  * Can get as complex as you need it to
  * There are usually better ways, though!

#### Nested `if` Statements
* You can "nest" if statements within each other
* Indentation is key so Python knows which commands are in which block
* Can get complicated quickly!

  ```
  if _condition 1 :
    ...
    ...
    if condition_2 :
      ...
      ...
      if condition_3 :
        ...
        ...
      else:
        ...
        ...
    else:
     ...
     ...
  else:
    ...
    ...
  ```
  
* Can get as complex as you need it to
* There are usually better ways, though!

#### Misc thoughts on complexity
* Think about how to test your code as you write it
  * For every level of nesting, you have more test cases to try to make sure things work
  * The more you simplify the logic of your program, the easier it is to test
  * The easier it is to test your program, the more confidence you can have that it is doing what you want!
  
#### Lab Exercises
* Evaluate as a group to understand what will happen:
  * What will be printed out and why?
    ```
    x = 7
    if x < 10:
      x = 10
    else:
      x = 0
      print(x)
    ```
  
  * Make a small change below. Now what will be printed?
    ```
    x = 7
    if x < 10:
      x = 10
    else:
      x = 0
    print(x)
    ```
  
  * What will appear after running the following `if/elif/else` statement?
    ```
    x = 0
    y = 10
    if x < y:
      x = y
    elif x == y:
      x = x - 1
    else:
      x = 0
    print(x)
    print(y)
    ```
  
* Guided Exercises:
  * Type in the following commands and see if it behaves the way you expect (either in a new file in nano or in the Python3 shell)

    ```
    x = 100
    y = 101
    if x < y:
      x = x + 1
    
    if x < y: 
      print(x, "is less than", y)
    elif x > y:
      print(x, "is greater than", y)
    else:
      print(x, "is equal to", y)
    ```
  
  * Type in the following commands and see if it behaves the way you expect (either in a new file in nano or in the Python3 shell)

    ```
    x = True
    y = False
    if x or y:
      print("at least one is true")
    else:
      print("both are false")
    
    if x and y:
      print("both are true")
    else:
      print("at least one is false")
  
    if x not y:
      print("x is true and y is false")
    else:
      print("x is false or y is true")
    ```

* Individual Exercises for further exploration:
  * Write commands to take two input numbers and print out a different message when:
    
    a. the first is greater than the second, 
    
    b. they are equal, or 
    
    c. the first is less than the second
    
    Remember the `input()` and `eval()` commands from last class in order to treat the input as a Number rather than a String:
    ```
    x = eval(input("Enter a number: "))
    ```
    This will interpret the input as a number rather than a text string, so that the comparison can be done correctly

  * Write commands to prompt the user for their name. Write out different greetings based on whether their name is:

    a. Fred

    b. George

    c. your name

    d. anyone else
    

#### Short-Circuiting
* The computer only evaluates as much as it must to get its answer.
* It will stop as soon as it hits a condition that makes the overall statement False

* Example:
  ```
  if (1 < 0 and 3 < 4) and (5 < 6 or 0 == 0):
  ```
  * This will stop as soon as it evaluates `1 < 0` as false because nothing else on that line will make the overall statement true.
* Example:
  ```
  if (1 < 0 and 3 < 4) or (5 < 6 and 0 == 0):
  ```
  * This has to evaluate the entire line because the `or` means even if the first part is false, the overall expression could still be true

* Don't worry about short-circuiting for simple programs, but it will save the computer time and resources if you keep in mind that it is possible as things get more complicated.
