def process_input(command):
    while True:
        try:
            rows, columns = list(map(int, input(command).split()))
        except ValueError:
            print('Invalid input! You should enter exactly 2 integers!\n')
        else:
            return validate_matrix_of_floats(rows, columns)


def validate_matrix_of_floats(rows, columns):
    print('Enter matrix: ')
    new_matrix = []
    assigned_rows = 0
    while rows > assigned_rows:
        try:
            list_to_append = list(map(float, input().split()))
        except ValueError:
            print('Invalid input! You should enter only numbers!')
        else:
            if len(list_to_append) > columns or len(list_to_append) < columns:
                print('Incorrect number of arguments in row!')
                continue
            else:
                new_matrix.append(list_to_append)
                assigned_rows += 1
    return new_matrix
