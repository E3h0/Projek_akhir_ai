from abc import ABC, abstractmethod

# Class untuk merepresentasikan node di dalam graph DFS
class Node(ABC):

  @abstractmethod
  def is_the_solution(self):
    pass

  @abstractmethod
  def extend_node(self):
    pass

  @abstractmethod
  def __str__(self):
    pass

# Class untuk algoritma pencarian DFS
class DFS:

  # Inisialisasi awal
  def __init__(self, start):
    self.start_state = start
    self.frontier = [self.start_state]
    self.checked_nodes = []
    self.number_of_steps = 0
  
  # Meng-insert node ke awal frontier (frontier = kumpulan node yang belum dieksplorasi)
  def insert_to_frontier(self, node):

    self.frontier.insert(0, node)
  
  # Menghapus node di awal frontier dan menambahkannya ke dalam list checked_nodes
  def remove_from_frontier(self):

    first_node = self.frontier.pop(0)
    self.checked_nodes.append(first_node)
    return first_node

  # Mengecek apakah list frontier sudah habis
  def frontier_is_empty(self):

    if len(self.frontier) == 0:
      return True
    return False

  # Algoritma pencarian solusi
  def search(self):

    while True:

      self.number_of_steps += 1
      
      if self.frontier_is_empty():
        print(f"No Solution Found after {self.number_of_steps} steps!")
        break
        
      selected_node = self.remove_from_frontier()
      
      # Mengecek selected_node merupakan solusi
      if selected_node.is_the_solution():
        print(f"Solusi ditemukan dalam {self.number_of_steps - 1} langkah\n")
        print(selected_node)
        break

      # Mengekstensi node
      new_nodes = selected_node.extend_node()

      # Menambahkan node yang diekstensi ke dalam frontier
      if len(new_nodes) > 0:
        for new_node in new_nodes:
          if new_node not in self.frontier and new_node not in self.checked_nodes:
            self.insert_to_frontier(new_node)
