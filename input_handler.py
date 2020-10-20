from string import digits


def digits_only_input(string) -> bool:
    accepted = digits + ' -.'
    for element in string:
        if element not in accepted:
            print('Invalid input! Only digits accepted')
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
    if digits_only_input(string_input):
        casted_list = split_and_cast_to_list(string_input)
        if length_correct(casted_list, required_length):
            return True
        else:
            return False
    return False


def split_and_cast_to_list(digits_only_string):
    return list(map(int, digits_only_string.split()))


def split_and_cast_to_floats(digits_only_string):
    return list(map(float, digits_only_string.split()))


def process_input(dimensions):
    if input_validator(dimensions, 2):
        rows, columns = split_and_cast_to_list(dimensions)
        matrix = validate_matrix_of_floats(rows, columns)
        return matrix
    else:
        return []


def validate_matrix_of_floats(rows, columns):
    matrix = []
    assigned_rows = 0
    while rows > assigned_rows:
        user_input = input()
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
