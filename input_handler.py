from string import digits


def split_and_cast_to_list(digits_only_string):
    return list(map(int, digits_only_string.split()))


def split_and_cast_to_floats(digits_only_string):
    return list(map(float, digits_only_string.split()))


def digits_only_input(string_input) -> bool:
    accepted = digits + ' -.'
    for element in string_input:
        if element not in accepted:
            return False
        return True
    return False


def length_correct(list_of_ints, target_length):
    if len(list_of_ints) > target_length:
        print('Too many arguments!')
        return False
    elif len(list_of_ints) < target_length:
        print('Too few arguments!')
        return False
    else:
        return True


def input_validator(string_input, required_length):
    string_copy = string_input
    while not digits_only_input(string_copy):
        string_copy = input('Invalid input! Only digits accepted! \
        \n Enter new dimensions or "esc" to escape: ')
        if string_copy == 'esc':
            return [0, 0]

    if digits_only_input(string_copy):
        casted_list = split_and_cast_to_list(string_copy)
        if length_correct(casted_list, required_length):
            return casted_list
        else:
            print('Default size [1, 1]:')
            return [1, 1]
    else:
        return [1, 1]


def process_input(user_input):
    rows, columns = input_validator(user_input, 2)
    matrix = validate_matrix_of_floats(rows, columns)
    return matrix


def validate_matrix_of_floats(rows, columns):
    print('Enter matrix:')
    matrix = []
    assigned_rows = 0
    while rows > assigned_rows:
        user_input = input()
        if user_input == 'esc':
            return [[0.0]]
        if not digits_only_input(user_input):
            continue
        else:
            list_to_append = split_and_cast_to_floats(user_input)
            if not length_correct(list_to_append, columns):
                continue
            else:
                matrix.append(list_to_append)
                assigned_rows += 1
    return matrix
