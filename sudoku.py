from copy import deepcopy
from dfs import Node

# Class Sudoku untuk papan berukuran 9x9
class Sudoku(Node):

  # Inisialisasi awal
  def __init__(self, puzzle, rows=9, cols=9):
    self.puzzle = puzzle
    self.rows = rows
    self.cols = cols

  # Mengecek apakah angka sudah unik dengan angka lain sepanjang baris
  def check_row(self, row, value):

    for col in range(self.cols):
      if value == self.puzzle[row][col]:
        return False
    return True
  
  # Mengecek apakah angka sudah unik dengan angka lain sepanjang kolom
  def check_col(self, col, value):

    for row in range(self.rows):
      if value == self.puzzle[row][col]:
        return False
    return True
  
  # Mengecek apakah angka sudah unik dengan angka lain dalam petak
  def check_square(self, row, col, value):

    square_row_start = (row // 3) * 3
    square_col_start = (col // 3) * 3

    for row in range(square_row_start, square_row_start + 3):
      for col in range(square_col_start, square_col_start + 3):
        if self.puzzle[row][col] == value:
          return False
    return True
  
  # Mencari sel pertama yang belum ditentukan (bernilai 0) sebagai root tree dari permasalahan
  def find_first_empty_slot(self):

    for row in range(self.cols):
      for col in range(self.rows):
        if self.puzzle[row][col] == 0:
          return row, col

  # Memperluas node saat ini, meng-update papan Sudoku untuk setiap angka yang valid
  def extend_node(self):

    row, col = self.find_first_empty_slot()
    new_puzzles = []
    for number in range(1, 9+1):
      if self.check_row(row, number) and self.check_col(col, number) and self.check_square(row, col, number):
        new_puzzle = deepcopy(self.puzzle)
        new_puzzle[row][col] = number
        new_puzzles.append(Sudoku(new_puzzle))
    return new_puzzles
  
  # Mengecek apakah node saat ini merupakan solusi
  def is_the_solution(self):

    for row in range(self.rows):
      for col in range(self.cols):
        if self.puzzle[row][col] == 0:
          return False
    return True

  # Mencetak papan Sudoku yang sudah ter-solve
  def __str__(self):

    sudoku = ""
    for row in range(self.rows):
      for col in range(self.cols):
        sudoku += f"{self.puzzle[row][col]} "
      sudoku += "\n"
    return sudoku

# Class Sudoku untuk papan yang berukuran 4x4
class Sudoku2(Node):

  def __init__(self, puzzle, rows=4, cols=4):
    self.puzzle = puzzle
    self.rows = rows
    self.cols = cols

  def check_row(self, row, value):
  
    for col in range(self.cols):
      if value == self.puzzle[row][col]:
        return False
    return True

  def check_col(self, col, value):
  
    for row in range(self.rows):
      if value == self.puzzle[row][col]:
        return False
    return True
  
  def check_square(self, row, col, value):
   
    square_row_start = (row // 2) * 2
    square_col_start = (col // 2) * 2

    for row in range(square_row_start, square_row_start + 2):
      for col in range(square_col_start, square_col_start + 2):
        if self.puzzle[row][col] == value:
          return False
    return True
  
  def find_first_empty_slot(self):
  
    for row in range(self.cols):
      for col in range(self.rows):
        if self.puzzle[row][col] == 0:
          return row, col

  def extend_node(self):
 
    row, col = self.find_first_empty_slot()
    new_puzzles = []
    for number in range(1, 4+1):
      if self.check_row(row, number) and self.check_col(col, number) and self.check_square(row, col, number):
        new_puzzle = deepcopy(self.puzzle)
        new_puzzle[row][col] = number
        new_puzzles.append(Sudoku2(new_puzzle))
    return new_puzzles

  def is_the_solution(self):

    for row in range(self.rows):
      for col in range(self.cols):
        if self.puzzle[row][col] == 0:
          return False
    return True
  
  def __str__(self):
  
    sudoku = ""
    for row in range(self.rows):
      for col in range(self.cols):
        sudoku += f"{self.puzzle[row][col]} "
      sudoku += "\n"
    return sudoku
