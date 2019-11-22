## Day 1
Date: 1/7/2020 (Tuesday)

## Lesson: Conditional Execution

#### Goals:
* To understand what an algorithm is
* To understand the value of conditional execution
* To understand how to test for conditions
* To understand if and if-else statements
* To understand Python's if-else syntax and indentation requirements

#### Algorithms
* How do you define a process or solution to a problem?
* How do you make a peanut butter and jelly sandwich?
* An algorithm is a set of instructions designed to achieve a certain goal or solve a certain problem
* We all use algorithms every day of our lives, we just may not call them that
  1. How do you get ready for school in the morning?
  2. How do you make your bed?
  3. How do you make a Peanut Butter Sandwich?

#### Limitations of Linear Program Flow
* So far the instructions you have given the computer have been linear sequences of simple instructions
* All instructions executed once and once only
* No chance to deal with problems that arise
* Using PB&J algorithm from above, discuss the drawbacks of having one fixed set of instrctions that happen once each
  * What if the bag of bread is empty?
  * How do you know when to stop putting PB on the bread?
  * What if you stop after one scoop of jelly? Is it enough?
  * What if you run out of Peanut Butter?
  * What if you have more than one kind of jelly?

#### Logical Operators
* Have already covered Boolean type (TRUE/FALSE)
* `<, >, ==, !=, >=, <=`
* `and, or, not`
* These allow us to produce boolean values based on the comparison of logical statements
  * `x = 7 < 8` (x = true)
  * `a = 7 >= 8` (a = false)
  * `b = 1 != 2` (b = true)
  * `isEqual = x == y` (true or false depending on what is in `x` and `y`)
* Logical statements can be combined or chained
  * `x = 7 > 8 or 1 < 3` 
  * `a = x == y and u == v`
* Logical statements can be grouped
  * `x = (7 < 8 or 1 < 3) and 5 < 4`
  * `a = (x == y and u == v) or true`
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

#### Lab Exercises
* TBD

## Day 2 - 
Date: 1/9/20 (Thursday)

## Lesson: Branching

#### Goals:
* To understand more complex conditional statments (if-else and if-elif-else)
* To understand how to nest conditional statements 
* To understand Python's syntax and indentation requirements

#### IF/ELSE
* What if an IF statement is not enough?
* What if I need to take different actions based on the true/false result of a statement?
  * I can say:
    ```
    if x == y:
      print('yep')
    if x != y:
      print('nope')
    ```
  * But I always want one and only one of those to happen, why check twice?  
* IF/ELSE Checks for a condition and goes one of two ways (branching)
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
  
#### IF/ELIF/ELSE
* What if two options is not enough?
* IF/ELIF/ELSE Checks for multiple conditions in order and executes one (and only one) option
* IF/ELIF/ELIF/ELIF/ELIF/ELIF/ELSE
  * Can get as complex as you need it to
  * There are usually better ways, though!

#### Nested Logical Statements
* Nested IF statements
* Indentation is key

#### Stretch Goals Based on Time
* Simplifying Logical statements
  * Can spend weeks talking about how to simplify logic
  * Use short-circuiting to your benefit
  * Try to avoid overly complex statements that are:
    1. Hard to understand
    2. Prone to typos
    3. Hard to test and find problems
* Think about how to test your code as you write it
  * For every level of nesting, you have more test cases to try to make sure things work
  * The more you simplify the logic of your program, the easier it is to test
  * Cyclical complexity is a term that describes the number of possible paths through your code
  * Greater cyclical complexity leads to bugs that are harder to find and code that is harder to read
  
#### Lab Exercises
TBD
