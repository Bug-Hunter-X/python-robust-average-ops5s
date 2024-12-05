# Python ZeroDivisionError Example
This repository demonstrates a common coding error in Python: the ZeroDivisionError. The `bug.py` file contains a function that calculates the average of a list of numbers but does not handle the case of an empty list, leading to a division by zero error. The `bugSolution.py` file shows a corrected version of the function that addresses this issue.

## How to Reproduce
1. Clone this repository.
2. Run `bug.py`. Observe the `ZeroDivisionError`. 
3. Run `bugSolution.py` to see the solution.

## Solution
The solution involves checking if the input list is empty before performing the division. If the list is empty, the function returns 0 to prevent the error.