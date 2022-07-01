from __future__ import annotations
from collections.abc import Iterable, Iterator
from dsa.array.Array import Array
from typing import Any

class StackIterator(Iterator):
  def __init__(self, stack: Stack):
    self.current = stack.n - 1
    self.stack = stack

  def __iter__(self) -> Iterator[Stack]:
    return self

  def __next__(self) -> Any:
    if self.current < 0:
      raise StopIteration
    item = self.stack.data[self.current]
    self.current -= 1
    return item

class Stack(Iterable):
  def __init__(self):
    self.n: int = 0
    self.data: Array = Array(1)

  def __len__(self) -> int:
    return self.n

  def __str__(self) -> str:
    return f'{self.__class__.__name__}({list(self.data).__str__()})'

  def __iter__(self) -> Iterator[Stack]:
    return StackIterator(self)
  
  def is_empty(self) -> bool:
    return self.n == 0
  
  def peek(self) -> Any:
    if self.is_empty():
      raise IndexError(f'Peek from empty {self.__class__.__name__}')
    return self.data[self.n-1]

  def pop(self) -> Any:
    if self.is_empty():
      raise IndexError(f'Pop from empty {self.__class__.__name__}')
      
    item = self.data[self.n-1]
    self.data[self.n-1] = None
    self.n -= 1
    if self.n > 0 and self.n <= len(self.data) // 4:
      self.data.resize(len(self.data) // 2)
    return item

  def push(self, item: Any) -> None:
    if self.n == len(self.data):
      self.data.resize(2 * self.n)
    self.data[self.n] = item
    self.n += 1
    return


    