from __future__ import annotations
from collections.abc import Iterable, Iterator, Hashable, MutableMapping
from copy import deepcopy
from dsa.array.Array import Array
from typing import Any

class Tombstone:
  def __init__(self):
    pass

  def __str__(self) -> str:
    return f"Tombstone"

class DoubleHashingHashTableIterator(Iterator):
  def __init__(self, hash_table: DoubleHashingHashTableIterator):
    self.current_index = 0
    self.hash_table = hash_table

  def __iter__(self) -> Iterator[DoubleHashingHashTableIterator]:
    return self

  def __next__(self) -> Hashable:
    while True:
      if self.current_index >= self.hash_table.size:
        raise StopIteration
      if (self.hash_table.table[self.current_index] is None or 
          isinstance(self.hash_table.table[self.current_index], Tombstone)):
        self.current_index += 1
      else:
        break
    pair = self.hash_table.table[self.current_index]
    self.current_index += 1
    return pair.key

class Pair:
  def __init__(self, key: Hashable, value: Any):
    self.key = key
    self.value = value

  def __str__(self) -> str:
    return f"({self.key}, {self.value})"
  
class DoubleHashingHashTable(MutableMapping):
  def __init__(self, size: int = 5):
    self.n = 0
    self.n_tombstone = 0
    self.size = size
    self.table = Array(size)

  def __setitem__(self, key: Hashable, value: Any) -> None:
    hash_key = hash(key)
    mod_base_1 = self.size
    mod_base_2 = (self.size // 2 + 1)
    mod_hash_key_1 = hash_key % mod_base_1
    mod_hash_key_2 = mod_base_2 - (hash_key % mod_base_2)
    candidate_index = mod_hash_key_1
    pair = Pair(key, value)

    while True:
      if (self.table[candidate_index] is None or
          isinstance(self.table[candidate_index], Tombstone) or
          hash(self.table[candidate_index].key) == hash_key):
        self.table[candidate_index] = pair
        self.n += 1
        if self.alpha >= 0.5:
          self.resize(self.get_next_prime_number_size(expand=True))
        break
      else:
        candidate_index += mod_hash_key_2
      if candidate_index >= self.size:
        candidate_index -= self.size

  def __getitem__(self, key: Hashable) -> Any:
    hash_key = hash(key)
    mod_base_1 = self.size
    mod_base_2 = (self.size // 2 + 1)
    mod_hash_key_1 = hash_key % mod_base_1
    mod_hash_key_2 = mod_base_2 - (hash_key % mod_base_2)
    candidate_index = mod_hash_key_1

    while True:
      if (self.table[candidate_index] is not None and
          not isinstance(self.table[candidate_index], Tombstone) and
          hash(self.table[candidate_index].key) == hash_key):
        return self.table[candidate_index].value
      else:
        candidate_index += mod_hash_key_2  
      if candidate_index >= self.size:
        candidate_index -= self.size
      if self.table[candidate_index] is None:
        break
    raise KeyError(f'{key}')

  def __delitem__(self, key: Hashable) -> None:
    hash_key = hash(key)
    mod_base_1 = self.size
    mod_base_2 = (self.size // 2 + 1)
    mod_hash_key_1 = hash_key % mod_base_1
    mod_hash_key_2 = mod_base_2 - (hash_key % mod_base_2)
    candidate_index = mod_hash_key_1

    while True:
      if (self.table[candidate_index] is not None and
          not isinstance(self.table[candidate_index], Tombstone) and
          hash(self.table[candidate_index].key) == hash_key):
        self.table[candidate_index] = Tombstone()
        self.n -= 1
        self.n_tombstone += 1
        if self.alpha - self.alpha_tombstone and self.size > 5:
          self.resize(self.get_next_prime_number_size(expand=False))
        return
      else:
        candidate_index += mod_hash_key_2  
      if candidate_index == self.size:
        candidate_index -= self.size
      if self.table[candidate_index] is None:
        break
    raise KeyError(f'{key}')

  def __iter__(self) -> DoubleHashingHashTableIterator[DoubleHashingHashTable]:
    return DoubleHashingHashTableIterator(self)

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
    return (self.n + self.n_tombstone) / self.size

  @property
  def alpha_tombstone(self) -> float:
    return self.n_tombstone / self.size

  def clear(self) -> None:
    self.n = 0
    self.n_tombstone = 0
    self.table = Array(self.size)
    return

  def update(self, iterable: Iterable) -> None:
    for key in iterable:
      self[key] = iterable[key]
    return

  def get_next_prime_number_size(self, expand: bool = True) -> int:
    current_size = self.size
    if expand:
      current_size = current_size * 2
    else:
      current_size = current_size // 2
    if current_size < 5:
      return 5
    while True:
      for i in range(2, current_size):
        if (current_size % i) == 0:
          break
      else:
        return current_size
      current_size += 1

