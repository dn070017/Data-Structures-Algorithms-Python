from dsa.heap.MinHeap import MinHeap

class MaxHeap(MinHeap):
  def __init__(self):
    super().__init__()

  def heapify_up(self, index: int) -> None:
    parent_index = index // 2
    while index > 1 and self.data[parent_index] < self.data[index]:
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
      elif self.data[child_b_index] > self.data[child_a_index]:
        exchange_to = child_b_index
      else:
        exchange_to = child_a_index
      if self.data[index] >= self.data[exchange_to]:
        break
      self.data.exchange(index, exchange_to)
      index = exchange_to
    return