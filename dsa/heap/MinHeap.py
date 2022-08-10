#%%
from collections.abc import Iterable
from dsa.array.Array import Array
from typing import Any

#%%
class MinHeap(Iterable):
  def __init__(self):
    self.data: Array = Array(1)
    self.n = 0

  def __len__(self) -> int:
    return self.n
 
  def __iter__(self) -> None:
    pass

  def insert(self, x: Any) -> None:
    if self.n == len(self.data) - 1:
      self.data.resize(2 * len(self.data))
    
    self.n += 1
    self.data[self.n] = x
    self.heapify_up(self.n)
    return

  def peek(self) -> Any:
    if self.n == 0:
      raise IndexError(f'Peek from empty {self.__class__.__name__}')
    return self.data[1]

  def pop(self) -> None:
    if self.n == 0:
      raise IndexError(f'Pop from empty {self.__class__.__name__}')
    result = self.data[1]
    self.data.exchange(1, self.n)
    self.n -= 1
    self.heapify_down(1)
    self.data[self.n + 1] = None
    if self.n > 0 and self.n == (len(self.data) - 1) / 4:
      self.data.resize(0.5 * len(self.data))
    return result
  
  def heapify_up(self, index: int) -> None:
    parent_index = index // 2
    while index > 1 and self.data[parent_index] > self.data[index]:
      self.data.exchange(index, parent_index)
      index = parent_index
      parent_index = index // 2
    return

  def heapify_down(self, index: int) -> None:
    while 2 * index <= self.n:
      child_a_index = index * 2
      child_b_index = index * 2 + 1
      if child_b_index > self.n:
        exchange_to = child_a_index
      elif self.data[child_b_index] < self.data[child_a_index]:
        exchange_to = child_b_index
      else:
        exchange_to = child_a_index
      if self.data[index] <= self.data[exchange_to]:
        break
      self.data.exchange(index, exchange_to)
      index = exchange_to
    return

