# Numeric Matrix Processor 

This program allows you to perform a variety of operations on matrices including addition, multiplication, finding the determinant, and dealing with inverse matrices.

**In this stage, the program supports:**

- addition
- multiplication by number
- matrix by matrix multiplication
- transposition along the main diagonal
- transposition along the side diagonal
- transposition along the vertical line
- transposition along the horizontal line

**Features in progress:** 

- finding the determinant
- finding the inverse of a matrix

## Get started!
- download the repository
- run the program in the command-line
```
NumericMatrixProcessor > python main.py
```
**The program executes the below steps:**
- Prints a menu consisting of 4 options. 
- Reads the user's choice.
- Reads all data (matrices, constants) needed to perform the chosen operation. 
- Calculates the result and outputs it. 
- Repeats all these steps.

### Sample usage:
```
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 2
Enter size of matrix: > 2 2
Enter matrix:
> 1.5 7.0
> 6.0 5.0
Enter constant: > 0.5
The result is:
0.75 3.5
3.0 2.5
```