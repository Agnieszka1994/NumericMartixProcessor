from matrix_class import *
from input_handler import *
import os

FIRST_INPUT = 'Enter size of first matrix: '
SECOND_INPUT = 'Enter size of second matrix: '
SINGLE_INPUT = 'Enter size of matrix: '
CONST_INPUT = 'Enter constant: '


while True:
    
    
    
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')
    choice = input('Your choice: ')
    if choice not in digits:
        print('Only digits from 0 to 6 allowed!')
        input("Press Enter to continue...")
        continue

    choice = int(choice)
    # ------------------------------------------------------------------------------------------------
    if choice == 1:

        matrix_a = Matrix(process_input(input(FIRST_INPUT)))
        matrix_b = Matrix(process_input(input(SECOND_INPUT)))
        matrix_a.add_matrix(matrix_b)
    # ------------------------------------------------------------------------------------------------
    elif choice == 2:

        matrix_a = Matrix(process_input(input(SINGLE_INPUT)))
        matrix_a.multiply_by_scalar(float(input(CONST_INPUT)))
    # ------------------------------------------------------------------------------------------------
    elif choice == 3:

        matrix_a = Matrix(process_input(input(FIRST_INPUT)))
        matrix_b = Matrix(process_input(input(SECOND_INPUT)))
        matrix_a.multiply_by_matrix(matrix_b)
    # ------------------------------------------------------------------------------------------------
    elif choice == 4:
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        option = int(input('Your choice: '))
        # --------------------------------------------------------------------------------------------
        if option == 1:

            matrix = Matrix(process_input(input(SINGLE_INPUT)))
            matrix.transpose_main()
        # --------------------------------------------------------------------------------------------
        elif option == 2:

            matrix = Matrix(process_input(input(SINGLE_INPUT)))
            matrix.transpose_side()
        # --------------------------------------------------------------------------------------------
        elif option == 3:

            matrix = Matrix(process_input(input(SINGLE_INPUT)))
            matrix.transpose_vertical()
        # --------------------------------------------------------------------------------------------
        elif option == 4:

            matrix = Matrix(process_input(input(SINGLE_INPUT)))
            matrix.transpose_horizontal()
        # --------------------------------------------------------------------------------------------
        else:
            print('No such option available!')
            break
    # ------------------------------------------------------------------------------------------------
    elif choice == 5:

        matrix = Matrix(process_input(input(SINGLE_INPUT)))
        print(f'The result is: \n{matrix.determinantOfMatrix(matrix.matrix)}')
    # ------------------------------------------------------------------------------------------------
    elif choice == 6:

        matrix = Matrix(process_input(input(SINGLE_INPUT)))
        matrix.inverse()
    # --------------------------------------------------------------------------------------------
    elif choice == 0:
        break
    else:
        print('No such option available!')

    input("Press Enter to continue...")
