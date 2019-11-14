
Date: 1/7/2020 (Tuesday)

Lesson: Conditional Execution

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
* `<, >, ==, !, etc`
* `||, &&, ()`
* These allow us to produce boolean values based on the comparison of logical statements
  * `x = 7 < 8` (x = true)
  * `a = 7 >= 8` (a = false)
  * `b = 1 != 2` (b = true)
  * `isEqual = x == y` (true or false depending on what is in `x` and `y`)
* Logical statements can be combined or chained
  * `x = 7 > 8 || 1 < 3` 
  * `a = x == y && u == v`
* Logical statements can be grouped
  * `x = (7 < 8 || 1 < 3) && 5 < 4`
  * `a = (x == y && u == v) || true`
* Logic in our algorithms comes from using these logical operators at runtime to figure out what to do
* `7 < 8` is always true, but `x < y` I have no idea about until the program actually runs

#### If statements
* `If there are two slices of bread...`
* `If there is no strawberry jelly, then eat something else`
* Simple IF - Checks for a condition and executes or does not 
* IF-ELSE - Checks for a condition and goes one of two ways (branching)
* IF-ELIF-ELSE - Checks for multiple conditions in order and executes one (and only one) option
* IF-ELIF-ELIF-ELIF-ELIF-ELIF-ELSE - Can get as complex as you need it to (though there are usually better ways...)
* Nested IF statements (cyclical complexity?)
* Short-circuiting is a mechanism whereby the computer stops as soon as it can determine the final true/falise state
  * if 7 > 8 && 1 < 2
  * if 7 < 8 || 1 < 2
  * if x == y && u > v
  * if x == y || u == v

#### Python particulars
* colon
* indentation
* multiple statement blocks

#### Lab Exercises
* TBD


