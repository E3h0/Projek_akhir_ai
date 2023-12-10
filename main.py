from sudoku import Sudoku, Sudoku2
from dfs import DFS

# Membaca file '.txt' dan mengembalikan list sebagai data dari file input
def read_data(filename): 
  data = []
  total_digits = 0

  try:
    with open(f"puzzles/{filename}", "r", encoding="utf-8") as f:
      for line in f.readlines():
        numbers = [int(number) for number in line.strip().split() if number]
        total_digits += len(numbers)
        data.append(numbers)
  except FileNotFoundError:
    return None, 0

  return data, total_digits

# Panggil fungsi read_data dan buat objek sudoku baru. Lalu jalankan fungsi DFS dan cetak sudoku yang ter-solve
def main():
  filename = input("Masukkan nama file: ") + ".txt"
  data, total_digits = read_data(filename)

  if data is not None:
    if total_digits == 81:
      sudoku = Sudoku(data)
    elif total_digits == 16:
      sudoku = Sudoku2(data)
    print("\n// Sudoku Solver dengan DFS //\n")
    DFS(sudoku).search()
  else:
    print("File tidak ditemukan.")

main()
