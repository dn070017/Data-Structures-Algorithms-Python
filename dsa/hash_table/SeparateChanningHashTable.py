from __future__ import annotations
from collections.abc import Iterable, Iterator, Hashable, MutableMapping
from copy import deepcopy
from dsa.array.Array import Array
from typing import Any, Optional

class SeparateChanningHashTableIterator(Iterator):
  def __init__(self, hash_table: SeparateChanningHashTable):
    self.current_index = -1
    self.current_pair = None
    self.hash_table = hash_table

  def __iter__(self) -> Iterator[SeparateChanningHashTable]:
    return self

  def __next__(self) -> Hashable:
    while self.current_pair is None:
      self.current_index += 1
      if self.current_index >= self.hash_table.size:
        raise StopIteration
      self.current_pair = self.hash_table.table[self.current_index]

    pair = self.current_pair
    self.current_pair = self.current_pair.next_pair
    return pair.key

class Pair:
  def __init__(
      self,
      key: Hashable,
      value: Any,
      next_pair: Optional[Pair] = None):
    self.key = key
    self.value = value
    self.next_pair = next_pair
  
  def __str__(self) -> str:
    return f"({self.key}, {self.value}) -> {self.next_pair}"

class SeparateChanningHashTable(MutableMapping):
  def __init__(self, size: int = 4):
    self.n = 0
    self.size = size
    self.table = Array(size)

  def __setitem__(self, key: Hashable, value: Any) -> None:
    hash_key = hash(key)
    mod_hash_key = hash_key % self.size
    pair = Pair(key, value)
    if self.table[mod_hash_key] is None:
      self.table[mod_hash_key] = pair
      self.n += 1
    else:
      existing_pair = self.table[mod_hash_key]
      while True:
        if hash(existing_pair.key) == hash_key:
          existing_pair.value = value
          return
        elif existing_pair.next_pair is not None:
          existing_pair = existing_pair.next_pair
        else:
          break
      existing_pair.next_pair = pair
      self.n += 1
      if self.alpha >= 10:
        self.resize(self.size * 2)

  def __getitem__(self, key: Hashable):
    hash_key = hash(key)
    mod_hash_key = hash_key % self.size
    if self.table[mod_hash_key] is not None:
      existing_pair = self.table[mod_hash_key]
      while True:
        if hash(existing_pair.key) == hash_key:
          return existing_pair.value
        elif existing_pair.next_pair is not None:
          existing_pair = existing_pair.next_pair
        else:
          break
    raise KeyError(f'{key}')

  def __delitem__(self, key: Hashable):
    hash_key = hash(key)
    mod_hash_key = hash_key % self.size
    if self.table[mod_hash_key] is not None:
      previous_pair = None
      existing_pair = self.table[mod_hash_key]
      while True:
        if hash(existing_pair.key) == hash_key:
          if previous_pair is None:
            self.table[mod_hash_key] = existing_pair.next_pair
          else:
            previous_pair.next_pair = existing_pair.next_pair
          self.n -= 1
          if self.alpha <= 0.5 and self.size > 4:
            self.resize(self.size // 2)
          return existing_pair.value
        elif existing_pair.next_pair is not None:
          previous_pair = existing_pair
          existing_pair = existing_pair.next_pair
        else:
          break
    raise KeyError(f'{key}')

  def __iter__(self) -> SeparateChanningHashTableIterator[SeparateChanningHashTable]:
    return SeparateChanningHashTableIterator(self)

  def __len__(self) -> int:
    return self.n
  
  def __str__(self) -> str:
    message = ''.join((
      f'N: {self.n}\nSize: {self.size}\nLoading Factor: {self.alpha}\n',
      f'Array:\n'
    ))
    for i, data in enumerate(self.table):
      message += f'- {i:>02}: {data}\n'
    return message

  def resize(self, size: int) -> None:
    old_hash_table = deepcopy(self)
    self.clear()
    self.size = size
    self.table = Array(size)
    self.update(old_hash_table)
    return

  @property
  def alpha(self) -> float:
    return self.n / self.size

  def clear(self) -> None:
    self.n = 0
    self.table = Array(self.size)
    return

  def update(self, iterable: Iterable) -> None:
    for key in iterable:
      self[key] = iterable[key]
    return