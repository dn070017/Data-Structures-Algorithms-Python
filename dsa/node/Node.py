from __future__ import annotations
from typing import Any, Optional

class Node:
  def __init__(self, item: Any, next_node: Optional[Node] = None):
    self.item: Any = item
    self.next_node: Node = next_node