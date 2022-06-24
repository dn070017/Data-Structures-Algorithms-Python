from __future__ import annotations
from collections.abc import Iterable, Iterator
from dsa.node.Node import Node
from typing import Any, Optional

class LinkedStackIterator(Iterator):
  def __init__(self, linked_stack: LinkedStack):
    self.current = linked_stack.last

  def __iter__(self) -> Iterator[LinkedStack]:
    return self

  def __next__(self) -> Any:
    if self.current is None:
      raise StopIteration
    item = self.current.item
    self.current = self.current.next_node
    return item

class LinkedStack(Iterable):
  def __init__(self):
    self.n: int = 0
    self.last: Optional[Node] = None

  def __iter__(self) -> Iterator[LinkedStack]:
    return LinkedStackIterator(self)

  def __len__(self) -> int:
    return self.n

  def __str__(self) -> str:
    return f'{self.__class__.__name__}({list(self).__str__()})'
  
  def is_empty(self) -> bool:
    return self.n == 0
  
  def peek(self) -> Any:
    if self.is_empty():
      raise IndexError(f'Peek from empty {self.__class__.__name__}')
    return self.last.item

  def pop(self) -> Any:
    if self.is_empty():
      raise IndexError(f'Pop from empty {self.__class__.__name__}')
    item = self.last.item
    self.last = self.last.next_node
    self.n -= 1
    return item

  def push(self, item: Any) -> None:
    node = Node(item)
    if self.is_empty():
      self.last = node
    else:
      node.next_node = self.last
      self.last = node
    self.n += 1
    return
