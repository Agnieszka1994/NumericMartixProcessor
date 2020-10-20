
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def print(self):
        print('The result is:')
        for row in self.matrix:
            print(*row)

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
        self.print()

    def transpose_side(self):
        self.matrix = [[self.matrix[y][x]
                        for y in reversed(range(0, self.columns))]
                       for x in reversed(range(0, self.rows))]
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
