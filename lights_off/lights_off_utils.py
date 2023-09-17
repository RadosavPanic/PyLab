# Utility functions for lights off game

def turnoff_light(matrix, x, y, num_rows, num_cols):
    matrix[x][y] = "X"

    if x-1 >= 0:
        matrix[x-1][y] = "X"
    if x+1 < num_rows:
        matrix[x+1][y] = "X"
    if y-1 >= 0:
        matrix[x][y-1] = "X"
    if y+1 < num_cols:
        matrix[x][y+1] = "X"
    if x-1 >= 0 and y-1 >= 0:
        matrix[x-1][y-1] = "X"
    if x+1 < num_rows and y-1 >= 0:
        matrix[x+1][y-1] = "X"
    if x+1 < num_rows and y+1 < num_cols:
        matrix[x+1][y+1] = "X"
    if x-1 >= 0 and y+1 < num_rows:
        matrix[x-1][y+1] = "X"


def target_field(matrix, num_rows, num_cols):
    coords = input("Insert coordinates in format (row, column): ")
    coords = coords.split(",", 2)
    x = int(coords[0]) - 1
    y = int(coords[1]) - 1
    if x > num_rows or x < 0 or y > num_cols or y < 0:
        print("Invalid input!")
        return
    turnoff_light(matrix, x, y, num_rows, num_cols)


def check(matrix):
    for row in matrix:
        if "O" in row:
            return False
    return True


def print_matrix(matrix, num_rows, num_cols):
    print(" ", end=" ")
    for column in range(0, num_cols):
        print(str(column+1), end=" ")
    print()
    for row in range(0, num_rows):
        print(str(row+1), end=" ")
        print(" ".join(matrix[row]))

