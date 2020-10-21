
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def print(self):
        print('The result is:')
        for row in self.matrix:
            for element in row:
                if element % 1 == 0:
                    print('{:>5s}'.format(str(round(element))), end=' ')
                elif element % 0.1 == 0:
                    print('{:>5s}'.format(str(round(element, 1))), end=' ')
                else:
                    print('{:>5s}'.format(str(round(element, 2))), end=' ')
            print('\n', end='', flush=True)

    def multiply_by_matrix(self, other):
        if self.columns != other.rows:
            print('Multiplication Impossible!')
            return [[]]
        else:
            result = [[0 for x in range(other.columns)] for y in range(self.rows)]
            for x in range(self.rows):
                for y in range(other.columns):
                    for z in range(other.rows):
                        result[x][y] += self.matrix[x][z] * other.matrix[z][y]
            self.matrix = result
            self.print()

    def update_attributes(self):
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def add_matrix(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print('The operation cannot be performed.')
            return []
        self.matrix = [[self.matrix[x][y] + other.matrix[x][y]
                        for y in range(self.columns)]
                       for x in range(self.rows)]
        self.print()

    def multiply_by_scalar(self, scalar):
        self.matrix = [[self.matrix[x][y] * scalar
                        for y in range(self.columns)] for x in range(self.rows)]
        self.print()

    def transpose_main(self):
        self.matrix = [[self.matrix[y][x]
                        for y in range(self.columns)]
                       for x in range(self.rows)]
        self.update_attributes()
        self.print()

    def transpose_side(self):
        self.matrix = [[self.matrix[y][x]
                        for y in reversed(range(0, self.columns))]
                       for x in reversed(range(0, self.rows))]
        self.update_attributes()
        self.print()

    def transpose_vertical(self):
        self.matrix = [[self.matrix[x][y]
                        for y in reversed(range(0, self.rows))]
                       for x in range(0, self.columns)]
        self.print()

    def transpose_horizontal(self):
        self.matrix = [[self.matrix[x][y]
                        for y in range(self.rows)]
                       for x in reversed(range(0, self.columns))]
        self.print()

    @staticmethod
    def get_cofactor(matrix, i, j):
        return [row[: j] + row[j + 1:] for row in (matrix[: i] + matrix[i + 1:])]

    def determinantOfMatrix(self, matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return value
        # initialize Sum to zero
        running_sum = 0
        # loop to traverse each column of matrix a.
        for current_column in range(len(matrix)):
            # calculating the sign corresponding to co-factor of that sub matrix.
            sign = (-1) ** current_column
            # calling the function recursively to
            # get determinant value of a sub-matrix obtained
            sub_determinant = self.determinantOfMatrix(self.get_cofactor(matrix, 0, current_column))
            # adding the calculated determinant to the total sum
            running_sum += (sign * matrix[0][current_column] * sub_determinant)

        return running_sum

    @staticmethod
    def transpose(matrix):
        return map(list, zip(*matrix))

    def inverse(self):
        determinant = self.determinantOfMatrix(self.matrix)
        if determinant == 0 or self.rows != self.columns \
                or self.rows == 1 or self.columns == 1:
            print("This matrix doesn't have an inverse.")
            return 0
        # special case for 2x2 matrix:
        elif self.rows == 2 and self.columns == 2:
            return [[self.matrix[1][1] / determinant, -1 * self.matrix[0][1] / determinant],
                    [-1 * self.matrix[1][0] / determinant, self.matrix[0][0] / determinant]]
        # find matrix of cofactors
        cofactors = []

        for row in range(self.rows):
            cofactor_row = []
            for col in range(self.columns):
                minor = self.get_cofactor(self.matrix, row, col)
                cofactor_row.append(((-1) ** (row + col)) * self.determinantOfMatrix(minor))
            cofactors.append(cofactor_row)
        cofactors = [[cofactors[y][x] for y in range(len(cofactors))]
                     for x in range(len(cofactors))]
        for row in range(len(cofactors)):
            for col in range(len(cofactors)):
                self.matrix[row][col] = cofactors[row][col] / determinant
        self.print()
