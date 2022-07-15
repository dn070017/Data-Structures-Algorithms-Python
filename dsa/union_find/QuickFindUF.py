from dsa.array.Array import Array

class QuickFindUF:
  def __init__(self, n_nodes):
    self.n_components: int = n_nodes
    self.n_nodes: int = n_nodes
    self.component_id: Array = Array(n_nodes)
    for i in range(n_nodes):
      self.component_id[i] = i

  def __str__(self) -> str:
    return str(self.component_id)

  def __len__(self) -> int:
    return self.n_components

  def validate_index(self, index) -> None:
    if index < 0 or index >= self.n_nodes:
      message = ''.join((
          f'{index} is not a valid index for {self.__class__.__name__} '
          f'with size {len(self.component_id)}'))
      raise IndexError(message)
  
  def is_connected(self, index_a, index_b) -> bool:
    self.validate_index(index_a)
    self.validate_index(index_b)
    return self.component_id[index_a] == self.component_id[index_b]

  def union(self, index_a, index_b) -> None:
    self.validate_index(index_a)
    self.validate_index(index_b)
    component_id_a = self.component_id[index_a]
    component_id_b = self.component_id[index_b]
    if component_id_a == component_id_b:
      return
    for i in range(self.n_nodes):
      if self.component_id[i] == component_id_a:
        self.component_id[i] = component_id_b
    self.n_components -= 1
    return

  def find(self, index) -> int:
    self.validate_index(index)
    return self.component_id[index]