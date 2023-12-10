import os
from sudoku1 import Sudoku
from dfs_algorithm import DFS

#Membaca file '.txt' dan mengembalikan list sebagai data dari file input
def read_data(filename): 
  data = []
  
  try:
      with open(f"puzzles/{filename}", "r", encoding="utf-8") as f:
          data = [[int(number) for number in line.strip().split() if number] for line in f.readlines()]
  except FileNotFoundError:
      return None
  return data

#Panggil fungsi read_data dan buat objek sudoku baru. Kemudian jalankan algoritma DFS dan cetak sudoku yang sudah terselesaikan
def main():
  filename = input("Please enter the number of the text file: ")
  filename += ".txt"
  data = read_data(filename)

  if data is not None:
    sudoku = Sudoku(data)
    print("Depth First Search")
    dfs = DFS(sudoku)
    dfs.search()
  else:
    print("This file does not exit. Please enter another file name")

if __name__ == '__main__':
  main()
