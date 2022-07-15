from dsa.array.Array import Array

class PathCompressionRankedQuickUnionUF:
  def __init__(self, n_nodes):
    self.n_components: int = n_nodes
    self.n_nodes: int = n_nodes
    self.parent_id: Array = Array(n_nodes)
    self.rank: Array = Array(n_nodes)
    for i in range(n_nodes):
      self.parent_id[i] = i
      self.rank[i] = 1

  def __str__(self) -> str:
    return str(self.parent_id)

  def __len__(self) -> int:
    return self.n_components

  def validate_index(self, index) -> None:
    if index < 0 or index >= self.n_nodes:
      message = ''.join((
          f'{index} is not a valid index for {self.__class__.__name__} '
          f'with size {len(self.parent_id)}'))
      raise IndexError(message)
  
  def is_connected(self, index_a, index_b) -> bool:
    self.validate_index(index_a)
    self.validate_index(index_b)
    return self.parent_id[index_a] == self.parent_id[index_b]

  def union(self, index_a, index_b) -> None:
    self.validate_index(index_a)
    self.validate_index(index_b)
    root_a = self.find(index_a)
    root_b = self.find(index_b)
    if root_a == root_b:
      return
    if self.rank[root_a] < self.rank[root_b]:
      self.parent_id[root_a] = root_b
    elif self.rank[root_a] > self.rank[root_b]:
      self.parent_id[root_b] = root_a
    else:
      self.parent_id[root_b] = root_a
      self.rank[root_a] += 1
    self.n_components -= 1
    return

  def find(self, index) -> int:
    self.validate_index(index)
    while index != self.parent_id[index]:
      self.parent_id[index] = self.parent_id[self.parent_id[index]]
      index = self.parent_id[index]
    return index