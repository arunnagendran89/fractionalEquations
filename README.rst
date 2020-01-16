=====================
Fractional Arithmetic
=====================
:Authors: Arun N A Muralidharan

:Version: 1.0 of 2020/01/16

Introduction
------------
The project contains the classes required to parse and
solve stringed equations formed with fractional operands.
For example

::

    ? 1/2 + 1/2
    = 1

A command line interface is provided along with the class
to help run the application to solve fractional equations.


Installation
------------
The project was developed with Python 3.6.6 and is
recommended to be run using the same. No other additional
packages should be required.

From the project folder run

::

    python cliFractionalEquation.py

Example Usage
-------------

- Adding two fraction operands

::

    ? 3_1/4 + 5/6
    =  4_1/12

- Subtracting two fraction operands

::

    ? -3_3/8 - -2_5/8
    =  -3/4

- Multiply two fraction operands

::

    ? 1/4 * 0
    =  0

    ? -3_1/9 * 9
    =  -28

- Divide two fractions

::

    ? -3_1/9 / -3_1/9
    =  1

    ? -1/5 / 5_0/1
    =  -1/25

Change Logs
-----------
- Commit 1: Create a class for operands. add basic apis
- Commit 2: Update __reduceFractions implementation and add comments.
- Commit 3: Add Command Line Interface, descriptive custom exceptions and readme.

