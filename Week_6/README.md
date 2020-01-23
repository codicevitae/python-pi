
# Week 6: Functions 


## Goals & Objectives

- To be able to define new functions in Python
- To understand the details of function calls and parameter passing in Python.
- To write programs that use functions to reduce code duplication and increase modularity

## Lesson - Functions (aka methods, subroutines, )

You can think of a function as a subprogram - a small program within a program (a unit of reuseable code). In math, a function computes a result from given values. In Python, a function is a block of code that performs a specific task. A function is a way to organize the code into specific tasks that can be repeated in more than a single place in a program. 

We have used various types of functions without knowing it:
- `print`
- `input`
- `Math.floor`

## Function definition

We define a function in python with the `def` keyword:
```python
def myFunction():
    print("Hello from myFunction")
    # additional code here
```

The statements that are indented below the function are what will get exectuted when the function is **called** in another place. 

## Function call or invocation

Functions are called or invoked when we type the name of the function, followed by parenthesis. 

```python
def myFunction():   # define function
    print("Hello from myFunction")
    # additional code here

myFunction()    # call function
```

### Exercise

- Create a new function called `greet` that prints a greeting to the user. 
- Call this function within the file. 
- Use nano to create this program, as we will build upon it.
- Raise your hand when done.

<br/><br/><br/><br/><br/><br/><br/>

## Function arguments / parameters

Additionally, functions can take input (called arguments or parameters) in order to do their work. These arguments come after the function name, within the parenthesis. There can be as many as needed, with each separated by a comma. The ordering of the arguments determines their values in the function.

```python
def myFunction(first_name, last_name, is_birthday):
    print("Hello ", first_name, " ", last_name)
    if is_birthday:
        print("Happy birthday!")
    else:
        print("How are you today?")

myFunction("Josh", "Bouckenooghe", false)
myFunction("John", "Doe", true)
```

What happens when we don't pass the correct number of arguments the function was defined for? 

```python
def myFunction(name, birthday):
    print("Hello ", name)
    if birthday:
        print("Happy birthday" )

myFunction("Josh")
```

### Key = value arguments

Python also supports the **key** = **value** style arguments for function calls. This way, the ordering of the arguments do not matter.

```python
def myFunction(name, age):
    print("Hello ", name)
    if age > 65:
        print("You are a senior citizen")

myFunction(age = 1234, name = "Josh")
```

### Exercise

- Modify your `greet` function to take in the name of the user and their age. 
- Call this function more than once with different names and ages. 
- Call the function at least once with one of the arguments missing.

