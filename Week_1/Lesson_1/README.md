
Date: 12/3/2019 (Tuesday)

Lesson: Computers and programs

#### Goals 
* To understand the roles of hardware and software in computer systems.
* To understand the basic design of a modern computer.
* To understand how to run a python script. 
* To learn the purpose of a programming language.

#### Definitions
* Computer: **A machine that can carry out a sequence of operations as specified in a computer program.**
* Computer program: **A detailed set of instructions telling a computer exactly what to do.**

#### Hardware
* Have you ever looked inside a computer before (raise of hands)? 
* What is a computer? What is required for something to be considered a computer? 
    - microwave
    - doorbell
    - vending machine
    - lamp
* How is a computer different from a device such as a clock or flashlight?
* When was the first **programmable** computer conceived of?

* Who knows what this is? 
![Pi](https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Raspberry_Pi_3_B%2B_%2839906369025%29.png/1200px-Raspberry_Pi_3_B%2B_%2839906369025%29.png)
* It isn't required to know all the details about a computer to be a computer scientist, but it helps (as knowing a few things about a car helps any driver).
* The main parts of a computer are:
    * CPU
    * Volatile or main memory (RAM)
    * Permanent memory (hard disk drive (HDD), solid state drive (SSD))
    * Input devices (mouse, keyboard)
    * Output devices (monitor, printer)
* Every computer is just a machine for executing programs.
* Computers have become as common place as automobiles. However, understanding how they work are a different matter.
* Computers are to computer science as telescopes are to astronomy. They (computers) are an important tool in the subject, but not the sole focus of it.
* **Demo / Lab**
    * Open and examine your rasberry pi. 
    * Label each part. Check your answers against the board.

#### Software Programs
* Computer software (programs): "And the borrower is servant to the lender" (Prov 22:7), additionally, the hardware is servant to the software. 
* The way to get the hardware to perform actions is via software, and specifically software programming. 
* Software is written in one or more programming languages. 
* A programming language is either compiled or interpreted. 
    * A **compiled** language takes the human readable text, and compiles/translates it to a form that the CPU can directly execute. 
    * An **interpreted** language will execute the code instruction at a time, via an interpreter (aka virtual machine).
* What happens when the language is abiguous? 
    * ![Img](http://www.teamjimmyjoe.com/wp-content/uploads/2011/12/1_churchKill.jpg)
    * ![Img2](https://cybertext.files.wordpress.com/2012/11/commas.png?w=450&h=447)
    * ![Img3](https://www.thepoke.co.uk/wp-content/uploads/2014/01/BeMM4BsIQAAjrS2.jpg)
    * ![Img4](http://blog.ivman.com/wp-content/CowsCloseGate.jpg)
* Programming languages are precise and sometimes pedantic (but for good reason). 
* The language we will be using is call python. It is an interpreted language. 
* **Demo / Lab**
    * Boot the rasberry pi
    * Verify keyboard input and visual output is working
    * From the terminal, try typing in:
        * python -c "print( 'Hello world' )"
        * What is displayed in response?

#### Terminal / Command line
* One tool that will be used to run, execute, and utilize the computer will be the terminal (aka command line).
* Some commands to get around:
    * **ls** - prints all files/folders in the current directory
    * **cd** - changes the current directory to a new one
    * **mkdir** - creates a new directory with the given name
    * **mv** - moves a file/folder from one location to another
    * **cat** - prints the contents of a file
    * **cp** - copies a file/folder from one location to another
    * **nano** - starts the text editor we will use in class to create our programs
    * When in doubt, **tool-name** --help to see options
        * example: ls --help
* Since this is linux, file paths are deliminated with the / character, instead of the \ character.
* Demo / Lab
    * Create a directory structure/tree with the following layout:
```
    +---Middle-Earth
    |       Hobbit
    |       Fellowship-of-the-Rings
    |       The-Two-Towers
    |       Return-of-the-King
    |
    \---Narnia
            The-Lion-the-Witch-and-the-Wardrobe
            Prince-Caspian
            The-Voyage-of-the-Dawn-Treader
            The-Silver-Chair
            The-Horse-and-His-Boy
            The-Magicians-Nephew
            The-Last-Battle
```