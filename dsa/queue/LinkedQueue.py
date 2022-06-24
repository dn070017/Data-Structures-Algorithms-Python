from __future__ import annotations
from collections.abc import Iterable, Iterator
from dsa.node.Node import Node
from typing import Any, Optional

class LinkedQueueIterator(Iterator):
  def __init__(self, linked_queue: LinkedQueue):
    self.current = linked_queue.first

  def __iter__(self) -> Iterator[LinkedQueue]:
    return self

  def __next__(self) -> Any:
    if self.current is None:
      raise StopIteration
    item = self.current.item
    self.current = self.current.next_node
    return item

class LinkedQueue(Iterable):
  def __init__(self):
    self.n: int = 0
    self.first: Optional[Node] = None
    self.last: Optional[Node] = None

  def __iter__(self) -> Iterator[LinkedQueue]:
    return LinkedQueueIterator(self)

  def __len__(self) -> int:
    return self.n

  def __str__(self) -> str:
    return f'{self.__class__.__name__}({list(self).__str__()})'
  
  def is_empty(self) -> bool:
    return self.n == 0
  
  def peek(self) -> Any:
    if self.is_empty():
      raise IndexError(f'Peek from empty {self.__class__.__name__}')
    return self.first.item

  def dequeue(self) -> Any:
    if self.is_empty():
      raise IndexError(f'Pop from empty {self.__class__.__name__}')
    item = self.first.item
    self.first = self.first.next_node
    self.n -= 1
    return item

  def enqueuee(self, item: Any) -> None:
    node = Node(item)
    if self.is_empty():
      self.first = node
      self.last = node
    else:
      self.last.next_node = node
    self.n += 1
    return
