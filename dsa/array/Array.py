from collections.abc import MutableSequence
from typing import Any

class Array(MutableSequence):
  def __init__(self, size: int = 0):
    self.n = size
    self.__data = [None] * size 

  def __getitem__(self, key: int) -> Any:
    return self.__data[key]
  
  def __delitem__(self, key: int) -> None:
    self.__data[key] = None
    return

  def __setitem__(self, key: int, val: Any) -> None:
    self.__data[key] = val
    return

  def __len__(self):
    return len(self.__data)

  def __str__(self):
    return f'{self.__class__.__name__}({self.__data.__str__()})'

  def resize(self, size: int = 0, start: int = 0):
    duplicate = [None] * size
    max_index = min(self.n, size + start)
    i = 0
    for j in range(start, max_index):
      duplicate[i] = self.__data[j]
      i += 1

    self.__data = duplicate
    self.n = size
    return

  def insert(self, key: int, val: Any) -> None:
    duplicate = [None] * (self.n + 1)
    i = 0
    for item in self.__data:
      duplicate[i] = item
      if i == key:
        duplicate[i] = val
      i += 1

    self.__data = duplicate
    self.n += 1
    return