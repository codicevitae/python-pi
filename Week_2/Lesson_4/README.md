# Expressions and Arithmetic

## Goal
The goal of this lesson is understand what expressions are and how they are different from statements, and how they can cause different kinds of errors.

## Objectives
- The student will be able to identify the arithmetic operators and use them to create valid expressions

- The student will be able to identify logical operators and use them to create valid expressions

- The student will learn a few string operators and use them to create valid string expressions

- The student will be able to tell the difference between syntax errors and runtime errors

## Lesson
*These concepts will be given interactively, via whiteboard/projector. Students can take notes during the discussion. Estimated time ~15 minutes.*

The grammar of imperative languages is composed of statements, expressions, and values. Today we will discuss expressions.

Expressions are *evaluated* to obtain a *value*. They are always evaluated before they are used in a statement. We know three types of values (number, string, boolean), so we will look at three kinds of expressions, focussing on numbers.

An expression is built using variables, values and operators. Each type has a set of operators that can be used to work with that type. For numbers, the operators will look familiar.

| Operator | What it means                                               |
| -------- | ----------------------------------------------------------- |
| x + y    | Addition                                                    |
| x - y    | Subtraction                                                 |
| x * y    | Multiplication                                              |
| x / y    | Floating point division                                     |
| x // y   | Integer division (compare to Math.floor)                    |
| x % y    | Modular division (remainder)                                |
| -x       | Negation (unary)                                            |

If an expression contains only integers, the value will be an integer (unless you use floating point division).

If an expression contains any floating point numbers, the value will be a floating point number.

Python follows normal math operator precendence (left to right, negation, multiplication/division, addition/subtraction). This can be modified with paranthesis.

```python
3 + 6 * 2           # 15
(3 + 6) * 2         # 18
```

String expressions are much simplier than numbers, as there is only a single operator, the `+`. When this operator is applied to strings, the value is the contatenation of those strings into a single string.

```python
'John' + " " + 'Smith'     # "John Smith"
```

While we can mix integers and floating point numbers in an expression, we can't mix numbers and strings:

```python
3 + 'dog'   # Returns an error
```


syntax vs traceback





## Activities
*Students can work through these activities directly on their Pi. Estimated time ~ 20 minutes.*

1. Let the user input a number of seconds and convert this to a time of day in the format hh:mm. For example, 11900 seconds is 3:33. 

2. Modify your previous program to handle the case if the number of seconds is greater than a single day. Change the format to show days, hours and minutes. For example, 3421356 seconds is 39d 14h 22m

3. If you have 1 - (1 / 2) - (1 / 2) with real numbers, the answer should be zero. Does Python calculate this to zero? What about 1 - (1 / 3) - (1 /3) - (1 / 3) ? What's the difference?

