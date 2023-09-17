# Lights off
"""
Game based on 2D 5x5 matrix that random chooses 'X' values for lights-off and
value 'O' for lights-on.
User inputs coordinates for field where light turns off, as well as all
adjacent fields that are vertically/horizontally aligned with input field.
Game ends after matrix is filled only with 'X' values.
"""

import random
from lights_off_utils import *

num_rows = 5
num_cols = 5

""" Detailed random fill of matrix
matrix = list()
for x in range(0, num_rows):
    matrix.append(list())
    for y in range(0, num_cols):
        matrix[x].append(random.choice("XO"))
"""

matrix = [[random.choice("XO") for x in range(5)] for y in range(5)]  # generator function

while True:
    print_matrix(matrix, num_rows, num_cols)
    target_field(matrix, num_rows, num_cols)
    if check(matrix):
        print_matrix(matrix, num_rows, num_cols)
        break

print("Game ended. You have turned off all the lights! Congratulations!")
