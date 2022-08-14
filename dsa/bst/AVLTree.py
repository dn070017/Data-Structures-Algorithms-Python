#%%
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from dsa.bst.BinarySearchTree import BinarySearchTree, BinarySearchTreeIterator
from typing import Any, TypeVar

class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...

ComparableT = TypeVar('ComparableT', bound=Comparable)

class AVLTreeNode:
  def __init__(self, key: ComparableT, value: Any):
    self.key = key
    self.value = value
    self.left: AVLTreeNode = None
    self.right: AVLTreeNode = None
    self.height: int = 1

  def __repr__(self) -> str:
    return f"{self.__class__.__name__}({{{self.key}: {self.value}}})"

class AVLTree(BinarySearchTree):
  def __init__(self):
    super().__init__()
    self.root: AVLTreeNode = None

  def __setitem__(self, key: ComparableT, value: Any) -> None:
    super().__setitem__(key, value)
    return

  def __getitem__(self, key: ComparableT) -> Any:
    return super().__getitem__(key)    

  def __delitem__(self, key: ComparableT) -> None:
    super().__delitem__(key)
    return

  def insert(self, node, key, value):
    if node is None:
      self.n += 1
      return AVLTreeNode(key, value)

    if key < node.key:
      node.left = self.insert(node.left, key, value)
    elif key > node.key:
      node.right = self.insert(node.right, key, value)
    else:
      node.value = value
      return node

    node.height = 1 + max(
        self.get_node_height(node.left),
        self.get_node_height(node.right))
    balance_factor = self.get_balance_factor(node)

    if balance_factor > 1 and key < node.left.key:
        return self.right_rotate(node)

    if balance_factor < -1 and key > node.right.key:
        return self.left_rotate(node)

    if balance_factor > 1 and key > node.left.key:
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    if balance_factor < -1 and key < node.right.key:
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    return node

  def delete(self, node, key):
 
    if node is None:
      raise KeyError(f'{key}')

    if key < node.key:
      node.left = self.delete(node.left, key)
    elif key > node.key:
      node.right = self.delete(node.right, key)
    else:
      if node.left is None:
        temp = node.right
        node = None
        return temp 
      elif node.right is None:
        node = node.left
        node = None
        return temp
      else:
        temp = self.min_of_subtree(node.right)
        node.key = temp.key
        node.value = temp.value
        node.right = self.delete(node.right, temp.key)

      if node is None:
        return node

      node.height = 1 + max(
          self.get_node_height(node.left),
          self.get_node_height(node.right))

      balance_factor = self.get_balance_factor(node)

      if balance_factor > 1 and self.get_balance_factor(node.left) >= 0:
          return self.right_rotate(node)

      if balance_factor < -1 and self.get_balance_factor(node.right) <= 0:
          return self.left_rotate(node)

      if balance_factor > 1 and self.get_balance_factor(node.left) < 0:
          node.left = self.left_rotate(node.left)
          return self.right_rotate(node)

      if balance_factor < -1 and self.get_balance_factor(node.right) > 0:
          node.right = self.right_rotate(node.right)
          return self.left_rotate(node)
      
    return node

  def get_node_height(self, node: AVLTreeNode) -> int:
    if node is None:
      return 0
    return node.height

  def get_balance_factor(self, node: AVLTreeNode) -> int:
      if node is None:
        return 0
      node_height_left = self.get_node_height(node.left)
      node_height_right = self.get_node_height(node.right)
      return node_height_left - node_height_right

  def min_of_subtree(self, node):
    if node is None or node.left is None:
      return node
 
    return self.min_of_subtree(node.left)

  def left_rotate(self, z: AVLTreeNode):

      y = z.right
      T2 = y.left

      y.left = z
      z.right = T2

      z.height = 1 + max(
          self.get_node_height(z.left),
          self.get_node_height(z.right))
      y.height = 1 + max(
          self.get_node_height(y.left),
          self.get_node_height(y.right))

      return y

  def right_rotate(self, z: AVLTreeNode):

      y = z.left
      T3 = y.right

      y.right = z
      z.left = T3

      z.height = 1 + max(
          self.get_node_height(z.left),
          self.get_node_height(z.right))
      y.height = 1 + max(
          self.get_node_height(y.left),
          self.get_node_height(y.right))

      return y

  def __iter__(self) -> BinarySearchTreeIterator:
    return BinarySearchTreeIterator(self)

  def __len__(self) -> int:
    return self.n
