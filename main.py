from matrix_class import *
from input_handler import *
import os

while True:
    os.system('cls')
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('0. Exit')
    choice = input('Your choice: ')
    if choice not in digits:
        print('Only digits from 0 to 5 allowed!')
        input()
        continue

    choice = int(choice)
    # ------------------------------------------------------------------------------------------------
    if choice == 1:

        first_dimensions = input('Enter size of first matrix: ')
        matrix_a = Matrix(process_input(first_dimensions))
        second_dimensions = input('Enter size of second matrix: ')
        matrix_b = Matrix(process_input(second_dimensions))
        matrix_a.add_matrix(matrix_b)
    # ------------------------------------------------------------------------------------------------
    elif choice == 2:

        dimensions = input('Enter size of matrix: ')
        matrix_a = Matrix(process_input(dimensions))
        constant = float(input('Enter constant: '))
        matrix_a.multiply_by_scalar(constant)
    # ------------------------------------------------------------------------------------------------
    elif choice == 3:

        first_dimensions = input('Enter size of first matrix: ')
        matrix_a = Matrix(process_input(first_dimensions))
        second_dimensions = input('Enter size of second matrix: ')
        matrix_b = Matrix(process_input(second_dimensions))
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

            dimensions = input('Enter size of matrix: ')
            matrix = Matrix(process_input(dimensions))
            matrix.transpose_main()
        # --------------------------------------------------------------------------------------------
        elif option == 2:

            dimensions = input('Enter size of matrix: ')
            matrix = Matrix(process_input(dimensions))
            matrix.transpose_side()
        # --------------------------------------------------------------------------------------------
        elif option == 3:

            dimensions = input('Enter size of matrix: ')
            matrix = Matrix(process_input(dimensions))
            matrix.transpose_vertical()
        # --------------------------------------------------------------------------------------------
        elif option == 4:

            dimensions = input('Enter size of matrix: ')
            matrix = Matrix(process_input(dimensions))
            matrix.transpose_horizontal()
        # --------------------------------------------------------------------------------------------
        else:
            print('No such option available!')
            break
    # ------------------------------------------------------------------------------------------------
    elif choice == 0:
        break
    else:
        print('No such option available!')

    input("Press Enter to continue...")
