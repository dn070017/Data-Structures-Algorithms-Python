from __future__ import annotations
from collections.abc import Iterable, Iterator
from dsa.array.Array import Array
from typing import Any

class QueueIterator(Iterator):
  def __init__(self, queue: Queue):
    self.first = queue.first
    self.last = queue.last
    self.queue = queue

  def __iter__(self) -> Iterator[Queue]:
    return self

  def __next__(self) -> Any:
    if self.first > self.last:
      raise StopIteration
    item = self.queue.data[self.first]
    self.first += 1
    return item

class Queue(Iterable):
  def __init__(self):
    self.n: int = 0
    self.first: int = 0 
    self.last: int = -1
    self.data: Array = Array(1)

  def __len__(self) -> int:
    return self.n

  def __str__(self) -> str:
    return f'{self.__class__.__name__}({list(self.data).__str__()})'
  
  def __iter__(self) -> Iterator[Queue]:
    return QueueIterator(self)

  def is_empty(self) -> bool:
    return self.n == 0
  
  def peek(self) -> Any:
    if self.is_empty():
      raise IndexError(f'Peek from empty {self.__class__.__name__}')
    return self.data[self.first]

  def dequeue(self) -> Any:
    if self.is_empty():
      raise IndexError(f'Pop from empty {self.__class__.__name__}')
    item = self.data[self.first]
    self.data[self.first] = None
    self.first += 1
    self.n -= 1
    if self.n > 0 and self.n == len(self.data) // 4:
      self.data.resize(len(self.data) // 2, self.first)
      self.first = 0
      self.last = self.n - 1
    if self.n == 0:
      self.first = 0
      self.last = -1
    return item

  def enqueue(self, item: Any) -> None:
    if self.n == len(self.data):
      self.data.resize(2 * self.n)
    self.last += 1
    self.data[self.last] = item
    self.n += 1
    return


