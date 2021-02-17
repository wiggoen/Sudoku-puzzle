import random

"""
An attempt to build a Sudoku puzzle generator and solver with a minimal amount
of imported packages.
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix = [numbers] * 9


elements = sum(len(n) for n in matrix)
factor = 9

#selected = random.randint(1, 9)
selected = random.choice(numbers)


def show_board():
  horisontal_wall = "  +" + "---+" * 9

  print("  ", end=" ")
  for i in range(len(letters)):
    print(" %s " % letters[i], end=" ")
  print("\r")  # Carriage Return
  print(horisontal_wall)


  for index in numbers:
    print("%d |" % index, end=" ")
    for column in matrix[index-1]:
      print("%d |" % column, end=" ")
    print("\r")  # Carriage Return
    print(horisontal_wall)





  return None

show_board()